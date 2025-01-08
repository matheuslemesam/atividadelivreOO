class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def fazer_cadastro(self):
        with open("alunos.txt", "a") as arquivo:
            arquivo.write(f"{self.nome};{self.idade};{str(self.notas)};\n")

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return f"Parabéns {self.nome}, você está aprovado com média {media:.2f}."
        else:
            return f"{self.nome}, você está reprovado com média {media:.2f}."

# Testando a classe Aluno
aluno1 = Aluno("José", 19, [6, 7, 8, 3])
aluno1.fazer_cadastro()
print(aluno1.verificar_aprovacao())

aluno2 = Aluno("Maria", 20, [9, 8, 10, 7])
aluno2.fazer_cadastro()
print(aluno2.verificar_aprovacao())