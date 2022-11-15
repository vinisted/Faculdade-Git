lit = float(input("Digite a quantidade de litros comprados: "))
tipo = input("A-alcool, G-gasolina: ")

if tipo == "A":
	preço = 1.9
	if lit <= 20:
		des = 3
	elif lit > 20:
		des = 5
elif tipo == "G":
	preço = 2.5
	if lit <= 20:
		des = 4
	elif lit > 20:
		des = 6

total = lit * preço - (lit * preço * des / 100)

print("O valor a ser pago para {} litros de {} é: R$ {}".format(lit, tipo, total))