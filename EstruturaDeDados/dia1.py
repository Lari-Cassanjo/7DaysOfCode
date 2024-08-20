# Arrays

print('LISTA DE COMPRAS')

class ListaDeCompras:
    itens = []
    quantidade = []

    def listar(self):
        if self.itens == []:
            print('Lista vazia!')
        for i in self.itens:
            pos = self.itens.index(i)
            q = self.quantidade[pos]
            print(f'{i:<12} - {q:>4} un')
    
    def add(self,produto,quantidade):
        self.itens.append(produto)
        self.quantidade.append(quantidade)

    def remover(self,produto):
        pos = self.itens.index(produto)
        self.quantidade.pop(pos)
        self.itens.remove(produto)

print('1- Ver lista \n2- Adicionar item \n3- Remover item \n4- Sair')
selecao = 0
lista = ListaDeCompras()
while selecao != 4:
    try:
        selecao = int(input('Selecione uma ação: '))
        if selecao == 1:
            lista.listar()
        elif selecao == 2:
            lista.add(input('Produto: '), input('Quantidade: '))
        elif selecao == 3:
            lista.remover(input('Produto: '))
        else:
            if selecao != 4: 
                print('Comando inválido! Tente novamente.')
                selecao = int(input('Selecione uma ação: '))
    except ValueError:
        print('Comando inválido! Tente novamente.')
print('Até mais!')
