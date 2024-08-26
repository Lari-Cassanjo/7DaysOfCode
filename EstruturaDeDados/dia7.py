# Árvores

class Produto:
    def __init__(self,id=0,nome='',quantidade=0):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade

class Node:
    def __init__(self,esquerda,direita,produto):
        self.esquerda = esquerda
        self.direita = direita
        self.produto = produto

class Arvore_Produto:
    def __init__(self):
        self.raiz = None
    
    def inserir(self,id=0,nome='',quantidade=0):
        produto = Produto(id,nome,quantidade)
    
    def buscar(self,id=0):
        pass
    
