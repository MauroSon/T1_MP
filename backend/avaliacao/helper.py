# Importa helpers necessários
from database.base_helper import BaseHelper
from auth.helper import AuthHelper
from loja.helper import LojaHelper
from produto.helper import ProdutoHelper
import base64

# Helper para fazer a interação com o banco de dados 
class AvaliacoesHelper(BaseHelper):
    # Método que irá inserir uma nova avaliacao no banco de dados
    def create(self, usuario_id: int , nota: int, comentario: str = None, 
               loja_id: int = None, produto_id: int = None) -> tuple[bool, str]:

        usuario_existe = AuthHelper.read(usuario_id=usuario_id)
        if not usuario_existe:
            msg = "Usuario não encontrado."
            return False, msg
        
        if not (loja_id or produto_id):
            msg = "Parametros nao fornecidos."
            return False, msg        

        # Verifica a existência das informações obrigatórias
        if nota:
            if loja_id:
                # Verifica se loja esta cadastrada no banco de dados
                loja_existe = LojaHelper.read(self, loja_id=loja_id)
                if not loja_existe:
                    msg = "Loja não encontrada."
                    return False, msg

                else:
                    insert_avaliacao_query = """
                                                INSERT INTO Avaliacao_loja (Usuario_id, Loja_id, Nota, Comentario)
                                                VALUES (%s, %s, %s, %s)
                                            """
                    try:
                        # Executa o comando SQL
                        self.cursor.execute(insert_avaliacao_query, (usuario_id, loja_id, nota, comentario))
                        self.conn.commit()
                        
                    except Exception as err:
                        self.conn.rollback()
                        return False, str(err)
                    
            if produto_id:
                # Verifica se produto esta cadastrada no banco de dados
                produto_existe = ProdutoHelper.read(self, produto_id=produto_id)
                if not produto_existe:
                    msg = "Produto não encontrado."
                    return False, msg

                else:
                    insert_avaliacao_query = """
                                                INSERT INTO Avaliacao_produto (Usuario_id, Produto_id, Nota, Comentario)
                                                VALUES (%s, %s, %s, %s)
                                            """
                    try:
                        # Executa o comando SQL
                        self.cursor.execute(insert_avaliacao_query, (usuario_id, produto_id, nota, comentario))
                        self.conn.commit()
                        
                    except Exception as err:
                        self.conn.rollback()
                        return False, str(err)

        else:
            msg = "Campos incompletos."
            return False, msg
            
    def read(self, avaliacao_id: int, type_review: str) -> list | None:
        select_review_query = f"SELECT * FROM Avaliacao_{type_review} WHERE {type_review.capitalize()}_id = %s"
        try:
            self.cursor.execute(select_review_query, (avaliacao_id))
            review_data = list(self.cursor.fetchone())
            return review_data if review_data else None
        
        except Exception as err:
            print(err)
            return None
        
    def read_all_by_product(self, produto_id: int) -> list[dict] | None:
        select_all_reviews_query = """        
                                            SELECT
                                                ap.Produto_id, ap.Nota, ap.Comentario, 
                                                u.Nome_usuario, u.Email, u.Foto_perfil
                                            FROM Usuario u
                                            JOIN Avaliacao_produto ap ON ap.Usuario_id = u.Usuario_id
                                            WHERE ap.Produto_id = %s
                                           """
        try:
            self.cursor.execute(select_all_reviews_query, (produto_id))
            reviews_data = list(self.cursor.fetchall())
            reviews_data = [list(review) for review in reviews_data]

            # Ordena as avaliacoes pelas notas
            reviews_data.sort(key=lambda x: x[1], reverse=True)

            # Formata dados retornados
            for review in reviews_data:
                if review[5]:
                    review[5] = base64.b64encode(review[5]).decode('utf-8')

            # Mapeia os valores retornados
            for ind in range(len(reviews_data)):
                reviews_data[ind] = {
                    "produto_id": reviews_data[ind][0],
                    "nota": reviews_data[ind][1],
                    "comentario": reviews_data[ind][2],
                    "nome": reviews_data[ind][3],
                    "email": reviews_data[ind][4],
                    "foto_perfil": reviews_data[ind][5]
                }
            return reviews_data
        
        except Exception as err:
            print(err)
            return None
         
    def read_all_by_store(self, loja_id: int) -> list[dict] | None:
        select_all_reviews_query = """        
                                            SELECT
                                                al.Loja_id, al.Nota, al.Comentario, 
                                                u.Nome_usuario, u.Email, u.Foto_perfil
                                            FROM Usuario u
                                            JOIN Avaliacao_loja al ON al.Usuario_id = u.Usuario_id
                                            WHERE al.Loja_id = %s
                                            """
        try:
            self.cursor.execute(select_all_reviews_query, (loja_id))
            reviews_data = list(self.cursor.fetchall())
            reviews_data = [list(review) for review in reviews_data]

            # Ordena as avaliacoes pelas notas
            reviews_data.sort(key=lambda x: x[1], reverse=True)

            # Formata dados retornados
            for review in reviews_data:
                if review[5]:
                    review[5] = base64.b64encode(review[5]).decode('utf-8')

            # Mapeia os valores retornados
            for ind in range(len(reviews_data)):
                reviews_data[ind] = {
                    "loja_id": reviews_data[ind][0],
                    "nota": reviews_data[ind][1],
                    "comentario": reviews_data[ind][2],
                    "nome": reviews_data[ind][3],
                    "email": reviews_data[ind][4],
                    "foto_perfil": reviews_data[ind][5]
                }
            return reviews_data

        except Exception as err:
            print(err)
            return None
                
    def update(self, avaliacao_id: int, type_review: str, new_nota: int = None, new_comentario: str = None) -> tuple[bool, str]:

        review_exist = self.read(avaliacao_id=avaliacao_id, type_review=type_review)
        
        if not review_exist:
            msg = "Avaliação não encontrada."
            return False, msg
        
        fields_to_update = []
        args = []
        if new_nota:
            fields_to_update.append("Nota = %s")
            args.append(new_nota)

        if new_comentario:
            fields_to_update.append("Comentario = %s")
            args.append(new_comentario)

        if len(fields_to_update):
            try:
                update_review_query = f"UPDATE Avaliacao_{type_review} SET " + ", ".join(fields_to_update) + "WHERE Avaliacao_id = %s"
                args.append(avaliacao_id)
                self.cursor.execute(update_review_query, (args))
                self.conn.commit()
                msg = "Avaliação atualizada com sucesso."
            
            except Exception as err:
                self.conn.rollback()
                return False, str(err)

        else:        
            msg = "Informações não fornecidas."
            return False, msg

    def delete(self, avaliacao_id: int, type_review: str) -> tuple[bool, str]:
        review_exist = self.read(avaliacao_id=avaliacao_id, type_review=type_review)
        if not review_exist:
            msg = "Avaliação não encontrada."
            return False, msg
        
        delete_review_query = f"DELETE FROM Avaliacao_{type_review} WHERE Avaliacao_id = %s"
        try:
            self.cursor.execute(delete_review_query, (avaliacao_id))
            self.conn.commit()
            
            review_exist = self.read(avaliacao_id=avaliacao_id, type_review=type)

            if not review_exist:
                msg = "Avaliação excluída."
                return True, msg
            
            msg = "Não foi possível realizar a operação."
            return False, msg

        except Exception as err:
            print(err)
            return False, str(err)