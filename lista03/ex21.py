class Livro:
    def __init__(self, titulo, autor, estoque):
        self.titulo = titulo
        self.autor = autor
        self.estoque = max(estoque, 0)  # Evita que o estoque seja negativo

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Quantidade em estoque: {self.estoque}")

    def vender_livro(self):
        if self.estoque > 0:
            self.estoque -= 1
            print(f"Livro vendido! Estoque atual: {self.estoque}")
        else:
            print("Não há mais livros em estoque.")

    def reabastecer_estoque(self, quantidade):
        if quantidade > 0:
            self.estoque += quantidade
            print(f"Estoque reabastecido com {quantidade} unidades. Estoque atual: {self.estoque}")
        else:
            print("Quantidade inválida para reabastecimento.")

livro = Livro("O Alquimista", "Paulo Coelho", 10)
livro.exibir_detalhes()
livro.vender_livro()
livro.reabastecer_estoque(5)
