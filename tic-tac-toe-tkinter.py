from tkinter import *


class Tile(Label):
    def __init__(self, parent, check_winner, get_current_player):
        Label.__init__(self, parent, font=('', 50), width=2, justify='center', relief='raised', bg='gray')
        self.bind('<Button-1>', self.mark)
        self.marked = ""
        self.check_winner = check_winner
        self.get_current_player = get_current_player

    def mark(self, event):
        if not self.marked:
            current_player = self.get_current_player()
            self.config(text=current_player)
            self.marked = current_player
            self.check_winner()


class Main:
    def __init__(self, parent):
        self.parent = parent
        self.x_player = StringVar()
        self.o_player = StringVar()
        self.winner = StringVar()
        self.current_player = 'X'
        self.mainFrame = Frame(self.parent)
        self.gameFrame = Frame(self.parent)
        self.winFrame = Frame(self.parent)
        self.tiles = []
        self.create_widgets()

    def create_widgets(self):
        Label(self.mainFrame, text="Tic Tac Toe", font=("", 50)).pack()
        frame1 = Frame(self.mainFrame)
        Label(frame1, text='X Player').grid(padx=5, pady=5)
        Entry(frame1, textvariable=self.x_player).grid(row=0, column=1, padx=5, pady=5)
        Label(frame1, text='O Player').grid(padx=5, pady=5)
        Entry(frame1, textvariable=self.o_player).grid(row=1, column=1, padx=5, pady=5)
        frame1.pack()
        Button(self.mainFrame, text='Start', command=self.start).pack()
        self.mainFrame.pack(padx=10, pady=10)
        self.gameFrame = Frame(self.parent)
        Label(self.winFrame, textvariable=self.winner, font=("", 50)).pack()
        Button(self.winFrame, text="Play Again", command=self.start).pack()

    def start(self):
        self.current_player = 'X'  # initialize 'X' as the current player at start of each game.
        x_player = self.x_player.get()
        o_player = self.o_player.get()
        self.tiles = []
        self.winFrame.pack_forget()
        if x_player and o_player and x_player != o_player:
            self.mainFrame.forget()
            for i in range(3):
                for j in range(3):
                    tile = Tile(self.gameFrame, self.check_winner, self.get_current_player)
                    tile.grid(row=i, column=j)
                    self.tiles.append(tile)
        self.gameFrame.pack(padx=10, pady=10)

    def check_winner(self):
        for x, y, z in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [1, 4, 7], [2, 5, 8], [0, 3, 6], [2, 4, 6], [0, 4, 8]]:
            if self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'X':
                self.show_winner(self.x_player.get())
            elif self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'O':
                self.show_winner(self.o_player.get())
        self.toggle_player()

    def toggle_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def show_winner(self, player):
        self.winFrame.pack(padx=10, pady=10)
        self.winner.set(player + "\nWins!")

    def get_current_player(self):
        return self.current_player


if __name__ == '__main__':
    root = Tk()
    Main(root)
    root.mainloop()
