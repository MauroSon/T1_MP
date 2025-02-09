import pytest

# Objetivo do test_create_store: cadastrar uma loja que ainda não existe no banco de dados
def test_create_store(client, auth_token):
    # Cadastro um usuário feirante antes
    user_data = {
        "email": "feirante@email.com",
        "password": "senha", 
        "nome": "Feirante", 
        "administrador": False, 
        "feirante": True, 
        "identificador": "09876543210" # Identificador: CPF/CPNJ (a depender do tipo de usuario) 
    }

    # Cria uma requisicao para cadastrar um usuario feirante
    create_user = client.post("/auth/signup", json=user_data)

    if create_user.status_code == 201 and create_user.json["success"] == True:
    # Dados da loja a serem enviados
        json_data = {

            "feirante_id": 2,  # ID do usuário dono da loja
            "localizacao": "71025100", # CEP da Feira Guará 
            "nome": "Loja Exemplo",
            "categoria": "Roupas",
            "descricao": "Uma loja especializada em roupas de alta qualidade."
        }

        headers = {"Authorization": f"Bearer {auth_token}"}
        
        # Faz uma requisição POST para cadastrar a loja
        response = client.post("/loja/create", headers=headers, json=json_data)

        print(response.json)
        # Verifica se a loja foi cadastrada com sucesso
        assert response.status_code == 201
        assert response.json["success"] == True
        assert response.json["msg"] == "Loja criada com sucesso!"
    # else:
        with pytest.raises(Exception) as e_info:
            print(e_info)
            
# Objetivo do test_create_store_exists: tentar cadastrar uma loja com o mesmo nome e falhar
def test_create_store_exists(client, auth_token):
    # Dados da loja já cadastrada
    json_data = {
        "feirante_id": 2,  # Mesmo usuário
        "localizacao": "71025100",
        "nome": "Loja Exemplo",  # Nome repetido
        "categoria": "Roupas",
        "descricao": "Uma loja especializada em roupas de alta qualidade."
    }
    
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Faz uma requisição POST para cadastrar a loja
    response = client.post("/loja/create", headers=headers, json=json_data)

    # Verifica se o sistema detecta que a loja já existe
    assert response.status_code == 400
    assert response.json["success"] == False
    assert response.json["msg"] == "Já existe uma loja com esse nome."

# Objetivo do test_create_store_no_user: tentar cadastrar uma loja sem um usuario associado
def test_create_store_no_user(client, auth_token):
    # Dados da loja a ser cadastrada
    json_data = {
        "feirante_id": 1000000,  # Usuario inexistente
        "localizacao": "71025100",
        "nome": "Outra loja",
        "categoria": "Esporte",
        "descricao": "Uma loja especializada artigos de esporte."
    }

    headers = {"Authorization": f"Bearer {auth_token}"}

    # Faz uma requisição POST para cadastrar a loja
    response = client.post("/loja/create", headers=headers, json=json_data)

    # Verifica se o sistema detecta que ao usuario nao existe
    assert response.status_code == 400
    assert response.json["success"] == False
    assert response.json["msg"] == "Loja sem usuário associado."
