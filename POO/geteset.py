class Veiculo:
    def __init__(self, cor, idade):
        self._cor = cor  # Atributo privado
        self._idade = idade  # Atributo privado

    @property
    def cor(self):
        """Getter para a cor do veículo."""
        return self._cor

    @cor.setter
    def cor(self, nova_cor):
        """Setter para a cor do veículo."""
        self._cor = nova_cor

    @property
    def idade(self):
        """Getter para a idade do veículo."""
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        """Setter para a idade do veículo, com verificação."""
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("Erro! A idade não pode ser negativa!")

veiculo = Veiculo("vermelho", 5)
print(veiculo.cor)  # Saída: vermelho

veiculo.cor = "azul"
print(veiculo.cor)  # Saída: azul

try:
    veiculo.idade = -3  # definir uma idade negativa
except ValueError as e:
    print(e)  # Saída: Erro! A idade não pode ser negativa!