base=int(input('Informe a base:'))
vbase = base
expoente=int(input('Informe o expoente:'))

if (expoente == 1) or (expoente == 0):
  if (expoente == 1):
     print('Resultado:', base)
  else:
    print('Resultado: 1')
    
else:
  for i in range (expoente - 1):
    base*=vbase
  print('Resultado:', base)