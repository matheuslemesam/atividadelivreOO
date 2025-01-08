class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []  

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10: 
            self.notas.append(nota)
            print(f"Nota {nota} adicionada para o estudante {self.nome}.")
        else:
            print("Nota inválida. As notas devem estar entre 0 e 10.")

    def calcular_media(self):
        if not self.notas:  
            print(f"O estudante {self.nome} não tem notas para calcular a média.")
            return None
        media = sum(self.notas) / len(self.notas)
        return media

#uso da classe Estudante
if __name__ == "__main__":
    estudante1 = Estudante("João")
    
    estudante1.adicionar_nota(8.5)
    estudante1.adicionar_nota(7.0)
    estudante1.adicionar_nota(9.0)

    media = estudante1.calcular_media()
    if media is not None:
        print(f"A média de notas do estudante {estudante1.nome} é: {media:.2f}")