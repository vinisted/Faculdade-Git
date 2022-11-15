qtdhoras = float(input('digite a quantidade de horas que você trabalha por mês: '))
vhora = float(input('digite quanto você ganha por hora: '))
sbruto = (qtdhoras * vhora)

insento = 0
i1500 = (sbruto * 5) / 100
i2500 = (sbruto * 10) / 100
m2500 = (sbruto * 20) / 100

if (sbruto <= 1500) :
    print('você foi insento de IR', insento)

elif (sbruto > 900 and sbruto <= 1500 and sbruto < 2500) :
    print('você teve 5% de desconto do IR', i1500)

elif (sbruto > 1500 and sbruto <= 2500) :
    print('você teve 10% de desconto do IR', i2500)

else :
    (sbruto > 2500)
    print('você teve 20% de desconto do IR', m2500)