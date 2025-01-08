class Evento:
    def __init__(self, nome, descricao, horario_inicio, horario_fim):
        self.nome = nome
        self.descricao = descricao
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim

    def __repr__(self):
        return f"Evento(nome='{self.nome}', descricao='{self.descricao}', " \
            f"horario_inicio='{self.horario_inicio}', horario_fim='{self.horario_fim}')"


class Agenda:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        if self.verificar_conflito(evento):
            print("Conflito de horário! O evento não pode ser adicionado.")
        else:
            self.eventos.append(evento)
            print(f"Evento '{evento.nome}' adicionado com sucesso!")

    def verificar_conflito(self, novo_evento):
        for evento in self.eventos:
            if (novo_evento.horario_inicio < evento.horario_fim and
                    novo_evento.horario_fim > evento.horario_inicio):
                return True
        return False

    def listar_eventos(self):
        if not self.eventos:
            print("Nenhum evento agendado.")
        for evento in self.eventos:
            print(evento)

if __name__ == "__main__":
    agenda = Agenda()

    evento1 = Evento("Reunião", "Reunião com a equipe", "2023-10-10 10:00", "2023-10-10 11:00")
    evento2 = Evento("Almoço", "Almoço com cliente", "2023-10-10 12:00", "2023-10-10 13:00")
    evento3 = Evento("Reunião", "Reunião de feedback", "2023-10-10 10:30", "2023-10-10 11:30") 

    agenda.adicionar_evento(evento1)
    agenda.adicionar_evento(evento2)
    agenda.adicionar_evento(evento3) 

    agenda.listar_eventos()