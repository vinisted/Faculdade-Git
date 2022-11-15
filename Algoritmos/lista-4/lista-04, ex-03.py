qtd = int(input('digite a quantidade de caracteres: '))
crt = input('digite qual caractere deseja usar: ')
for i in range(qtd):
    for j in range(qtd):
        print (crt, end = '')
    print ()