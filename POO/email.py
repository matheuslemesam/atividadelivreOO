class Email:
    def __init__(self, remetente):
        self.remetente = remetente
        self.caixa_de_entrada = []  # Lista para armazenar mensagens recebidas

    def enviar(self, destinatario, assunto, corpo):
        mensagem = {
            'remetente': self.remetente,
            'destinatario': destinatario,
            'assunto': assunto,
            'corpo': corpo
        }
        print(f"Email enviado para {destinatario} com assunto: '{assunto}'")
        return mensagem  

    def receber(self, mensagem):
        self.caixa_de_entrada.append(mensagem)
        print(f"Email recebido de {mensagem['remetente']} com assunto: '{mensagem['assunto']}'")

    def listar_mensagens(self):
        if not self.caixa_de_entrada:
            print("A caixa de entrada está vazia.")
        else:
            print("Mensagens recebidas:")
            for i, mensagem in enumerate(self.caixa_de_entrada, start=1):
                print(f"{i}. De: {mensagem['remetente']}, Assunto: {mensagem['assunto']}")

if __name__ == "__main__":
    email1 = Email("usuario1@example.com")
    email2 = Email("usuario2@example.com")

    mensagem_enviada = email1.enviar("usuario2@example.com", "Olá!", "Como você está?")

    email2.receber(mensagem_enviada)

    email2.listar_mensagens()