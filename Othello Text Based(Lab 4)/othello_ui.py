#Kevin Luu
#ID:48783106
# othello_ui

from othello_classes import *

##### USER INTERFACE #####

def user_interface():
    row = int(input('Rows: '))
    column = int(input('Columns: '))
    first_player = input('1st Player? (B or W): ').upper().strip()
    first_piece = input('Corner piece? (B or W): ').upper().strip()
    least_or_most = input('Gamestyle? (> or <): ').strip()
        
    game = GameState(first_player, str(least_or_most))
    game.center_four(row, column, first_piece)
    game.num_of_color()
    game.print_board()

    while True:
        player_move = _input_moves()
        move_down = int(player_move[0])
        move_right = int(player_move[1])
        game.make_move(move_down, move_right)
        
    

def _input_moves () -> 'list containing move coordinates':
    while True:
        try:
            moves = []
            player_move = input('Move: ').strip().split()
            for x in player_move:
                moves.append(int(x)-1)               
            return moves
        except:
            print('ERROR')





if __name__ == '__main__':
    user_interface()
