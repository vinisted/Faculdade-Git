import math
    
print('Equaçao do 2° da forma: ax² + bx + c')
    
a = int( input('digite a variável a: ') )

if (a == 0):
    print('quando a=0 a equação não é do segundo grau')
else:
    b = int( input('digite a variável b: ') )
    c = int( input('digite a variável c: ') )
    delta = b*b - (4 * a * c)

if delta<0:
    print('Delta menor que 0 não possui raiz')

elif delta==0:
    raiz = -b / (2*a)
    print('Delta=0, raiz = ', raiz)

else:
    raiz1 = (-b + math.sqrt(delta) ) / (2*a)
    raiz2 = (-b - math.sqrt(delta) ) / (2*a)
    print('Raizes: ', raiz1, ' e ', raiz2)