num = int(input('Escolhe a quantidade de números : '))
x = 0
y = []

for i in range(num):
  v = int(input('Valor do número : '))
  x = x + v
  y = y + [v]
  
  
maior = max(y)
menor = min(y)
soma = sum(y)

print('O maior valor será',maior,', o menor valor será',menor,'e a soma de tudo será',x)