print ('')
fms1 = [0]*10
frn = input('Você é um fornecedor? (caso seja digite "sim") ')
print ('')

#listando nome dos filmes

if frn == 'sim':
    for i in range (10):
        fms1[i] = input('Digite um filme:')
print ('')

if frn != 'sim':
    fms1 = ['star wars I ep', 'star wars II ep', 'star wars III ep', 'star wars IV ep', 'star wars V ep', 'star wars VI ep', 'star wars VII ep', 'star wars VIII ep', 'star wars IX ep', 'rogue one - uma história star wars']

# booleanos usuario 1

usuario1 = input('Seja bem vindo! Você é o usuário nº 1, Qual o seu nome? ')

print ('')

print ('Observe a lista de indicações de filmes abaixo: ')
print (fms1)

print ('')

cont = int(input('Da lista citada, QUANTOS filmes você já assistiu? '))
us1 = [0]*cont

print ('')

if cont == 0:
    print ('Querido(a)', usuario1, '. Está a procura de se tornar um grande cinéfilo? - Logo menos te indicaremos excelentes filmes, AGUARDE! :D ')
if cont == 1:
    for i in range (1):
        us1[i] = input ('Digite o filme que você assistiu (digite assim como escrito pelo fornecedor): ')
    print ('')
    print ('Nossa', usuario1, 'esse filme é excelente! vimos que gostou do popular:', us1, '- Logo menos te indicaremos excelentes filmes!')

elif cont > 1:
    for i in range (1):
        us1[i] = input('Digite um dos filmes que você assistiu (digite assim como escrito pelo fornecedor): ')
        for j in range (cont-1):
            us1[j+1] = input('Digite outro filme (digite assim como escrito pelo fornecedor): ')
    print ('')
    print ('Nossa', usuario1, 'Esses seus filmes são excelentes! vimos que gostou dos populares:', us1, '- Logo menos te indicaremos excelentes filmes!')

print ('_________________________________________________________________________________________________________________________________')
print ('')

# booleanos usuario 2

usuario2 = input('Seja bem vindo! Você é o usuário nº 2, Qual o seu nome? ')

print ('')

print ('Observe a lista de indicações de filmes abaixo: ')
print (fms1)

print ('')

cont2 = int(input('Da lista citada, QUANTOS filmes você já assistiu? '))
us2 = [0]*cont2

print ('')

if cont == 0:
    print ('Querido(a)', usuario2, '. Está a procura de se tornar um grande cinéfilo? - Logo menos te indicaremos excelentes filmes, AGUARDE! :D ')

if cont2 == 1:
    for i in range (1):
        us2[i] = input ('Digite o filme que você assistiu (digite assim como escrito pelo fornecedor): ')
    print ('')
    print ('Nossa', usuario2, 'esse filme é excelente! vimos que gostou do popular:', us2, '- Logo menos te indicaremos excelentes filmes!')

elif cont2 > 1:
    for i in range (1):
        us2[i] = input('Digite um dos filmes que você assistiu (digite assim como escrito pelo fornecedor): ')
        for j in range (cont2-1):
            us2[j+1] = input('Digite outro filme (digite assim como escrito pelo fornecedor): ')
    print ('')
    print ('Nossa', usuario2, 'esses seus filmes são excelentes! vimos que gostou dos populares:', us2, '- Logo menos te indicaremos excelentes filmes!')

print ('')
print ('_________________________________________________________________________________________________________________________________')
print ('')

#indicando filmes aos usuários

#caso os dois usuários não tenham assistido...

if cont + cont2 == 0:
    print ('Eiiii querido(a)', usuario1, ', Dá uma olhada nessa bela #maratona que te indicamos:')
    print (fms1)

    print ('_________________________________________________________________________________________________________________________________')
    print ('')

    print ('Eiiii querido(a)', usuario2, ', Dá uma olhada nessa bela #maratona que te indicamos:')
    quit (fms1)

#variáveis de indicação dos filmes

usn1 = []
usn2 = []

#caso um dos usuários não tenha assistido nenhum filme...

if cont == 0:

    usn1.append(us2)

    for i in fms1:
        if i not in us2:
            usn2.append(i)

    print ('Olá', usuario1, 'tudo bom? #fica a dica desses belos filmes para ti!')
    print (usn1)

    print ('_________________________________________________________________________________________________________________________________')
    print ('') 

    print ('Olá', usuario2, 'tudo bom? Você aparenta ser o nosso #cliente mais maratonista hein, #fica a dica desses belos filmes para ti!')
    quit (usn2)

elif cont2 == 0:

    usn2.append(us1)

    for i in fms1:
        if i not in us1:
            usn1.append(i)

    print ('Olá', usuario1, 'tudo bom? Você aparenta ser o nosso #cliente mais maratonista hein, #fica a dica desses belos filmes para ti!')
    print (usn1)

    print ('_________________________________________________________________________________________________________________________________')
    print ('') 

    print ('Olá', usuario2, 'tudo bom? #fica a dica desses belos filmes para ti!')
    quit (usn2)

#condição mencionada na atividade...

elif cont and cont2 != 0:

    for i in us2:
        if i not in us1:
            usn2.append(i)

    for i in us1:
        if i not in us2:
            usn1.append(i)

    print ('Olá', usuario1, 'tudo bom? #fica a dica desses belos filmes para ti!')
    print (usn2)

    print ('_________________________________________________________________________________________________________________________________')
    print ('') 


    print ('Olá', usuario2, 'tudo bom? #fica a dica desses belos filmes para ti!')
    print (usn1)