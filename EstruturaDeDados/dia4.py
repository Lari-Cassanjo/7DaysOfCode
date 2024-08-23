# Filas

# Enqueue (enfileirar: adicionar ao final da lista)
# Dequeue (desenfileirar: remover o primeiro elemento da fila)

class Pedido:
    def __init__(self,numero=0,cliente='',itens='',total=0.0):
        self.numero = numero
        self.cliente = cliente
        self.itens = itens
        self.total = total

class Fila_de_Pedidos:
    def __init__(self):
        self.fila = []
    
    def add_pedido(self, numero=0,cliente='',itens='',total=0.0):
        novo_pedido = Pedido(numero,cliente,itens,total)
        for pedido in self.fila:
            if pedido['numero'] == numero:
                print(f'O pedido nº {numero} já existe!')
                return
        self.fila.append({'numero': novo_pedido.numero, 'cliente': novo_pedido.cliente, 'itens': novo_pedido.itens, 'total': novo_pedido.total})
    
    def remover_pedido(self):
        self.fila.pop(0)
        print('Pedido atendido com sucesso!')
    
    def listar_pedidos(self):
        if not self.fila:
            print('Nenhum pedido registrado!')
        else:
            print(f'{'ID':^4} | {'Cliente':^12} | {'Itens do Pedido':^30} | {'Total':^6}')
            for pedido in self.fila:
                print(f'{pedido['numero']:^4} | {pedido['cliente']:<12} | {pedido['itens']:<30} | R$ {pedido['total']}')

pedido = Fila_de_Pedidos()

pedido.add_pedido(1,'Joana','Filé com batata',32.50)
pedido.add_pedido(2,'Carlos','Arroz com bife',27.90)
pedido.add_pedido(2,'Carlos','Arroz com bife',27.90)
pedido.add_pedido(3,'Paula','Escondidinho de Frango',44.50)

pedido.listar_pedidos()

pedido.remover_pedido()

pedido.listar_pedidos()
