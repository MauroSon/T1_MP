# Importa bibliotecas necessárias
from hashlib import sha256
from database.base_helper import BaseHelper
from flask_jwt_extended import create_access_token
from datetime import timedelta
import base64

# Helper para fazer a interação com o banco de dados 
class AuthHelper(BaseHelper):
    # Método que irá inserir um novo cadastro no banco de dados na tabela "Usuarios"
    def create(self, email: str, senha: str, nome: str, papel: str, feirante: bool,
                identificador: str, foto_perfil: bytes = None) -> tuple[bool, str]:
        msg = ""
        try:
            # Verifica se a conta já está cadastrada com o email fornecido
            login_exists = self.read(email=email)
            if login_exists:
                return False, "Email já registrado."
            
            # Verifica a existência das informações obrigatórias
            if nome  and email and senha and papel and feirante and identificador:
                # Comando SQL para inserir informações no banco de dados
                insert_user_query = """
                                    INSERT INTO 
                                        Usuario (email, senha, nome, papel, feirante, identificador, fotoPerfil)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                                    """

                try:
                    # Criptografa a senha 
                    hashed_senha = sha256(senha.encode()).hexdigest()
                    self.cursor.execute(insert_user_query, ( email, hashed_senha, nome, papel,
                                                             feirante, identificador, foto_perfil))
                    self.conn.commit()
                    msg = "Conta criada com sucesso!"
                    return True, msg

                except Exception as err:
                    self.conn.rollback()
                    return False, str(err)

            else:
                msg = "Campos incompletos."
                return False, msg
        except Exception as err:
            return False, str(err)

    # Método que irá ler um usuário no banco de dados com base na coluna Id (identificador do usuário)
    def read(self, usuario_id: int = None) -> list | None:

        # Verifica a existência do Id
        if usuario_id:
            # Comando SQL para ler usuário da tabela "Usuario" com base na coluna "Id"
            select_user_query = "SELECT * FROM Usuario WHERE usuarioId = %s"

            try:
                self.cursor.execute(select_user_query, (usuario_id,))
                user_data = list(self.cursor.fetchone())
                
                if user_data[-1]:
                    user_data[-1] = base64.b64encode(user_data[-1]).decode('utf-8')

                return user_data 
            
            except Exception as err:
                return None, str(err)
        
        else:
            msg = "Informações não fornecidas."
            return None, msg
        
    # Método que lê todos os usuários do banco de dados
    def read_all(self) -> list | None:
        # Comando SQL para ler todos os usuários da tabela "Usuario"
        select_all_users_query = "SELECT * FROM Usuario"
        try:
            self.cursor.execute(select_all_users_query)
            users_data = list(self.cursor.fetchall())
            users_data = [list(user) for user in users_data]

            # Formata dados retornados
            for user in users_data:
                if user[-1]:
                    user[-1] = base64.b64encode(user[-1]).decode('utf-8')

            # Ordena os usuários por nome
            users_data.sort(key=lambda x: x[3])

            # Mapeia os valores retornados
            for ind in range(len(users_data)):
                users_data[ind] = {
                    "email": users_data[ind][1],
                    "nome": users_data[ind][3],
                    "papel": users_data[ind][5],
                    "feirante": users_data[ind][6],
                    "identificador": users_data[ind][7],
                    "foto_perfil": users_data[ind][-1]
                }
            return users_data
        
        except Exception as err:
            return None, str(err)
         
    # Método que atualiza informações de um usuário no banco de dados
    def update(self, usuario_id: int, new_email: str = None, new_senha: str = None, 
               new_nome: str = None, new_foto_perfil: bytes = None) -> tuple[bool, str]:
        fields_to_update = []
        args = []
        msg = ""
        if new_nome:
            fields_to_update.append("nome = %s")
            args.append(new_nome)

        if new_email:
            fields_to_update.append("email = %s")
            args.append(new_email)

        if new_senha:
            hashed_senha = sha256(new_senha.encode()).hexdigest()
            fields_to_update.append("senha = %s")
            args.append(hashed_senha)
        
        if new_foto_perfil:
            fields_to_update.append("foto_perfil = %s")
            args.append(new_foto_perfil)
        
        if not len(fields_to_update):
            msg = "Informações não fornecidas."
            return False, msg
        
        # Comando SQL para atualizar informações do usuário na tabela "Usuario"
        update_user_query = "UPDATE Usuario SET " + ", ".join(fields_to_update) + "WHERE usuarioId = %s"
        args.append(usuario_id)
        
        try:
            self.cursor.execute(update_user_query, (args))
            self.conn.commit()
            msg = "Usuário atualizado com sucesso."
            return True, msg
        
        except Exception as err:
            self.conn.rollback()
            return False, str(err)
    
    # Método para deletar usuário no banco de dados
    # TODO: colocar metodos para excluir avaliacoes de produtos e lojas
    # TODO: antes de excluir. Checar tambem se usuario eh feirante para poder excluir a loja
    # def delete(self, usuario_id: int) -> tuple[bool, str]:
    #     msg = ""

    #     # Comando SQL para excluir usuário da tabela "Usuario"
    #     delete_user_query = "DELETE FROM Usuario WHERE usuarioId = %s"

    #     # Verifica se o Id foi fornecido
    #     if usuario_id:
    #         try:
    #             user_exists = self.read(usuario_id=usuario_id)
    #             # Verifica se o usuário existe no banco de dados
    #             if user_exists:
    #                 user_have_loans = self.user_have_loans(usuario_id=usuario_id)
    #                 # Verifica se o usuário possui empréstimos ativos
    #                 if user_have_loans:
    #                     msg = "Usuário tem empréstimos ativos."
    #                     return False, msg
                    
    #                 self.cursor.execute(delete_user_query, (usuario_id, ))
    #                 self.conn.commit()
    #                 msg = "Usuário excluído."
    #                 return True, msg
                
    #             msg = "Usuário inexistente."
    #             return False, msg
        
    #         except Exception as err:
    #             self.conn.rollback()
    #             print(f"ERROR: {err}")
    #             return False, err

    #     else:
    #         msg = "Usuário inexistente."
    #         return False, msg
        
    # Método para verificar login
    def autenticacao(self, email: str, senha: str) -> tuple[str, str] | tuple[bool, str]:
        msg = ""

        # Verifica se o email e a senha foram fornecidos
        if email and senha:
            # Criptografa a senha
            hashed_senha = sha256(senha.encode()).hexdigest()
            # Comando SQL para selecionar usuário da tabela "Usuario" com base no email e senha fornecidos
            select_user_query = "SELECT * FROM Usuario WHERE email = %s AND senha = %s"
            try:
                self.cursor.execute(select_user_query, (email, hashed_senha))
                usuario = self.cursor.fetchone()
                # Se as senhas e emails coincidirem, retorna o token de acesso
                if usuario:
                    usuario_id = usuario[0]
                    try:
                        add_claims = {
                            "papel" : usuario[5],
                            "email" : email,
                            "nome" : usuario[4]
                        }

                        # Tempo de validade do token
                        expires = timedelta(minutes=30)

                        # Token JWT de autenticação
                        access_token = create_access_token(identity = usuario_id, additional_claims = add_claims, expires_delta=expires)
                        return True, access_token

                    except Exception as err:
                        return False, str(err)
                    
                else:
                    msg = "Credenciais inválidas."
                    return False, msg
            
            except Exception as err:
                return False, str(err)

        else:
            msg = "Campos incompletos."
            return False, msg

