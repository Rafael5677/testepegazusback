fila = ["Roberto","Eduardo","Lucas"]


def adicionar_item(fila, add): #criamos uma função para adiconar mais uma string.
    fila.pop(2)  # usamos o .pop() para remover o primeiro número.
    fila.append(add)  #usamos o append para adiconar a string no final da fila


add = "Fred"


adicionar_item(fila, add)


print(fila)# imprimimos nossa fila