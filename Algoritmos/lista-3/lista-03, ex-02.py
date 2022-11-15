#2.	Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('digite um nome de usuário: ')
senha = input('digite uma senha: ')

while senha == nome:
    senha = input('sua senha não pode ser igual ao nome de usuário, digite outra senha: ')

print('seu login é',nome)
print('sua senha é', senha)