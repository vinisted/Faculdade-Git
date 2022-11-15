#6.	Faça um programa que leia 10 números e informe a soma e a média dos números.

num = int(input('digite um numero: '))
valor = num

for i in range (10):
    num = int(input('digite um numero: '))
    valor = valor + num
media = valor/(i+1) #media = valor/10
print('soma =',valor)
print('media =',media)
