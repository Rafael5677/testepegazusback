responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}


for lista in responsejson["produtos"]: #criamos um loop
        if lista["nome"] == "Produto B": #criamos um condição com base na lista 
            print(lista["nome"]) #imprimimos  a lista filtrada

       
    
  