class Point:
  def __init__(self, x, y):
    self.x= x
    self.y= y
  def imprimir(self):
    print(f'Minha coordenada x é: {self.x}')
    print(f'Minha coordenada y é: {self.y}')

pt= Point(2,3)
pt.imprimir()

