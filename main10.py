fila = ["livro", "caderno", "caneta"]


def adicionar_item(fila, add): #criamos uma função para adiconar mais uma string.
    fila.pop(0)  # usamos o .pop() para remover o primeiro número.
    fila.append(add)  #usamos o append para adiconar a string no final da fila


add= "lapiz"


adicionar_item(fila, add)


print(fila)#imprimimos nossa fila