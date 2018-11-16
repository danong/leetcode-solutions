import random


class TicTacToe:
    """TicTacToe game instance

    human plays against AI

    human player uses 'x'
    ai player uses 'o'

    board indices are:
    6 7 8
    3 4 5
    0 1 2

    """

    def __init__(self, player_first: bool = True) -> None:
        self.board = [' '] * 9
        self.valid_moves = {i for i in range(9)}
        self.turn = int(player_first)

    def display(self):
        print(f' {self.board[6]} | {self.board[7]} | {self.board[8]}')
        print('-----------')
        print(f' {self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('-----------')
        print(f' {self.board[0]} | {self.board[1]} | {self.board[2]}')

    def move(self):
        if self.turn % 2:  # human turn
            move = int(input('enter a move: '))
            while move not in self.valid_moves:
                print(f'invalid move. please choose from: \n{self.valid_moves}')
                move = int(input('enter a move: '))
            self.board[move] = 'x'
        else:
            move = random.choice(tuple(self.valid_moves))
            self.board[move] = 'o'
            print(f'ai makes move {move}')
        self.valid_moves.remove(move)

    def play(self):
        while True:
            print(f'turn {self.turn}')
            self.display()
            self.move()
            self.turn += 1


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
