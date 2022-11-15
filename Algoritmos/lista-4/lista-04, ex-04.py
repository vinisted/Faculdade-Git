esp =" "
tmn = int(input("digite o tamanho: "))
crt = input("digite o caractere desejado: ")

for i in range(tmn):
  if(i == 0):
    print(crt*2)
  else:
    print(" " + esp + (crt * 2))
    esp = esp + " " + " "