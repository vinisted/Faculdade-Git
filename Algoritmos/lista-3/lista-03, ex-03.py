pA = int(input('digite o 1° país: '))
pB = int(input('digite o 2° país: '))
ano = 0

while pA < pB:
	pA += pA * 0.03
	pB += pB * 0.015
	ano += 1

print ( 'A ultrapassa ou iguala a B em {} anos'.format(ano))