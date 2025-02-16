# Importa bibliotecas necessárias
from flask import Blueprint, request, jsonify
from app.factory import database
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_cors import cross_origin

# Utilização de blueprints para encapsular as funcionalidades e viabilizar a modularização
reviews_bp = Blueprint('reviews', __name__)

# Cria um nova avaliacao
@reviews_bp.route('/create/<type_review>', methods=['POST'])
@cross_origin()
def cria_avaliacao(type_review):
    # Busca identificador e informações do usuário no token JWT
    user_id = get_jwt_identity()
    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    # Recebe dados do formulário enviado
    data = request.json

    try:
        data = dict(data)

        # Retira os espaços em branco no início e no final dos valores
        for key, value in data.items():
            try:
                data[key] = value.strip()
            
            # Tratamento de erros para valores booleanos
            except AttributeError:
                continue
        if type_review == "product":
            # Insere dados cadastrados no banco de dados
            success, msg = database.reviews.create(
                usuario_id=data['usuario_id'],
                nota=data['nota'],
                comentario=data['comentario'],
                produto_id=data['produto_id']
            )    
        elif type_review == "store":
            # Insere dados cadastrados no banco de dados
            success, msg = database.reviews.create(
                usuario_id=data['usuario_id'],
                nota=data['nota'],
                comentario=data['comentario'],
                loja_id=data['loja_id']
            )    
        else:
            msg = f"Ocorreu um erro. Parâmetro recebido: {type_review}"
            success = False
        
    # Tratamento de erro para ausência de um dos campos
    except KeyError:
        success = False
        msg = "Campos incompletos."

    return jsonify({"success":success, "msg":msg}), (201 if success else 400)

# Lê todas as avaliacoes
@reviews_bp.route('/all/<type_review>/<read_id>', methods=['GET'])
@jwt_required()
@cross_origin()
def ler_avaliacoes(type_review: str, read_id: int):
    # Busca identificador e informações do usuário no token JWT
    user_id = get_jwt_identity()
    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    if not read_id:
        return jsonify(msg="ID não fornecido."), 400
    
    if type_review == "product":
        # Lê todos os usuários no banco de dados
        all_reviews = database.reviews.read_all_by_product(produto_id=read_id)
    elif type_review == "store":
        all_reviews = database.reviews.read_all_by_store(loja_id=read_id)
    else:
        print(type_review)
        print(read_id)
        return jsonify(msg="Parâmetros incorretos."), 400
    
    return jsonify(data=all_reviews) if all_reviews else ('',404)

# Atualiza informacoes de uma avaliacao
@reviews_bp.route('/update/<type_review>/<id_to_update>', methods=['PUT'])
@jwt_required()
@cross_origin()
def atualiza_avaliacao(type_review: str, id_to_update: int):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()
    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    data = request.json

    new_nota = data.get('new_nota', None)
    new_comentario = data.get('new_comentario', None)

    # Atualiza usuário no banco de dados
    success, msg = database.reviews.update(avaliacao_id=id_to_update, type_review=type_review,
                                           new_nota=new_nota, new_comentario=new_comentario)
    
    return jsonify({'success': success, "msg": msg}), (200 if success else 400)


# Exclui avaliacao
@reviews_bp.route('/delete/<type_review>/<id_to_delete>', methods=['DELETE'])
@jwt_required()
@cross_origin()
def exclui_avaliacao(type_review: str, id_to_delete: int):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()

    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    success = False
    # Exclui avaliacao do banco de dados
    if id_to_delete:
        success, msg = database.reviews.delete(avaliacao_id=id_to_delete, type_review=type_review)
    else:
        msg = "Avaliacao ID não fornecido."

    return jsonify({"success": success, "msg": msg}), (200 if success else 400)