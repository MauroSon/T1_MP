# Importa bibliotecas necessárias
from flask import Blueprint, request, jsonify
from app.factory import database
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_cors import cross_origin

# Utilização de blueprints para encapsular as funcionalidades e viabilizar a modularização
loja_bp = Blueprint('loja', __name__)

# Cadastro do usuário
@loja_bp.route('/create', methods=['POST'])
@jwt_required()
@cross_origin()
def criar_loja():
    # Recebe dados do formulário enviado
    data = request.json

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
            data['feirante_id'],
            data['localizacao'],
            data['nome'],
            data['categoria'],
            data['descricao']
        )    

    # Tratamento de erro para ausência de um dos campos
    except KeyError:
        success = False
        msg = "Campos incompletos."

    # Resposta da requisição
    return jsonify({"success":success, "msg":msg}), (201 if success else 400)


# Lê todas as lojas
@loja_bp.route('/all', methods=['GET'])
@jwt_required()
@cross_origin()
def ler_lojas():
    # Busca identificador e informações do usuário no token JWT
    user_id = get_jwt_identity()
    claims = get_jwt()
    try:
        role = claims["role"]
    except KeyError:
        return jsonify(msg="Informações do token faltando."), 401 

    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    # Lê todos as lojas no banco de dados
    lojas_data = database.loja.read_all()

    # Resposta da requisição
    return jsonify(data=lojas_data) if lojas_data else ('',404)


# Lê uma loja específica
@loja_bp.route('/details/<loja_id>', methods=['GET'])
@jwt_required()
@cross_origin()
def loja_details(loja_id: int):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()

    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    # Lê loja no banco de dados
    loja_data = database.loja.read(user_id=loja_id)
    
    # Resposta da requisição
    return jsonify(data=loja_data) if loja_data else ('', 404)


# Atualiza informações da loja
@loja_bp.route('/update/<loja_id>', methods=['PUT'])
@jwt_required()
@cross_origin()
def atualiza_loja(loja_id: int):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()
    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    data = request.form

    new_nome = data.get('new_nome', None)
    new_localizacao = data.get('new_localizacao', None)
    new_categoria = data.get('new_categoria', None)
    new_descricao = data.get('new_descricao', None)

    # Atualiza loja no banco de dados
    success, msg = database.loja.update(loja_id, new_nome, new_localizacao, new_categoria, new_descricao)
    
    # Resposta da requisição
    return jsonify({'success': success, "msg": msg}), (200 if success else 400)


# Exclui loja
@loja_bp.route('/delete/<loja_id>', methods=['DELETE'])
@jwt_required()
@cross_origin()
def exclui_loja(loja_id: int):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()

    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    # Exclui loja do banco de dados
    success, msg = database.loja.delete(loja_id)

    # Resposta da requisição
    return jsonify({"success": success, "msg": msg}), (200 if success else 400)
