qcds = int(input("Digite a quantidade de CD's : "))
cds = []
ncd = 1

for i in range(qcds):
    print('CD número ', ncd)
    valor_cd = cds.append(float(input('Digite o valor do CD: ')))
    ncd += 1

media = sum(cds) / len(cds)
print('A media para cada CD é: ', media)