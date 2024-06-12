"""
- fazer a pergunta 
- opções de respostas 
- dar as respostas de forma aletória

"""
import random

pergunta = input('Digite uma pergunta: ')

resposta1 = 'Sim, claro'
resposta2 = 'Não, nem pensar'
resposta3 = 'Talvez'
resposta4 = 'Por ser que sim'

resposta_final = random.randint(1, 4)
if resposta_final == 1:
    print(resposta1)
elif resposta_final == 2:
    print(resposta2)
elif resposta_final == 3:
    print(resposta3)
else:
    print(resposta4)


"""

Desafios para esse projeto: 

- O robo falar o nome da pessoa na resposta.: Nome - Resposta
- Tentar e aprender a usar listas ao inves de variáveis
- Ao aprender usar as listas, usar random.choice (pesquisar)
- edge case - caso uma pessoa não digite nada. 

"""