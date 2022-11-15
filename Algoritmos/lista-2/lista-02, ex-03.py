nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))

calculo = (nota1 + nota2) / 2
print(calculo)

if calculo > 7:
    print('aprovado')
if calculo < 6:
    print('reprovado')
if calculo < 7 and calculo > 5:
    print('prova final')