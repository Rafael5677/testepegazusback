lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

for lista_remo in lista: #criar um loop para remover o nome joão da lista.
    lista.remove("joao")

lista.insert(0,"maria")# depois adicionamos o nome de maria na lista colocando as posições desejadas.
lista.insert(3,"maria")
lista.insert(5,"maria")

print(lista)# imprimos a lista com os nomes removidos