numero = int(input('digite um numero: '))

if numero < 1000:
    unidades = numero // 1 % 10
    dezenas = numero // 10 % 10
    centenas = numero // 100 % 10
    if unidades > 1:
        unidadesString = "{} unidades".format(unidades)
    else:
        unidadesString = "{} unidade".format(unidades)
    if dezenas > 1:
        dezenasString = "{} dezenas".format(dezenas)
    else:
        dezenasString = "{} dezena".format(dezenas)
    if centenas > 1:
        centenasString = "{} centenas".format(centenas)
    else:
        centenasString = "{} centena".format(centenas)
    
    print("o numero digitado foi {} e ele contem: {}, {} e {}".format(numero, unidadesString, dezenasString, centenasString))