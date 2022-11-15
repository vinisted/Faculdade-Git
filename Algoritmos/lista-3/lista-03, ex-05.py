#5.	Faça um programa que leia 10 números e informe o maior número.

num = float(input('digite um numero: '))
maior = num
for i in range(9):
    num = int(input('digite um numero: '))
    if num > maior:
        maior = num
print('maior', maior)

