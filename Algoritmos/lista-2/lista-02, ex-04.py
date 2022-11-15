n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))

# para o menor valor:

if n1 < n2 and n1 < n3 :
    menor = n1
if n2 < n1 and n2 < n3 :
    menor = n2
if n3 < n1 and n3 < n2 :
    menor = n3

print('o menor valor digitado foi:', menor)

# para o maior valor:

if n1 > n2 and n1 > n3 :
    maior = n1
if n2 > n1 and n2 > n3 :
    maior = n2
if n3 > n1 and n3 > n2 :
    maior = n3

print('o maior valor digitado foi:', maior)

