p1 = float(input('digite o preço do primeiro produto: '))
p2 = float(input('digite o preço do segundo produto: '))
p3 = float(input('digite o preço do terceiro produto: '))

if p1 < p2 and p1 < p3 :
    menor = p1
if p2 < p1 and p2 < p3 :
    menor = p2
if p3 < p1 and p3 < p2 :
    menor = p3

print('o produto mais barato é o que custa:', menor)