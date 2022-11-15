nota = int(input('digite um numero entre zero e dez: '))

while nota < 0 or nota > 10 :
    nota = int(input('digite um valor entre 0 e 10: '))
print('a nota digitada foi {}'.format(nota))
    