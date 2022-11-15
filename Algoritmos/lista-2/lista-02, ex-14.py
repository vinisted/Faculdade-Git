print('Este é um quesrionário com intuito de investigar provas de um crime, favor escrever as respostas somente entre sim e não!')
perguntas = [ 'Telefonou para a vítima? ' ,'Esteve no local do crime? ' ,'Mora perto da vítima? ', 'Devia para a vítima? ' ,'Já trabalhou com a vítima? ' ]
resposta = 0

for qual in perguntas:
  resposta += (input(qual) == 'sim')
  
if resposta == 5:
  print('Assassino')
elif resposta >=3:
  print('Cúmplice')
elif resposta ==2:
  print('Suspeito')
else:
  print('Inocente')