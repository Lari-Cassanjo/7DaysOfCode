# Lista Encadeada

# Head -> primeiro nó da lista
# Tail -> último nó da lista

class Paciente:
    def __init__(self, nome, id, estado):
        self.nome = nome
        self.id = id
        self.estado = estado
        self.proximo = None        

class ListaPacientes():
    def __init__(self):
        self.primeiro = None
    
    def add_paciente(self, nome, id, estado):
        novo_paciente = Paciente(nome,id,estado)
        if self.primeiro is None:
            self.primeiro = novo_paciente
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_paciente
    
    def remover_paciente(self,nome):
        atual = self.primeiro
        encontrou = False
        if atual.nome == nome:
            self.primeiro = atual.proximo
        else:
            anterior = atual
            atual = atual.proximo
        
        while atual != None:
            if atual.nome == nome:
                anterior.proximo = atual.proximo
                encontrou = True
                break
            else:
                anterior = atual
                atual = atual.proximo
        if not encontrou:
            print('Paciente não encontrado!')

    def listar_pacientes(self):
        atual = self.primeiro
        while atual is not None:
            print(f'Nome: {atual.nome:<10} | Id: {atual.id} | Estado: {atual.estado}')
            atual = atual.proximo

paciente = ListaPacientes()
paciente.add_paciente('Antônio',1,'em tratamento')
paciente.add_paciente('Luander',2,'liberado')
paciente.add_paciente('Yuri',3,'em tratamento')
paciente.add_paciente('Larissa',4,'estável')
paciente.add_paciente('Alessandra',5,'crítico')
paciente.add_paciente('Aline',6,'em tratamento')
paciente.listar_pacientes()
print('-'*60)
paciente.remover_paciente('Luander')
paciente.remover_paciente('Larissa')
paciente.listar_pacientes()
