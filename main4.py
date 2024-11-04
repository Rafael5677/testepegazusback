lista = ["   joao   ","   maria   ","  joana  "]


lista_espaco = [nomes.strip() for nomes in lista] #usamos o comando strip para cortar os espaços das strings.
print(lista_espaco) #imprimimos a lista já cortada
