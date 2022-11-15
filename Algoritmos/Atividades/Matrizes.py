def crie_matriz(matriz, ordem):
    for i in range(ordem):
        matriz.append([0]*ordem)
    return matriz

def leit_matriz(matriz, ordem):
    for i in range (ordem):
        for j in range (ordem):
            print ('Digite o elemento [',i+1,',', j+1, ']:', sep='', end=' ' )
            matriz[i][j] = int(input())
    print()

def imp_mat(matriz, ordem):

    print('Representando sua matriz abaixo:\n')

    for i in range (ordem):
        for j in range (ordem):
            print (matriz[i][j], end=' ')
        print ()
    print()

def qmag(matriz, ordem):

    #diagonal principal
    som1=0
    for i in range(ordem):
        som1 = som1 + matriz[i][i]
        
    #diagonal secundaria
    som2=0
    for i in range(ordem):
        som2 = som2 + matriz[i][ordem-1-i]
    if (som2 != som1):
        print("Não é mágico")
        return

    #linhas
    for i in range(ordem):
        som2=0
        for j in range(ordem):
            som2=som2+matriz[i][j]
        if (som2 != som1):
            print("Não é mágico")
            return
            
    #colunas
    for j in range(ordem):
        som2=0
        for i in range(ordem):
            som2=som2+matriz[i][j]
        if (som2 != som1):
            print("Não é mágico")
            return
            
    print("É magico")


ord = int(input('Digite a ordem da Matriz: '))
print()

mat=[]

crie_matriz(mat,ord)
leit_matriz(mat,ord)
imp_mat(mat,ord)
qmag (mat,ord)