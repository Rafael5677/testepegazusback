lista = [0,1,2,3,4,5,6,7,8,9,10,11]
x=lista[0]
lista2=[]
while x in lista:# usamos o while para criar um loop para criar a condição.

    if x<=5:

        lista2.append(x)# usamos para adicionar o número no final da lista

    x=x+1

for i in lista2: #usamo o for para criar o loop para criar um comdando interativo.

    lista2[i]=lista2[i]+1

print(lista2)

#Utilizei while e for por serem estruturas de loop que nos ajudam muito a filtrar e diminuir o tempo que levariamos com outras funções no python.

