crt = input("Caractere: ")
crt2 = input("Caractere: ")
esp = ''
for linha in range(9):
    for coluna in range(9):
        if linha == coluna:
            print(crt * 2, end = '')
            print (crt * 2, end = '')
        elif (linha + coluna) == 8:
            print(crt2 * 2, end = '')
            print(crt2 * 2, end = '')
        else: 
            print(end ='  ')    
    print()