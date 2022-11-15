#9.	Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#  O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
num = int(input('digite o numero que deseja calcular: '))
valor = 0

for i in range (11):
    valor = num * i #valor = num * (i + 1)
    print(num,'x',i,'=',valor)
