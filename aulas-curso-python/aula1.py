

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# Desacoplando os indices da lista
# e inumerando eles. 

for indice, nome in enumerate(lista):
    print(indice, nome)