# Importa helpers necessários
from database.base_helper import BaseHelper
from auth.helper import AuthHelper

# Helper para fazer a interação com o banco de dados 
class LojaHelper(BaseHelper):
    # Método que irá inserir um novo cadastro no banco de dados na tabela "Lojas"
    def create(self, feirante_id: int, localizacao: str, nome: str, categoria: str, descricao: str) -> tuple[bool, str]:
        try:
            # Verifica se usuario existe no banco de dados
            usuario_existe = AuthHelper.read(usuario_id=feirante_id)
            if not(usuario_existe):
                msg = "Loja inexistente."
                return False, msg
            
            # Verifica a existência das informações obrigatórias
            if nome  and localizacao and categoria:
                # Comando SQL para inserir informações no banco de dados
                insert_loja_query = """
                                    INSERT INTO 
                                        Loja (Feirante_id, Localizacao, Nome, Categoria, Descricao)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                                    """

                try:
                    # Executa o comando SQL
                    self.cursor.execute(insert_loja_query, (feirante_id, localizacao, nome, categoria, descricao))
                    self.conn.commit()
                    msg = "Loja criada com sucesso!"
                    return True, msg

                except Exception as err:
                    self.conn.rollback()
                    return False, str(err)

            else:
                msg = "Campos incompletos."
                return False, msg
        except Exception as err:
            return False, str(err)

    # Método que irá ler uma loja no banco de dados com base na coluna Loja_id
    def read(self, loja_id: int = None) -> list | None:
        # Verifica a existência do id da loja
        if loja_id:
            # Comando SQL para ler loja da tabela "Loja" com base na coluna "Loja_id"
            select_loja_query = "SELECT * FROM Loja WHERE Loja_id = %s"

            try:
                self.cursor.execute(select_loja_query, (loja_id,))
                loja_data = list(self.cursor.fetchone())

                return loja_data 
            
            except Exception as err:
                return None, str(err)
        
        else:
            msg = "Informações não fornecidas."
            return None, msg
        
    # Método que lê todas as lojas do banco de dados
    def read_all(self) -> list | None:
        # Comando SQL para ler todas as lojas da tabela "Loja"
        select_all_lojas_query = "SELECT * FROM Loja"
        try:
            self.cursor.execute(select_all_lojas_query)
            lojas_data = list(self.cursor.fetchall())
            lojas_data = [list(loja) for loja in lojas_data]

            # Ordena as lojas por nome
            lojas_data.sort(key=lambda x: x[3])

            # Mapeia os valores retornados
            for ind in range(len(lojas_data)):
                lojas_data[ind] = {
                    "feirante_id": lojas_data[ind][1],
                    "localizacao": lojas_data[ind][2],
                    "nome": lojas_data[ind][3],
                    "cateogira": lojas_data[ind][4],
                    "descricao": lojas_data[ind][5]
                }
            return lojas_data
        
        except Exception as err:
            return None, str(err)
         
    # Método que atualiza informações de uma loja no banco de dados
    def update(self, loja_id: int, new_nome: str = None, new_localizacao: str = None, 
               new_categoria: str = None, new_descricao: str = None) -> tuple[bool, str]:
        fields_to_update = []
        args = []
        if new_nome:
            fields_to_update.append("Nome = %s")
            args.append(new_nome)

        if new_localizacao:
            fields_to_update.append("Localizacao = %s")
            args.append(new_localizacao)

        if new_categoria:
            fields_to_update.append("Categoria = %s")
            args.append(new_categoria)

        if new_descricao:
            fields_to_update.append("Descricao = %s")
            args.append(new_descricao)
        
        if not len(fields_to_update):
            msg = "Informações não fornecidas."
            return False, msg
        
        # Comando SQL para atualizar informações da loja na tabela "Loja"
        update_loja_query = "UPDATE Loja SET " + ", ".join(fields_to_update) + "WHERE Loja_id = %s"
        args.append(loja_id)
        
        try:
            self.cursor.execute(update_loja_query, (args))
            self.conn.commit()
            msg = "Loja atualizada com sucesso."
            return True, msg
        
        except Exception as err:
            self.conn.rollback()
            return False, str(err)
    
    # Método para excluir loja no banco de dados
    def delete(self, loja_id: int) -> tuple[bool, str]:
        # Comando SQL para excluir loja da tabela "Loja"
        delete_loja_query = "DELETE FROM Loja WHERE Loja_id = %s"

        loja_existe = self.read(loja_id=loja_id)
        # Verifica se a loja existe no banco de dados
        if loja_existe:
            try:
                self.cursor.execute(delete_loja_query, (loja_id, ))
                self.conn.commit()
                msg = "Loja excluída."
                return True, msg
            
            except Exception as err:
                self.conn.rollback()
                return False, str(err)
        else:
            msg = "Loja inexistente."
            return False, msg


