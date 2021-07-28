# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.erro = []
        self.acerto = []
        
    # Método para adivinhar a letra
    def guess(self, letter):
        if letter not in self.word :
            if letter not in self.erro :
                self.erro.append(letter)
                return
        else :
            if letter not in self.acerto :
                self.acerto.append(letter)
                return

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.hangman_won() :
            return False
        if len(self.erro) < len(board) :
            return True
        
    # Método para verificar se o jogador venceu
    def hangman_won(self):
        # acertos = []
        for i in self.word:
            if i not in self.acerto :
                return False
                # acertos.append(i)       
        return True

    # Método para não mostrar a letra no board
    def hide_word(self):
        tamanho = len(self.word)
        mask = '-' * tamanho
        if len(self.acerto) == 0 :
            return mask
        else :
            mask = list(self.word)
            for x,y in enumerate(mask):
                if y not in self.acerto :
                    mask[x] = '-'
            return ''.join(mask)
        
    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.erro)])
        print(self.hide_word())
        print('Letras erradas:')
        for i in self.erro :
            print(i)
        print('\nLetras certas:')
        for j in self.acerto :
            print(j)


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
            bank = f.readlines()
    return bank[random.randint(0,len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())
    # print(board[0])
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while game.hangman_over(): 
        # Verifica o status do jogo
        game.print_game_status()    
        chute = input('\nDigite uma letra: ')
        game.guess(chute)
    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print ('\nParabéns! Você venceu!!')
        print ('A palavra era ' + game.word)
    else:
        print ('\nGame over! Você perdeu.')
        print ('A palavra era ' + game.word)
        
    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa        
if __name__ == "__main__":
    main()