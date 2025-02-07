# Importa bibliotecas necessárias
from flask import Blueprint, request, jsonify
from app.factory import database
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_cors import cross_origin
from .auth import block_token

# Utilização de blueprints para encapsular as funcionalidades e viabilizar a modularização
auth_bp = Blueprint('auth', __name__)

# Cadastro do usuário
@auth_bp.route('/signup', methods=['POST'])
@cross_origin()
def signup():
    # Recebe dados do formulário enviado
    data = request.json

    # Verifica se foi enviado uma imagem de perfil e se sim, lê a imagem
    profile_img = request.files.get('foto_perfil')    
    profile_img_data = None
    if profile_img:
        profile_img_data = profile_img.read() 

    try:
        data = dict(data)

        # Retira os espaços em branco no início e no final dos valores
        for key, value in data.items():
            try:
                data[key] = value.strip()
            
            # Tratamento de erros para valores booleanos
            except AttributeError:
                continue
        # Insere dados cadastrados no banco de dados
        success, msg = database.auth.create(
            data['email'],
            data['password'],
            data['nome'],
            data['administrador'],
            data['feirante'],
            data['identificador'],
            profile_img_data  
        )    

    # Tratamento de erro para ausência de um dos campos
    except KeyError:
        success = False
        msg = "Campos incompletos."

    # Resposta da requisição
    return jsonify({"success":success, "msg":msg}), (201 if success else 400)


# Login do usuário
@auth_bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    # Recebe dados a serem verificados em JSON
    data = request.json
    try:
        # Verifica a autenticação no bando de dados
        # e retorna o token de acesso caso o login seja bem sucedido
        success, jwt_token = database.auth.autenticacao(data['email'], data['password'])

    # Tratamento de erro para ausência de um dos campos
    except KeyError:
        success = False
        jwt_token = "Campos incompletos."
        
    # Resposta da requisição
    if success:
        return jsonify(access_token=jwt_token), 200
    
    return jsonify(msg=jwt_token), 401

# Logout do usuário
@auth_bp.route('/logout', methods=['POST'])
@cross_origin()
@jwt_required()
def logout():
    # Busca informações (claims) do usuário por meio de um objeto payload 
    # Neste caso, busca o identificador do token (jti) e adiciona a lista dos tokens inválidos (block_token) 
    try:
        jti = get_jwt()["jti"]
        block_token(jti)
    except KeyError:
        pass

    # Resposta da requisição
    return "", 204


# Lê todos os usuários
@auth_bp.route('/all-users', methods=['GET'])
@jwt_required()
@cross_origin()
def read_all_users():
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
    
    # Verifica se o usuário ter permissão de administrador
    if role == "admin":
        # Lê todos os usuários no banco de dados
        all_users = database.auth.read_all()

        # Resposta da requisição
        return jsonify(data=all_users) if all_users else ('',404)

    # Resposta da requisição
    return jsonify(msg="Usuário não tem permissão para realizar essa operação."), 403

# Lê um usuário específico
@auth_bp.route('/details/<user_info>', methods=['GET'])
@jwt_required()
@cross_origin()
def user_details(user_info):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()

    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    # Lê usuário no banco de dados com base no identificador
    id_to_read = int(user_info)
    user_data = database.auth.read(user_id=id_to_read)
    
    # Resposta da requisição
    return jsonify(data=user_data) if user_data else ('', 404)


# Atualiza informações do usuário
@auth_bp.route('/update/<id_to_update>', methods=['PUT'])
@jwt_required()
@cross_origin()
def update_user(id_to_update):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()
    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    # Para dados de texto (como nome, email, etc.)
    data = request.form

    # Para arquivos, como a imagem de perfil
    files = request.files

    new_name = data.get('new_name', None)
    new_last_name = data.get('new_last_name', None)
    new_password = data.get('new_password', None)
    new_gender = data.get('new_gender', None)
    new_role = data.get('new_role', None)
    new_email = data.get('new_email', None)

    # Verifica se a imagem foi enviada nos arquivos
    profile_img = files.get('new_profile_img', None)
    profile_img_data = None
    if profile_img:
        profile_img_data = profile_img.read()  # Lê os dados da imagem
    
    # Atualiza usuário no banco de dados
    success, msg = database.auth.update(id_to_update, new_name, new_last_name, new_password,
                                         profile_img_data, new_gender, new_role, new_email)
    
    # Resposta da requisição
    return jsonify({'success': success, "msg": msg}), (200 if success else 400)


# Exclui usuário
@auth_bp.route('/delete/<id_to_delete>', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete_user(id_to_delete):
    # Busca identificador do usuário no token JWT
    user_id = get_jwt_identity()

    # Usuário não está logado
    if not user_id:
        return jsonify(msg="Operação não autorizada."), 401
    
    success = False
    # Exclui usuário do banco de dados
    if id_to_delete:
        success, msg = database.auth.delete(id_to_delete)
    else:
        msg = "Usuario ID não fornecido."

    # Resposta da requisição
    return jsonify({"success": success, "msg": msg}), (200 if success else 400)