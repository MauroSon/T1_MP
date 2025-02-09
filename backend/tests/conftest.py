import pytest

from app.factory import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    return app


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()

@pytest.fixture(scope="function")
def auth_token(client):
    """Autentica e retorna um token JWT válido para ser usado nos testes."""
    response = client.post("/auth/login", json={"email": "fulano@email.com", "password": "senha"})
    
    assert response.status_code == 200  # Certifique-se de que o login funcionou
    token = response.json.get("access_token")  # Ajuste conforme a resposta do seu backend

    assert token is not None, "Token de autenticação não foi retornado!"
    
    return token  # Retorna o token para ser reutilizado nos testes