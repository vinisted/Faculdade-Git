class Supermercado:
  def __init__(self, supermercado):
    self.supermercado = supermercado
    self.vendas = []
    self.next = None

class Venda:
  def __init__(self, venda):
    self.venda = venda
    self.valor = 0
    self.next = None

class Registro_Vendas:
  def __init__(self):
    self.head = None
  
  def CadastrarSupermercado(self,supermercado):
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Supermercado(supermercado)
    else:
      self.head = Supermercado(supermercado)

  def BuscarSupermercado(self,supermercado):
    aux = self.head
    while aux.supermercado != supermercado:
      aux = aux.next
    return aux
  
  def CadastrarVenda(self, venda, valor, supermercado):
    supermercado = self.BuscarSupermercado(supermercado)
    if supermercado:
      supermercado.vendas.append(Venda(venda))
      Venda.valor = valor
    else:
      print('Supermercado inexistente.')

  def relatorio(self):
    aux = self.head
    while aux:
      print(aux.supermercado, '\n-------------------------')
      for venda in aux.vendas:
        print(venda.venda, end = ' | Valor: R$ ')
        for valor in aux.vendas:
            print(valor.valor)
      aux = aux.next
      print('-------------------------\n')

supermercados = Registro_Vendas()
supermercados.CadastrarSupermercado('Supermercado 1')
supermercados.CadastrarSupermercado('Supermercado 2')
supermercados.CadastrarSupermercado('Supermercado 3')
supermercados.CadastrarSupermercado('Supermercado 4')

supermercados.CadastrarVenda('Desodorante', 13.83,'Supermercado 1')
supermercados.CadastrarVenda('Mouse', 42.99,'Supermercado 1')
supermercados.CadastrarVenda('Mesa', 1800,'Supermercado 2')
supermercados.CadastrarVenda('Pulseira', 3.89,'Supermercado 2')
supermercados.CadastrarVenda('Panela', 39.84,'Supermercado 1')
supermercados.CadastrarVenda('Bolsa', 129.99,'Supermercado 3')
supermercados.CadastrarVenda('Pulseira', 3.89,'Supermercado 4')
supermercados.CadastrarVenda('Flor', 5.99,'Supermercado 4')

supermercados.relatorio()
