idade = 0
sexo = 0 
eye = 0
hair = 0
continuar = 1

mid = 0
var1 = 0

while continuar != 0:

    idade = int(input("digite sua idade:"))
    ver1 = 0
    if idade >= 18 and idade <= 35:
        ver1 = 1

    sexo = input("digite seu sexo (masculino ou feminino):")
    ver2 = 0
    if sexo == 'feminino':
        ver2 = 1
    
    eye = input("digite a cor dos seus olhos (castanho, verde ou azul):")
    ver3 = 0
    if eye == 'verde':
        ver3 = 1

    hair = input("digite a cor dos seus cabelos (louro, castanho ou preto):")
    ver4 = 0
    if hair == 'louro':
        ver4 = 1

    print ("")

    if mid < idade:
        mid = idade

    if ver1 and ver2 and ver3 and ver4 == 1:
        var1+=1

    if idade != 0:
        continuar = int(input('Deseja continuar? sim = 1/ não = 0 '))
        print()

print ('')
print ('A maior idade entre os habitantes é:', mid,'anos.')
print ('A quantidade de indivíduos do sexo feminino que tenha entre 18 e 35 anos com olhos'
'\nverdes e cabelos louros é de',var1, 'individuo(os)')