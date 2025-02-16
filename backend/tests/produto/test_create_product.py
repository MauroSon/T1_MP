
def test_create_produto(client, auth_token):
    product_data = {
        "nome_produto": "PC Gamer",
        "categoria_produto": "Eletrônicos", 
        "loja_id": 1, 
        "preco": "3000.00", 
        "descricao_produto": "Um computador gamer de alta performance.", 
        "foto_produto": None
    }
    headers = {"Authorization": f"Bearer {auth_token}"}
        
    response = client.post("/produto/create", headers=headers, json=product_data)

    print(response.json)
    assert response.status_code == 201
    assert response.json["success"] == True
    assert response.json["msg"] == "Produto cadastrado com sucesso."
            

def test_create_another_produto(client, auth_token):
    product_data = {
        "nome_produto": "Bone",
        "categoria_produto": "Moda", 
        "loja_id": 1, 
        "preco": "150.00", 
        "descricao_produto": "Um boné de alta qualidade.", 
        "foto_produto": "https://static.prospin.com.br/media/catalog/product/cache/0e3f1fa1e1f5782c73be0e8cb4ab3f9d/n/e/nev23bon110-bone-new-era-9forty-a-frame-snapback-nyc-new-york-city-verde.jpg"    
    }
    headers = {"Authorization": f"Bearer {auth_token}"}
        
    response = client.post("/produto/create", headers=headers, json=product_data)

    print(response.json)
    assert response.status_code == 201
    assert response.json["success"] == True
    assert response.json["msg"] == "Produto cadastrado com sucesso."
            