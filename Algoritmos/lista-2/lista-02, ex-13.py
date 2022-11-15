sacar = int(input('qual valor deseja sacar? '))
    
if sacar >= 10 and sacar <= 600:
    n100 = sacar // 100
    sacar -= n100 * 100
        
    n50 = sacar // 50
    sacar -= n50 * 50
        
    n10 = sacar // 10
    sacar -= n10 * 10
        
    n5 = sacar // 5
    sacar -= n5 * 5

    n1 = sacar // 1
    sacar -= n1 * 1
    print('sairão: {} notas de 100, {} notas de 50, {} notas de 10, {} notas de 5 e {} notas de 1'.format(n100,n50,n10,n5,n1))

else:
    print('valor invalido')