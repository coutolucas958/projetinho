


lista_1 = ["Lucas","Victor","Gabriel","Guilherme"]
lista_1.insert(3, "Couto")
print(lista_1)

lista_1.pop() #por padrão sempre vai remover o ultimo index da lista.
print(lista_1)

vic = lista_1.pop(1) # pega o valor do index que escolheu e salva na variavel.
print(vic) # index salo na variavel
print(lista_1) # lista sem o index que você tirou da variavel.

#metodo range, cria uma lista do zero, 
# até um numero antes do que você atribuiu
lista_2 = range(13)
#ele retorna um objeto do type=range e o list converte para uma lista.
print(list(lista_2)) 


lista_5 = list(range(2, 14, 4))
# lembrar que incremento não vai até o ultimo numero do range. 
print(lista_5)


len(lista_1)
###len(precisa de um parametro para ter o que retornar) sorted()

