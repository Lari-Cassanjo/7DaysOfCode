# Lista Duplamente Encadeada

class Produto:
    def __init__(self, nome, codigo_de_barras, preco, quantidade):
        self.nome = nome
        self.codigo_de_barras = codigo_de_barras
        self.preco = preco
        self.quantidade = quantidade
        self.proximo = None

class Lista_de_produtos:
    def __init__(self):
        self.primeiro = None
        
    def add_produto(self, nome='', codigo_de_barras=0, preco=0.0, quantidade=0):
        novo_produto = Produto(nome, codigo_de_barras, preco, quantidade)
        if self.primeiro == None:
            self.primeiro = novo_produto
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_produto
    
    def remover_produto(self, nome=''):
        atual = self.primeiro
        encontrou = False
        if self.primeiro.nome == nome:
            self.primeiro = atual.proximo
        else:
            anterior = atual
            atual = atual.proximo
            
        while atual != None:
            if atual.nome == nome:
                anterior.proximo = atual.proximo
                encontrou = True
                print(f'\33[32mProduto "{nome}" removido com sucesso!\33[m\n')
                break
            else:
                anterior = atual
                atual = atual.proximo
        if not encontrou:
            print(f'\33[31mProduto "{nome}" não encontrado!\33[m\n')
    
    def att_produto(self, nome='', quantidade=0):
        atual = self.primeiro
        encontrou = False
        while atual != None:
            if atual.nome == nome:
                atual.quantidade = quantidade
                print(f'\33[32mQuantidade do produto "{nome}" atualizada com sucesso!\33[m\n')
                encontrou = True
                break
            else:
                atual = atual.proximo
        if not encontrou:
            print(f'\33[31mProduto "{nome}" não encontrado!\33[m\n')
    
    def buscar_nome(self, nome=''):
        atual = self.primeiro
        encontrou = False
        while atual != None:
            if atual.nome == nome:
                print('\33[32mProduto em estoque!\33[m')
                print(f'{atual.nome:<16}|{atual.codigo_de_barras:^10}| R$ {atual.preco:<9}| {atual.quantidade:<}\n')
                encontrou = True
                break
            else:
                atual = atual.proximo
        if not encontrou:
            print(f'\33[31mProduto "{nome}" não encontrado!\33[m\n')
    
    def buscar_codigo(self, codigo=0):
        atual = self.primeiro
        encontrou = False
        while atual != None:
            if atual.codigo_de_barras == codigo:
                print('\33[32mProduto em estoque!\33[m')
                print(f'{atual.nome:<16}|{atual.codigo_de_barras:^10}| R$ {atual.preco:<9}| {atual.quantidade:<}\n')
                encontrou = True
                break
            else:
                atual = atual.proximo
        if not encontrou:
            print(f'\33[31mCódigo "{codigo}" não encontrado!\33[m\n')
    
    def listar_produtos(self):
        if self.primeiro is None:
            print('Nenhum produto cadastrado!')
        else:
            atual = self.primeiro
            print(f'{'Produto':^16}|{'Código':^10}|{'Preço':^13}|{'Quantidade':^12}')
            while atual is not None:
                print(f'{atual.nome:<16}|{atual.codigo_de_barras:^10}| R$ {atual.preco:<9}| {atual.quantidade:<}')
                atual = atual.proximo
        
produtos = Lista_de_produtos()

produtos.add_produto('Garrafa',12345678,17.90,5)
produtos.add_produto('Bolsa Térmica',87654321,123.45,12)
produtos.add_produto('Pilha',56781234,4.30,109)
produtos.add_produto('Porta Copos',43218765,55.90,12)
produtos.remover_produto('Corda')
produtos.remover_produto('Pilha')
produtos.buscar_nome('Bolsa Térmica')
produtos.buscar_nome('Pilha')
produtos.buscar_codigo(12345678)
produtos.buscar_codigo(78564312)
produtos.att_produto('Garrafa',9)
produtos.att_produto('Copos', 7)

produtos.listar_produtos()
