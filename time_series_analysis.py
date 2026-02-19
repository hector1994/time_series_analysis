lista = ['Héctor','Alonso','Hormazábal','Vildósola']
print(lista)

for i in range(len(lista)):
    lista_invertida.append(lista[-i-1])
    print(lista[-i-1]) 
print(lista_invertida)