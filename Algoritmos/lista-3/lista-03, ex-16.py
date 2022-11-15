z=0
x=[]
while z != -1:
    z = int(input('Digite sua idade (para interromper digite -1): '))

    if z != -1:
        x.append(z)

if len(x) != 0:
    media = sum(x)/len(x)

m = round(media,0)

if 0 <= m <= 25:
    print('Populacao jovem')

if 26 <= m <= 60:
    print('Populacao adulta')

if m > 60:
    print('Populacao idosa')