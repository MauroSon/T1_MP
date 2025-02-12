# Importa helpers necessários
from database.base_helper import BaseHelper
from auth.helper import AuthHelper
from loja.helper import LojaHelper
import base64
import googlemaps

# Helper para fazer a interação com o banco de dados 
class ProdutoHelper(BaseHelper):
    # Método que irá inserir um novo produto no banco de dados
    def create(self, loja_id: int, nome_produto: str, categoria_produto: str,
                preco: float, descricao_produto: str, foto_produto: bytes = None) -> tuple[bool, str]:

        # Verifica se loja esta cadastrada no banco de dados
        loja_existe = LojaHelper.read(loja_id=loja_id)
        if not loja_existe:
            msg = "Loja não encontrada."
            return False, msg
        
        try:
            # Verifica a existência das informações obrigatórias
            if nome_produto and categoria_produto and preco and descricao_produto:
                # Comando SQL para inserir informações no banco de dados
                insert_produto_query = "INSERT INTO Produto (Nome, Categoria) VALUES (%s, %s)"
                try:
                    # Executa o comando SQL
                    self.cursor.execute(insert_produto_query, (nome_produto, categoria_produto, ))
                    self.conn.commit()
                    
                    # Pega ID do ultimo produto cadastrado
                    id_produto = self.cursor.lastrowid
                    if not id_produto:
                        msg = "Falha no cadastro do produto."
                        return False, msg

                    # Comando SQL para inserir produto na tabela intermediaria Loja_produto
                    insert_loja_produto_query = """
                                                INSERT INTO Loja_produto (Loja_id, Produto_id, Preco, Descricao_produto, Foto_produto)
                                                VALUES (%s, %s, %s, %s, %s)
                                                """
                    try:
                        self.cursor.execute(insert_loja_produto_query, (loja_id, id_produto, preco, descricao_produto, foto_produto, ))
                        self.conn.commit()
                        msg = "Produto cadastrado com sucesso."
                        return True, msg
                    
                    except Exception as err:
                        self.conn.rollback()
                        return False, str(err)

                except Exception as err:
                    self.conn.rollback()
                    return False, str(err)

            else:
                msg = "Campos incompletos."
                return False, msg
            
        except Exception as err:
            return False, str(err)

    # Método que irá ler um produto no banco de dados com base na coluna Produto_id
    def read(self, produto_id: int) -> list | None:
        # Verifica a existência do ID
        if produto_id:
            # Comando SQL para ler produto da tabela "Produto" com base na coluna "Produto_id"
            select_produto_query = """
                                        SELECT
                                            p.Produto_id, p.Nome, p.Categoria, lp.Preco, lp.Descricao_produto, 
                                            lp.Foto_produto, l.Localizacao, l.Nome, l.Loja_id
                                        FROM Produto p
                                        JOIN Loja_produto lp ON p.Produto_id = lp.Produto_id
                                        WHERE p.Produto_id = %s
                                   """
            try:
                self.cursor.execute(select_produto_query, (produto_id,))
                produto_data = self.cursor.fetchone()
                
                return list(produto_data) if produto_data else None 
            
            except Exception as err:
                return None, str(err)
        
        else:
            msg = "Informações não fornecidas."
            return None, msg

    # Método que lê todos os produtos do banco de dados
    def read_all(self) -> list[dict] | None:
        # Comando SQL para ler todos os produtos cadastrados
        select_all_produtos_query = """        
                                        SELECT
                                            p.Produto_id, p.Nome, p.Categoria, lp.Preco, lp.Descricao_produto, 
                                            lp.Foto_produto, l.Localizacao, l.Nome, l.Loja_id
                                        FROM Produto p
                                        JOIN Loja_produto lp ON p.Produto_id = lp.Produto_id
                                        JOIN Loja l ON lp.Loja_id = l.Loja_id
                                    """
        try:
            self.cursor.execute(select_all_produtos_query)
            produtos_data = list(self.cursor.fetchall())
            produtos_data = [list(produto) for produto in produtos_data]

            # Ordena os produtos por nome
            produtos_data.sort(key=lambda x: x[1])

            # Formata dados retornados
            for produto in produtos_data:
                if produto[5]:
                    produto[5] = base64.b64encode(produto[5]).decode('utf-8')

            # Mapeia os valores retornados
            for ind in range(len(produtos_data)):
                produtos_data[ind] = {
                    "produto_id": produtos_data[ind][0],
                    "nome_produto": produtos_data[ind][1],
                    "categoria_produto": produtos_data[ind][2],
                    "preco": produtos_data[ind][3],
                    "descricao_produto": produtos_data[ind][4],
                    "localizacao": produtos_data[ind][6],
                    "nome_loja": produtos_data[ind][7],
                    "loja_id": produtos_data[ind][8]
                }
            return produtos_data
        
        except Exception as err:
            print(err)
            return None
         
    def read_by_name(self, nome_produto: str) -> list[dict] | None:
        if nome_produto:
            select_produtos_query = """
                                        SELECT
                                            p.Produto_id, p.Nome, p.Categoria, lp.Preco, lp.Descricao_produto, 
                                            lp.Foto_produto, l.Localizacao, l.Nome, l.Loja_id
                                        FROM Produto p
                                        JOIN Loja_produto lp ON p.Produto_id = lp.Produto_id
                                        JOIN Loja l ON lp.Loja_id = l.Loja_id
                                        WHERE p.Nome = %s
                                    """
            try:
                self.cursor.execute(select_produtos_query, (nome_produto, ))
                produtos_data = list(self.cursor.fetchall())
                produtos_data = [list(produto) for produto in produtos_data]

                # Ordena os produtos por nome
                produtos_data.sort(key=lambda x: x[1])

                # Formata dados retornados
                for produto in produtos_data:
                    if produto[5]:
                        produto[5] = base64.b64encode(produto[5]).decode('utf-8')
                
                # Mapeia os valores retornados
                for ind in range(len(produtos_data)):
                    produtos_data[ind] = {
                        "produto_id": produtos_data[ind][0],
                        "nome_produto": produtos_data[ind][1],
                        "categoria_produto": produtos_data[ind][2],
                        "preco": produtos_data[ind][3],
                        "descricao_produto": produtos_data[ind][4],
                        "localizacao": produtos_data[ind][6],
                        "nome_loja": produtos_data[ind][7],
                        "loja_id": produtos_data[ind][8]
                    }
                
                return produtos_data

            except Exception as err:
                print(err)
                return None
            
    def ordena_produtos_distancia(self, cep_usuario: str) -> list[dict] | None:
        # Configuracoes para utilizar a API do google maps
        API_KEY = "AIzaSyBJ-XAw7TnCqlP0Avo5iRroVDX57b0uDJI"
        gmaps = googlemaps.Client(key=API_KEY)

        # Formata CEP do usuario
        cep_usuario = cep_produto[:5] + "-" + cep_produto[5:]

        # Pega todos os produtos cadastrados no banco de dados
        produtos_data = self.read_all()
        for produto in produtos_data:
            # Formata CEP da localizacao do produto
            cep_produto = produto["localizacao"][:5] + "-" + produto["localizacao"][5:]

            # Cria os parametros para consumir a API
            origem = f"{cep_usuario}, Brasil"
            destino = f"{cep_produto}, Brasil"

            # API para consultar a distancia entre os dois CEPs
            resultado = gmaps.distance_matrix(origem, destino, mode="driving")

            if resultado['status'] == 'OK':
                # Pega distancia e adiciona no produtos_data
                distancia = resultado['rows'][0]['elements'][0]['distance']['text']
                produto["distancia"] = float(distancia[:-3])

            else:
                print(resultado["status"])
                return None

        # Ordena produtos baseado na distancia
        produtos_ordenados = sorted(produtos_data, key=lambda x: x["distancia"])

        return produtos_ordenados
    
    def ordena_produtos_preco(self) -> list[dict] | None:
        # Pega todos os produtos cadastrados no banco de dados
        produtos_data = self.read_all()

        # Ordena produtos baseado no preco
        produtos_ordenados = sorted(produtos_data, key=lambda x: x["preco"])

        return produtos_ordenados
    
    
    # Método que atualiza informações de um produto no banco de dados
    def update(self, produto_id: int, new_nome_produto: str = None, new_categoria: str = None, 
               new_descricao: str = None, new_preco: float = None, new_foto_produto: bytes = None) -> tuple[bool, str]:
        updated = False
        fields_to_update = []
        args = []
        if new_nome_produto:
            fields_to_update.append("Nome = %s")
            args.append(new_nome_produto)

        if new_categoria:
            fields_to_update.append("Categoria = %s")
            args.append(new_categoria)

        if len(fields_to_update):
            try:
                # Comando SQL para atualizar informações do produto na tabela "Produto"
                update_produto_query = "UPDATE Produto SET " + ", ".join(fields_to_update) + "WHERE Produto_id = %s"
                args.append(produto_id)
                self.cursor.execute(update_produto_query, (args))
                self.conn.commit()
                updated = True
            
            except Exception as err:
                self.conn.rollback()
                return False, str(err)
        
        fields_to_update = []
        args = []
        if new_preco:
            fields_to_update.append("Preco = %s")
            args.append(new_preco)

        if new_descricao:
            fields_to_update.append("Descricao_produto = %s")
            args.append(new_descricao)
        
        if new_foto_produto:
            fields_to_update.append("Foto_produto = %s")
            args.append(new_foto_produto)
        
        if len(fields_to_update):
            # Comando SQL para atualizar informações do produto na tabela "Loja_produto"
            update_loja_query = "UPDATE Loja_produto SET " + ", ".join(fields_to_update) + "WHERE Produto_id = %s"
            args.append(produto_id)
            
            try:
                self.cursor.execute(update_loja_query, (args))
                self.conn.commit()
                msg = "Produto atualizado com sucesso."
                return True, msg
            
            except Exception as err:
                self.conn.rollback()
                return False, str(err)
        else:
            if not updated:
                msg = "Informações não fornecidas."
                return False, msg
            msg = "Produto atualizado com sucesso."
            return True, msg
        
    # Método para excluir produto no banco de dados
    def delete(self, produto_id: int) -> tuple[bool, str]:
        # Comando SQL para excluir produto da tabela "Produto"
        delete_produto_query = "DELETE FROM Produto WHERE Produto_id = %s"

        produto_existe = self.read(produto_id=produto_id)
        # Verifica se o produto existe no banco de dados
        if produto_existe:
            try:
                self.cursor.execute(delete_produto_query, (produto_id, ))
                self.conn.commit()
                msg = "Produto excluído."
                return True, msg
            
            except Exception as err:
                self.conn.rollback()
                return False, str(err)
        else:
            msg = "Produto inexistente."
            return False, msg
