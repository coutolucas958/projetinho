

#texto = 'Python'
#
#i = 0 
#tamanho_string = len(texto)
#
#while i < tamanho_string:
#    print(texto[i], i)
#
#    i += 1 

#texto = 'Python'

#for letra in texto:
#    print(letra)

#numeros = range(0, 11, 2)

#for numero in numeros:
  #  print(numero)


for i in range(10):   #linha
    if i == 2:
        print('i é 2, pulando...')
        continue
    
    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):   #coluna, o numero 3 não aparece, começa no 1
        print(i, j)         # e termina no 2. 
else:
    print('For completo com sucesso')