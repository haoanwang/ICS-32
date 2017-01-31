# Derek Edrich (343637846) and Kevin Luu (48783106)

import connectfour
import connectfoursharedcode

def playConsoleGame():
    '''plays a console-based game of connect 4'''
    gameState = connectfour.new_game_state()
    while(True):
        gameState = connectfoursharedcode.playerMove(gameState)
        if(connectfoursharedcode.checkWin(gameState)):
            connectfoursharedcode.win(gameState)
            break
if __name__ == '__main__':
    playConsoleGame()
