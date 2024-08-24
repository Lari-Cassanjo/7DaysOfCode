# Pilhas

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        
class Pilha_de_Livros:
    def __init__(self):
        self.pilha = []
    
    def add_livro(self,titulo,paginas):
        novo_livro = Livro(titulo,paginas)
        for livro in self.pilha:
            if livro['titulo'] == titulo:
                print(f'{titulo} já foi adicionado!')
                return
        self.pilha.append({'titulo':novo_livro.titulo, 'paginas':novo_livro.paginas})
    
    def remover_livro(self):
        fora = self.pilha.pop()
        print(f'"{fora['titulo']}" foi removido da pilha!')
    
    def exibir_topo(self):
        topo = self.pilha[-1]
        print(f'O último livro adicionado foi "{topo['titulo']}"')
    
    def mostrar_todos(self):
        for livro in self.pilha:
            print(f'{livro['titulo']:<20} | {livro['paginas']:<} páginas')
            
livro = Pilha_de_Livros()

livro.add_livro('A Guerra dos Tronos',694)
livro.add_livro('A Fúria dos Reis',768)
livro.add_livro('Tormenta de Espadas',973)
livro.add_livro('Festim dos Corvos',753)

livro.mostrar_todos()

livro.remover_livro()
livro.exibir_topo()
livro.remover_livro()

livro.mostrar_todos()
