

materias = ["historia", "fisica", "calculo", "poesias"]
notas = [98, 97, 85, 77]

boletim = [["historia", 98], ["fisca", 88], ["calulo", 77], ["poesias", 85]]
#print(boletim)

ciencia_comp = ['ciencias comp', 100]
boletim.append(ciencia_comp)
#print(boletim)

artes_visual = ['artes visuais', 93]
boletim.append(artes_visual)
#print(boletim)

mod_nota = boletim[-1][1] + 5 #soft code 
print(mod_nota)
#mod_nota = 98 #hard code 
print(mod_nota)
boletim[-1][1] = mod_nota
print(boletim)

'''

Exercicio que treinei habilidade de acessar index em listas bidimensional, 
como alterar o dado do de um index e como usar o metodo append.

'''

