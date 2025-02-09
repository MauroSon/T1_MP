# Objetivo do test_signup_user: cadastrar um usuário que ainda 
# não existe no banco de dados 
def test_signup_user(client):
    # Dados a serem enviados para cadastrar um usuario
    json_data = {
        "email": "fulano@email.com",
        "password": "senha", 
        "nome": "Fulano", 
        "administrador": False, 
        "feirante": False, 
        "identificador": # Identificador: CPF/CPNJ (a depender do tipo de usuario) 
        "01234567890"
    }
    # Cria uma requisição para a rota e atribui a resposta a "response"
    response = client.post("/auth/signup", json=json_data)

    # Verifica se a requisição foi bem sucedida
    # Ou seja, se o usuario foi cadastrado
    assert response.status_code == 201
    assert response.json["success"] == True
    assert response.json["msg"] == "Conta criada com sucesso!"

# Objetivo do test_signup_user_exists: cadastrar um usuário que já 
# foi previamente cadastrado e não conseguir 
def test_signup_user_exists(client):
    # Dados a serem enviados para cadastrar um usuario que já existe
    json_data = {
        "email": "fulano@email.com",
        "password": "senha", 
        "nome": "Fulano", 
        "administrador": False, 
        "feirante": False, 
        "identificador": # Identificador: CPF/CPNJ (a depender do tipo de usuario) 
        "01234567890"
    }
    # Cria uma requisição para a rota e atribui a resposta a "response"
    response = client.post("/auth/signup", json=json_data)

    # Verifica se a requisição falhou
    # Ou seja, se o usuario já está cadastrado
    assert response.status_code == 400
    assert response.json["success"] == False
    assert response.json["msg"] == "Email já registrado."
