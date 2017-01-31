# Derek Edrich (343637846) and Kevin Luu (48783106)

import connectfour

def playerMove(game_state):
    '''has the client player make a move'''
    printBoard(game_state)
    while(True):
        playermode = input("Move Mode: ('drop' or 'pop')")
        if(playermode == 'drop'):
            playerinput = input("Column:")
            trialstate = None
            try:
                trialstate = connectfour.drop_piece(game_state, int(playerinput)-1)
            except ValueError:
                print("Invalid Column Number.")
            except connectfour.InvalidConnectFourMoveError:
                print("Column is full.")
            else:
                return trialstate
        elif(playermode == 'pop'):
            playerinput = input("Column:")
            trialstate = None
            try:
                trialstate = connectfour.pop_piece(game_state, int(playerinput)-1)
            except ValueError:
                 print("Invalid Column Number.")
            except connectfour.InvalidConnectFourMoveError:
                print("Cannot pop that column.")
            else:
                return trialstate
        else:
            print("Invalid move mode.")
        

def printBoard(game_state):
    '''prints game board to console'''
    result = [] #stored rows of strings
    for col in game_state.board:
        for row in range(len(col)):
            if(len(result) > row): #check if result has been instantiated yet
                result[row] = result[row] + formatSquare(col[row])
            else:
                result.append(formatSquare(col[row]))
    stringresult = ""
    stringresult = stringresult + getBoardTitle()
    for row in result:
        stringresult = stringresult + row + "\n"
    stringresult = stringresult + "It is " + game_state.turn + "'s turn\n"
    print(stringresult)

def formatSquare(boardString:str):
    '''formats a square for printing the board to the console'''
    if(boardString == connectfour.NONE):
        return ".  "
    else:
        return boardString + "  "

def getBoardTitle() ->str:
    '''returns the header of the board'''
    result = ""
    for i in range(connectfour.BOARD_COLUMNS):
        result = result + str(i+1) + "  "
    return result + "\n"

def checkWin(gameState) ->bool:
    '''checks if the game is complete'''
    return connectfour.winning_player(gameState) != connectfour.NONE

def win(gameState):
    '''finishes the game by displaying winner on console'''
    print("Player " + connectfour.winning_player(gameState) + " has won!")
    
if __name__ == '__main__':
    pass
