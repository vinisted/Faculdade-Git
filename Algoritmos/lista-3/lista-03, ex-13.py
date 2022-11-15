num = int(input('digite um numero: '))
guard = 1

for i in range (num,1,-1):
    guard = guard * i
print('o fatorial de {} é {}'.format(num, guard))