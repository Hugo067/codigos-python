class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append({"nome": nome, "telefone": telefone})
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        if self.contatos:
            for contato in self.contatos:
                print(f"Nome: {contato['nome']} | Telefone: {contato['telefone']}")
        else:
            print("A agenda está vazia.")

agenda = Agenda()
agenda.adicionar_contato("Eduarda", "1234-5678")
agenda.adicionar_contato("Mario", "9876-5432")
agenda.listar_contatos()
