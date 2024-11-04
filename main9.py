import requests #importamos a biblioteca request para que os comandos request funcionem

#Não consegui finalizar

def requisicao():
    
    url = "https://jsonplaceholder.typicode.com/users" #criamos um solicitação para esse url.
    
    
    

    response = requests.get(url)
    
       
    usuarios = response.json() #criamos um conversor de json
    
    

    dados_extraidos = []
    
    
    for usuario in usuarios:
        
            
        dados_usuario = {
      
            "nome": usuario["nome"],

            "username": usuario["username"],
            
       
            "email": usuario["email"],
            "endereco": usuario["rua"]["numero"],
            
        }
        dados_extraidos.append(dados_usuario)
    
    
        
        

    return dados_extraidos #usamos o return para retornar os dados soliticados


resultado = requisicao() #chamamos noss função.

resultado = requisicao 
print(resultado) # imprimos nossa função.