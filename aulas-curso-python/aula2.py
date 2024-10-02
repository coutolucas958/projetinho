"""
Faça uma lista de compras com listas 
O usuário deve ter a possibilidade de 
inserir, apagar e listar valires da sua lista. 

Não permita que o programa quebre com erros de
indices inexistesntes na lista. 
"""
import os

lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        os.system('clear')
        indice_srt = input('Qual indice quer apagar: ')

        try:
            indice = int(indice_srt)
            del lista[indice]
        except ValueError:
            print('Digite um numero int.')
        except IndexError:
            print('Indice não existe na lista')
        except Exception: 
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('clear')
        
        if len(lista) == 0:
            print('Lista vazia :(')
        
        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Por favor escolha uma das opções validas.')