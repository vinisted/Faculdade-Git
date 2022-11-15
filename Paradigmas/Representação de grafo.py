print("####### Lista de adjacências #######")
print("")
print("")

#Variavel contendo o tipo de grafo

print("Qual o tipo de grafo? ")
print("")
print('Digite "1" para não direcionado.')
print('Digite "2" para direcionado.')
print('Digite "3" para ponderado.')
tpgraf = int(input(""))

#Variavel contendo a quantidade de vertices
print("")
qtdver = int(input("Digite a quantidade de vértices do grafo: \n"))
print ("")

#Criando o grafo
grafo = []

#Caso o grafo não seja direcionado
if tpgraf == 1:

  #Recebendo os valores correspondentes aos vértices e arestas
  for i in range (qtdver):
    grafoaux = []
    ver = 1
    while True:
      ver = int(input(f'Digite os VÉRTICES correspondentes a [{i+1}] (Para parar digite "0"): \n'))
      are = int(input('Digite a quantidade de ARESTAS da ligação citada acima (Para parar digite "0"): \n'))
      print("")

      if ver and are != 0:
        grafoaux.append([ver]+[are])
      else:
        break
    print("___________________________________________________________________________")
    print("")

    grafo.append(grafoaux)

  #imprimindo a lista de adjacência
  print("Seu grafo é NÃO DIRECIONADO, portanto, abaixo estão impressos os vértices adjacentes aos valores digitados e suas respectivas arestas:")
  print("")
  for i in range (qtdver):
    print(f"Vertice [{i+1}] --> {grafo[i]}")

#Caso o grafo seja direcionado
elif tpgraf == 2:
  print("*Lembre-se que no grafo direcionado só é necessário digitar os vértices!")
  print("")

  #Recebendo os valores correspondentes aos vértices e arestas
  for i in range (qtdver):
    grafoaux = []
    ver = 1
    while True:
      ver = int(input(f'Digite os VÉRTICES correspondentes a [{i+1}] (Para parar digite "0"): \n'))

      if ver != 0:
        grafoaux.append(ver)
      else:
        break
    print("___________________________________________________________________________")
    print("")

    grafo.append(grafoaux)

  #imprimindo a lista de adjacência
  print("Seu grafo é DIRECIONADO, portanto, abaixo estão impressos os vértices adjacentes aos valores digitados:")
  print("")
  for i in range (qtdver):
    print(f"Vertice [{i+1}] --> {grafo[i]}")

#Caso o grafo seja ponderado
elif tpgraf == 3:

  #Recebendo os valores correspondentes aos vértices e arestas
  for i in range (qtdver):
    grafoaux = []
    ver = 1
    while True:
      ver = int(input(f'Digite os VÉRTICES correspondentes a [{i+1}] (Para parar digite "0"): \n'))
      vlr = int(input('Digite o VALOR da ligação citada acima (Para parar digite "0"): \n'))
      print("")

      if ver and vlr != 0:
        grafoaux.append([ver]+[vlr])
      else:
        break
    print("___________________________________________________________________________")
    print("")

    grafo.append(grafoaux)

  #imprimindo a lista de adjacência
  print("Seu grafo é PONDERADO, portanto, abaixo estão impressos os vértices adjacentes aos valores digitados e os respectivos valores das arestas:")
  print("")
  for i in range (qtdver):
    print(f"Vertice [{i+1}] --> {grafo[i]}")

else:
  print("O valor digitado para o tipo de grafo não é válido!")