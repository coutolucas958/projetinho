'''
Criar uma lista 2D dados das vendas, onde vai ter uma lsita e dentro 
das llistas terão os dados de vendas. 
'''


dadosvendas = [[23, 12, 54], [11, 18, 7], [663, 4, 5]]
soma = 0


for dados in dadosvendas:
    for i in dados:
        soma += i
       # print(soma)
print(soma)


