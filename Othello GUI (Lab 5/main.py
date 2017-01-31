#Kevin Luu 48783106 Lab Section 3
import tkinter
import logic
import options

class GUI():
    def __init__(self, rows, columns, first, topLeft, gtype):
        self.dimx = 800 // rows
        self.dimy = 800 // columns
        self.main = tkinter.Tk()
        self.canvas_setup()
        self.grid()
        
    def canvas_setup(self):
        self.window = tkinter.Canvas(self.main, bg = "grey", width=800, height = 800)
        self.header = tkinter.Canvas(self.main, bg = "grey", width = 800, height = 100)
        self.first_header = self.header.create_text(400,50, text="Welcome to Reversi", fill="black")
        if main_game.first_move == "black":
            self.first_header = self.header.create_text(400,70, text="Black's to move.", fill="black")
        elif main_game.first_move == "white":
            self.first_header = self.header.create_text(400,10, text="White to move.", fill="white")
        self.second_header = self.header.create_text(400,90, text="White: 2, Black: 2", fill = "black")
        self.header.pack()
        self.window.bind("<Button-1>", self.when_playerClicks)
        

    def grid(self):
        main_game.draw_board()
        main_game.board_settings()
        for i in range(1, main_game.rows):
            line = self.window.create_line(0, self.dimx * i, 800, self.dimx * i)
        for i in range(1, main_game.columns):
            line = self.window.create_line(self.dimy * i, 0, self.dimy * i, 800)


    def when_playerClicks(self, event):       
        xcord = event.x // self.dimx
        ycord = event.y // self.dimy
        if len(main_game.flipped_pieces(xcord, ycord, main_game.turn))!= 0:
            main_game.player_move(xcord, ycord, main_game.turn)
            main_game.turn *= -1
        self.draw_pieces()
        main_game.player_score(main_game.rows, main_game.columns)
        self.header.delete(self.second_header)
        self.second_header = self.header.create_text(400,90, text = "White Score: " + str(main_game.white_score) + ", Black Score: " + str(main_game.black_score), fill = "black")
        if (main_game.player_go(main_game.turn, main_game.rows, main_game.columns) == False):
            main_game.turn *= -1
        elif main_game.game_over(main_game.white_score, main_game.black_score) == True:
            self.header.delete(self.first_header)
            self.first_header = self.header.create_text(400,70, text = "Game has ended. " + main_game.print_mesage(), fill = "black")
        self.whos_turn()
        self.draw_pieces()

  
    def print_ovals(self, x, y, tile):
        a = self.dimx 
        b = self.dimy
        c = abs(main_game.rows - main_game.columns)/2
        if tile == 1:
            new_oval = "white"
        elif tile == -1:
            new_oval = "black"
        if main_game.rows < main_game.columns:
            oval = self.window.create_oval((((x + c)*b),((y - (c))*a),((x + c + 1))*b ),((y - c + 1)*a),fill = new_oval)
        elif main_game.rows > main_game.columns:
            oval = self.window.create_oval(((x - c)*b),((y + c)*a),((x - c + 1) * b),((y + c + 1)*a),fill = new_oval)
        else:
            oval = self.window.create_oval(x* a, y * b, (x + 1) * a,(y + 1) * b, fill = new_oval)


    def whos_turn(self):
            if (main_game.turn == 1):
                self.header.delete(self.first_header)
                self.first_header = self.header.create_text(400, 70, text ="White Piece To Move.", fill = "white")
            elif (main_game.turn == -1):
                self.header.delete(self.first_header)
                self.first_header = self.header.create_text(400, 70, text ="Black Piece To Move.", fill = "black")


                
    def draw_pieces(self):
        for a in range(main_game.rows):
            for b in range(main_game.columns):
                if (main_game.board[a][b] != 0):
                    self.print_ovals(a, b, main_game.board[a][b])    
                            



if __name__ == '__main__':
    begin = options.GameOptions()
    begin.start()
    main_game = logic.LOGIC(int(begin.return_rows()), int(begin.return_columns()), begin.return_firstMove(),
                begin.return_topLeft(), begin.return_gameType())
    visual = GUI(int(begin.return_rows()), int(begin.return_columns()), begin.return_firstMove(),
                begin.return_topLeft(), begin.return_gameType())
    GUI.draw_pieces(visual)
    visual.window.pack()
    visual.main.mainloop()
