#formula da area do triângulo equilátero = l²*√3/4 - (angulo 60º)
#formula da area do quadrado = b*h
#formula da area do pentágono = 5*l*a/2 - (angulo de 108º)
#formula da apotema = mesma da tangente (tan = co/ca)


print ('')
print ('Neste programa você irá digitar informações sobre um polígono regular.')
print ('')

lados = int ( input ('Digite o número de lados: '))

if lados < 3:
    quit ('Não é um polígono.')
elif lados > 5:
    quit ('Polígono não identificado.')

cm = float ( input ('Digite o tamanho de cada lado: '))

if lados == 3:
    quad =  cm**2/4
    print ('Este polígono regular é um TRIÂNGULO equilátero.')
    print ('Área:', quad,'√3 cm², ou', quad * 1.73205080757, 'cm².')

elif lados == 4:
    ar = cm * cm
    print ('Este polígono regular é um QUADRADO.')
    print ('Área:', ar, 'cm².')

else:
    apot = cm/1.453
    are = 5 * cm * apot
    area = are/2
    print ('Este polígono regular é um PENTÁGONO equilátero.')
    print ('Área:', area, 'cm².')