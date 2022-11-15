class Funcionario:

  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario

class TabelaHash:
    
  def __init__(self):
    self.tabela = [[],[],[],[],[],[],[],[],[],[]]

  def Hash(self, nome):
      m = (ord(nome[0]))
      m = m % 10
      return m

  def InserirFuncionario(self, nome, salario):
    value = self.Hash(nome)
    self.tabela[value].append(Funcionario(nome, salario))
  
  def BuscarSalario(self, nome):
    value = self.Hash(nome)
    for i in self.tabela[value]:
        if i.nome == nome:
            print('\nO salário de {} é: R$ {}'.format(nome, i.salario))
        else:
            print('\nFuncionário não encontrado!')

Menu = TabelaHash()
valor = 0

while valor != 3:
    print('-'*100)
    print('Menu de cadastramento de Funcionários')
    print('-'*100)
    print('Digite o que deseja fazer:')
    print('-'*100)
    print('1 - Cadastrar funcionário')
    print('2 - Buscar salário de um funcionário')
    print('3 - Sair')
    valor = int(input('\nDigite: '))

    if valor == 1:
        print('-'*100)
        funcionario = input('Digite o nome do funcionário: ')
        salario = float(input('Digite o salário: R$ '))
        Menu.InserirFuncionario(funcionario, salario)
        print('\nO(a) funcionário(a) {} foi inserido(a)!'.format(funcionario))
        input('\nDigite enter para continuar... ')

    elif valor == 2:
        print('-'*100)
        funcionario = input('Digite o nome do funcionário que deseja visualizar o salário: ')
        Menu.BuscarSalario(funcionario)
        input('\nDigite enter para continuar... ')

    elif valor == 3:
        print('-'*100)
        print('Programa encerrado...')

    else:
        print('-'*100)
        print('Valor inválido, tente novamente!')
        input('Digite enter para continuar... ')