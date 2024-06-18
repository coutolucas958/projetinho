"""
- fazer a pergunta 
- opções de respostas 
- dar as respostas de forma aletória

"""
import random

while True:

    nome = input('Com quem estou falando? ')
    pergunta = input(f'Digite uma pergunta {nome}: ')
    
    if pergunta.strip() == "" or " ":
            print('Você não digou uma pergunta.')
            continue
    
    lista_resposta = [
        "Sim, claro",
        "Não, nem pensar",
        "Talvez",
        "Pode ser que sim"
    ]

    resposta_final = random.choice(lista_resposta)
    print(resposta_final)
    
    sair = input('Quer sair? [S]im: ').lower().startswith('S')

    if sair is True:
        break

"""

Desafios para esse projeto: 

- O robo falar o nome da pessoa na resposta.: Nome - Resposta
- Tentar e aprender a usar listas ao inves de variáveis
- Ao aprender usar as listas, usar random.choice (pesquisar)
- edge case - caso uma pessoa não digite nada. 

"""