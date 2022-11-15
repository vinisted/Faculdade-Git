produtos = int(input('Digite a quantidade de produtos: '))
while produtos > 50:
    produtos = int(input('Digite a quantidade de produtos(menos que 50): '))


precos = []
nproduto = 1
count = 0

for i in range(produtos):
    print('Produto N° ', nproduto)
    preco = precos.append(float(input('Digite o preco do produto: ')))
    nproduto += 1

nproduto = 1
for j in range(produtos):
    print('Produto N° ',nproduto ,'=' , precos[count])
    count += 1
    nproduto += 1