# Objetivo do test_login: fazer o login do usuario ja cadastrado 
def test_login(client):
    # Informacoes de login do usuario ja cadastrado
    json_data={
        "email": "fulano@email.com",
        "password": "senha"
    }

    response = client.post("auth/login", json=json_data)

    assert response.status_code == 200
    token = response.json["access_token"]

    assert token is not None

# Objetivo do test_login_invalid: fazer o login com um usuario com a senha incorreta
def test_login_password_invalid(client):
    # Informacoes de login do usuario ja cadastrado
    # mas com a senha incorreta
    json_data={
        "email": "fulano@email.com",
        "password": "Senha"
    }

    response = client.post("auth/login", json=json_data)

    assert response.status_code == 401
    assert response.json["msg"] == "Credenciais inválidas."

