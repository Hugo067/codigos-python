class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir(self):
        print(f'Título: {self.titulo},Autor: {self.autor}')
     
a = Livro("a menina que roubava livros", "Markus Zusak")

a.exibir()