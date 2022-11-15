tmn = int(input("digite o tamanho: "))
crt = input("digite o caractere desejado: ")
var = crt

for i in range(tmn):
    if i==0:
        print(crt)
    else:
        print(var + crt)
        var = var + crt