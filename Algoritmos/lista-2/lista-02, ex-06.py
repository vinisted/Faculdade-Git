n1 = float(input('digite um numero: '))
n2 = float(input('digite um numero: '))
n3 = float(input('digite um numero: '))

# caso sejam diferentes

if n1 > n2 > n3:
    print(n1, n2, n3)
if n1 > n3 > n2:
    print(n1, n3, n2)
if n2 > n1 > n3:
    print(n2, n1, n3)
if n2 > n3 > n1:
    print(n2, n3, n1)
if n3 > n1 > n2:
    print(n3, n1, n2)
if n3 > n2 > n1:
    print(n3, n2, n1)

# caso sejam iguais:

# 1° maneira:

if n2 > n1 == n3:
    print(n2, n1)
if n1 == n2 > n3:
    print(n1, n3)
if n1 > n2 == n3:
    print(n1, n3)

# 2° maneira:

if n2 < n1 == n3:
    print(n1, n2)
if n1 == n2 < n3:
    print(n3, n1)
if n1 < n2 == n3:
    print(n3, n1)