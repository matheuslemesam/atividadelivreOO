class Animal: #criar classe
    def __init__ (self, nome, especie): #contrutor de classe e parâmetros
        self.nome = nome #atributo da classe
        self.especie = especie #atributo...
        #pass , deixar a definição para depois

    def fazer_som(self): #método
        return "som genérico"
    
class Cachorro(Animal): #subclasse de Animal, herda atributos e métodos
    def fazer_som(self):
        return "Au au"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau"

nomec = input("Qual o nome do cachorro? ")
especiec = input("Qual a espécie do cachorro? ")

nomeg = input("Qual o nome do gato? ")
especieg = input("Qual a espécie do gato? ")

cachorro = Cachorro(nomec, especiec)
gato = Gato(nomeg, especieg)

print(f"{cachorro.nome} é um {cachorro.especie} e faz {cachorro.fazer_som()}") #acessa usando objetos
print(f"{gato.nome} é um {gato.especie} e faz {gato.fazer_som()}")