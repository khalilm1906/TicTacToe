import sys

class TicTacToe:
    def __init__(self):
        self.board = [
            '1','2','3',
            '4','5','6',
            '7','8','9'
        ]

    def print_board(self):
        print("\n %s | %s | %s " %
              (self.board[0],
              self.board[1],
              self.board[2]))
        print("------------")
        print(" %s | %s | %s " %
              (self.board[3],
              self.board[4],
              self.board[5]))
        print("------------")
        print(" %s | %s | %s " %
              (self.board[6],
              self.board[7],
              self.board[8]))

    def start_game(self):
        no_winner = True
        marker = "X"
        while no_winner:
            self.print_board()
            cell = input("\n\"%s\" player enter the number of the cell you want to play: " % marker)
            try:
                index = int(cell)-1
                if self.board[index] == cell: # means cell not in use
                    self.board[index] = marker
                else:
                    print("Cell already taken by player %s. Try again." % self.board[index])
                    continue
            except:
                print("You must enter a valid integer 1-9.")
                print("Please try again.")
                continue

            if self.is_winner(marker):
                print("%s is the winner!" % marker)
                no_winner = False
                sys.exit(0)
            if self.board_full():
                print("It's a draw!")
                no_winner = False
                sys.exit(0)
            else:
                marker = ("O" if marker == "X" else "X")


    def is_winner(self, marker):
        if self.board[0] == marker and self.board[1] == marker and self.board[2] == marker:
            return True
        if self.board[3] == marker and self.board[4] == marker and self.board[5] == marker:
            return True
        if self.board[6] == marker and self.board[7] == marker and self.board[8] == marker:
            return True
        if self.board[0] == marker and self.board[3] == marker and self.board[6] == marker:
            return True
        if self.board[1] == marker and self.board[4] == marker and self.board[7] == marker:
            return True
        if self.board[2] == marker and self.board[5] == marker and self.board[8] == marker:
            return True
        if self.board[0] == marker and self.board[4] == marker and self.board[8] == marker:
            return True
        if self.board[6] == marker and self.board[4] == marker and self.board[2] == marker:
            return True
        else:
            return False

    def board_full(self):
        for cell in self.board:
            if cell == "X" or cell == "O":
                continue
            else:
                return False
        return True



if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()
