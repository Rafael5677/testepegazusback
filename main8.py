import requests #importamos a biblioteca request para que os comandos request funcionem

def tarefas():
    
    resposta = requests.get("https://jsonplaceholder.typicode.com/todos") #criamos um solicitação para esse url.
    
    
    todos = resposta.json() #convertemos o json em python
    
    
    completadas = sum(1 for tarefas in todos if tarefas['completed'])

    pendentes = len(todos) - completadas  
    
    return completadas, pendentes


tarefas_completadas, tarefas_pendentes = tarefas() #chamamos a função

print(f"Tasks completadas: {tarefas_completadas}, Tasks pendentes: {tarefas_pendentes}")


#Utilizei esse metodos para fazer o codigo tem em vista que quando mais conseguirmos simplificar, melhor séra para caso no futuro fazermos alguma modificação, usei metodos e funções que fizeram o código fica menor e mais fácil de entender.