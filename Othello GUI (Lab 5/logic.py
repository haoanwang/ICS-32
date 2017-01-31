#Kevin Luu 48783106 Lab Section 3
class LOGIC():
    def __init__(self, rows, columns, first_move, top_left, game_type):
        self.board = []
        self.rows = rows
        self.columns = columns
        self.white_score = 0
        self.black_score = 0
        self.message = None
        self.first_move = first_move
        self.top_left = top_left
        self.game_type = game_type
        
        
    def draw_board(self):
        if self.first_move == "black" :
            self.turn = -1
        elif self.first_move == "white":
            self.turn = 1
        for x in range(int(self.rows)):
            self.board.append([])
            for y in range(int(self.columns)):
                self.board[x].append(int(0))
                
    def board_settings(self):
        r = int(self.rows // 2)
        c = int(self.columns // 2)
        if self.top_left == "white":
            self.board[r - 1][c - 1] = 1
            self.board[r - 1][c] = -1
            self.board[r][c] = 1
            self.board[r][c - 1] = -1
        if self.top_left == "black":
            self.board[r - 1][c - 1] = -1
            self.board[r - 1][c] = 1
            self.board[r][c] = -1
            self.board[r][c - 1] = 1

        
    def valid_move(self, x, y)->bool:
        return (x <= (self.rows - 1) and x >= 0 and y <= (self.columns - 1) and y >= 0)

    
    def _checkDirection(self, x , y ,color)->list:
        eight_offsets = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        to_flip = []
        for offset in eight_offsets:
            to_flip.extend(self._one_direction(x, y, color, offset))
        return to_flip
    
    def _one_direction(self, xcoor, ycoor,color, direction_offset)->list:
        opposite_color = []
        for num in range(1, 17):
            if self.valid_move(xcoor + num * direction_offset[1], ycoor + num * direction_offset[0]):
                if self.board[xcoor + num * direction_offset[1]][ycoor + num * direction_offset[0]] == (-1 * color):
                    opposite_color.append(((xcoor + num * direction_offset[1]),(ycoor + num * direction_offset[0])))
                elif self.board[xcoor + num * direction_offset[1]][ycoor + num * direction_offset[0]] == color:
                    return opposite_color
                else:
                    return []
            else:
                return []

  
    def flipped_pieces(self, x, y, color)->list:
        flipped = []
        if (self.valid_move(x,y)):
            if (self.board[x][y] == 0):
                    flipped.extend(self._checkDirection(x, y, color))
        return flipped
                            

    def player_move(self, x, y, color):
        changed = self.flipped_pieces(x,y,color)
        self.board[x][y] = color
        for element in changed:
            self.board[element[0]][element[1]] *= -1

          
    def player_go(self, color, rows, columns)->bool:
        for x in range(rows):
            for y in range(columns):
                return (len(self.flipped_pieces(x, y, color)) == 0)
            
    
    def player_score(self, rows, columns):
        self.white_score = 0
        self.black_score = 0
        for x in range(self.rows):
            for y in range(self.columns):
                if self.board[x][y] == 1:
                    self.white_score += 1
                elif self.board[x][y] == -1:
                    self.black_score += 1
        
    def game_over(self, white_score, black_score)->bool:
            if (self.player_go(self.turn, self.rows, self.columns) == False):
                if self.game_type == "most":
                    if (black_score > white_score):
                        self.message = "Player with the black pieces wins."
                        return True
                    elif (white_score > black_score):
                        self.message = "Player with the white pieces win."
                        return True
                    elif white_score == black_score:
                        self.message = "No winner"
                        return True
                elif self.game_type == "least":
                    if (black_score < white_score):
                        self.message = "Player with the white pieces wins."
                        return True
                    elif (white_score > black_score):
                        self.message = "Player with the black pieces win."
                        return True
                    elif white_score == black_score:
                        self.message = "No winner"
                        return True
                return True
            return False
                   
    def print_message(self, message):
        return self.message


if __name__ == '__main__':
    pass



