def rotate_word(nome, rotação, rotacionado):
  alfabeto =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  nome = nome.lower()

  for i in range (len(nome)):
    for j in range (len(alfabeto)):
      if nome[i]==alfabeto[j]:
        rotacionado.append(alfabeto[j+rotação])

  return rotacionado
  
def imprimir_word (rotacionado):
  print ('')
  for i in range (len(rotacionado)):
    print (rotacionado[i], end='')


rotacionado1 = []

nome = input('Digite o nome para rotacionar: ')
rotação = int(input('Quer rotacionar por quantos? '))

rotate_word(nome, rotação, rotacionado1)
imprimir_word(rotacionado1)