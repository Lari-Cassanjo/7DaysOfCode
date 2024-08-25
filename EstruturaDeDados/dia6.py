# Hashmaps

class Jogo:
    def __init__(self):
        self.jogadores = {}
        
    def add_jogador(self,nome='',pontos=0):
        jogadores = self.jogadores
        if jogadores == {}:
            jogadores[nome] = pontos
            print('Jogador adicionado com sucesso!')
        else:
            if nome in jogadores:
                print(f'{nome} já existe!')
                return
            else:
                jogadores[nome] = pontos
                print('Jogador adicionado com sucesso!')
    
    def att_pontuação(self,nome,pontos):
        jogador = self.jogadores
        print()
        if jogador == {}:
            print('Sem jogadores cadastrados!')
        else:
            jogador[nome] = pontos
            print('Pontuação atualizada com sucesso!')
    
    def remover_jogador(self,nome):
        jogador = self.jogadores
        print()
        if jogador == {}:
            print('Sem jogadores cadastrados!')
        elif nome not in jogador:
            print('Jogador não cadastrado!')
        else:
            del jogador[nome]
            print(f'{nome} removido com sucesso!')
    
    def listar_jogadores(self):
        jogador = self.jogadores
        print()
        if jogador == {}:
            print('Sem jogadores cadastrados!')
        else:
            for jogador, pontos in jogador.items():
                print(f'O jogador {jogador} tem {pontos} pontos')

jogo = Jogo()
jogo.listar_jogadores()
jogo.remover_jogador('Yuri')

jogo.add_jogador('Luander',21)
jogo.add_jogador('Yuri',24)
jogo.add_jogador('Luander',12)
jogo.add_jogador('Larissa',25)

jogo.listar_jogadores()

jogo.att_pontuação('Luander',19)

jogo.listar_jogadores()

jogo.remover_jogador('Yuri')
jogo.remover_jogador('Paula')

jogo.listar_jogadores()
