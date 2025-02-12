# Importa bibliotecas necessárias
from flask import Blueprint, request, jsonify
from app.factory import database
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_cors import cross_origin

# Utilização de blueprints para encapsular as funcionalidades e viabilizar a modularização
produto_bp = Blueprint('produto', __name__)

# Cria um novo produto
@produto_bp.route('/create', methods=['POST'])
@jwt_required()
@cross_origin()
def criar_produto():
    # Recebe dados do formulário enviado
    data = request.json

    # Verifica se foi enviado uma imagem do produto e se sim, lê a imagem
    foto_produto = request.files.get('foto_produto')    
    foto_produto_data = None
    if foto_produto:
        foto_produto_data = foto_produto.read() 

    try:
        data = dict(data)

        # Retira os espaços em branco no início e no final dos valores
        for key, value in data.items():
            try:
                data[key] = value.strip()
            except AttributeError:
                continue

        # Insere dados cadastrados no banco de dados
        success, msg = database.loja.create(
            data['nome_produto'],
            data['categoria_produto'],
            data['loja_id'],
            data['preco'],
            data['descricao_produto'],
            foto_produto_data
        )

    # Tratamento de erro para ausência de um dos campos
    except KeyError:
        success = False
        msg = "Campos incompletos."

    # Resposta da requisição
    return jsonify({"success":success, "msg":msg}), (201 if success else 400)


# Lê todos os produtos
@produto_bp.route('/all/', defaults={'parametro': None}, methods=['GET'])
@produto_bp.route('/all/<parametro>', methods=['GET'])
@jwt_required()
@cross_origin()
def ler_produtos(parametro):
    # Busca identificador e informações do usuário no token JWT
    user_id = get_jwt_identity()
    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    if parametro == "preco":
        produtos_data = database.produto.ordena_produtos_preco()
    elif parametro == "distancia":
        produtos_data = database.produto.ordena_produtos_distancia()
    else:
        produtos_data = database.produto.read_all()

    # Resposta da requisição
    return jsonify(data=produtos_data) if produtos_data else ('',404)


# Lê uma loja específica
@produto_bp.route('/details/<produto_id>', methods=['GET'])
@jwt_required()
@cross_origin()
def loja_details(produto_id: int):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()

    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    # Lê produto no banco de dados
    produto_data = database.produto.read(produto_id=produto_id)
    
    # Resposta da requisição
    return jsonify(data=produto_data) if produto_data else ('', 404)


# Atualiza informações do produto
@produto_bp.route('/update/<produto_id>', methods=['PUT'])
@jwt_required()
@cross_origin()
def atualiza_loja(produto_id: int):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()
    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    data = request.form

    # Verifica se foi enviado uma imagem do produto e se sim, lê a imagem
    new_foto_produto = request.files.get('foto_produto', None)    
    new_foto_produto_data = None
    if new_foto_produto:
        new_foto_produto_data = new_foto_produto.read() 

    new_nome_produto = data.get('new_nome_produto', None)
    new_categoria_produto = data.get('new_categoria_produto', None)
    new_descricao_produto = data.get('new_descricao_produto', None)
    new_preco = data.get('new_preco', None)
    produto_id = data.get('produto_id', None)

    # Atualiza produto no banco de dados
    success, msg = database.produto.update(produto_id, new_nome_produto, new_categoria_produto, new_descricao_produto, new_preco, new_foto_produto_data)
    
    # Resposta da requisição
    return jsonify({'success': success, "msg": msg}), (200 if success else 400)


# Exclui produto
@produto_bp.route('/delete/<produto_id>', methods=['DELETE'])
@jwt_required()
@cross_origin()
def exclui_loja(produto_id: int):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()

    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    # Exclui produto do banco de dados
    success, msg = database.produto.delete(produto_id)

    # Resposta da requisição
    return jsonify({"success": success, "msg": msg}), (200 if success else 400)
