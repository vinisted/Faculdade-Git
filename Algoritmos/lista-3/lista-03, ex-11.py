pares = 0
impares = 0

for i in range (10):
    num = int(input('digite um numero inteiro: '))
    if num % 2 == 0 :
        pares = pares + 1

    else:
        impares = impares + 1
        
print('pares', pares, ',impares', impares)