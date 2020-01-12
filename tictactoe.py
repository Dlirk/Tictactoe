import re
E=' '

player1_char = 'X'
player2_char = 'O'

row1 = [E,E,E]
row2 = [E,E,E]
row3 = [E,E,E]

def player_move_check(player_move, player_char):

    if player_move == ('0,0') and row3[0] == E:
        row3[0] = player_char

    if player_move == ('1,0') and row3[1] == E:
        row3[1] = player_char

    if player_move == ('2,0') and row3[2] == E:
        row3[2] = player_char


    if player_move == ('0,1') and row2[0] == E:
        row2[0] = player_char

    if player_move == ('1,1') and row2[1] == E:
        row2[1] = player_char

    if player_move == ('2,1') and row2[2] == E:
        row2[2] = player_char


    if player_move == ('0,2') and row1[0] == E:
        row1[0] = player_char

    if player_move == ('1,2') and row1[1] == E:
        row1[1] = player_char

    if player_move == ('2,2') and row1[2] == E:
        row1[2] = player_char
        
    print(row1)
    print(row2)
    print(row3)
    
def check_win():

    #PLAYER1 VICTORY CONDITIONS
    if row1[0] == 'X' and row1[1] == 'X' and row1[2] == 'X':
        return True

    if row2[0] == 'X' and row2[1] == 'X' and row2[2] == 'X':
        return True
        print('PLAYER1 WON!')

    if row3[0] == 'X' and row3[1] == 'X' and row3[2] == 'X':
        return True

    if row3[0] == 'X' and row2[1] == 'X' and row1[2] == 'X':
        return True

    if row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X':
        return True

    if row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X':
        return True

    if row1[1] == 'X' and row2[1] == 'X' and row3[1] == 'X':
        return True

    if row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X':
        return True

    #PLAYER 2 VICTORY CONDITIONS

    if row1[0] == 'O' and row1[1] == 'O' and row1[2] == 'O':
        return True

    if row2[0] == 'O' and row2[1] == 'O' and row2[2] == 'O':
        return True

    if row3[0] == 'O' and row3[1] == 'O' and row3[2] == 'O':
        return True

    if row3[0] == 'O' and row2[1] == 'O' and row1[2] == 'O':
        return True

    if row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O':
        return True

    if row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O':
        return True

    if row1[1] == 'O' and row2[1] == 'O' and row3[1] == 'O':
        return True

    if row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O':
        return True
        
def player1_move():
    player1 = input('PLAYER1 MOVE: ')
    player_move_check(player1, player1_char)

def player2_move():
    player2 = input('PLAYER2 MOVE: ')
    player_move_check(player2, player2_char)

while True:
    
    player1_move()
    if check_win() == True:
        print('PLAYER1 WON!')
        break
    
    player2_move()

    if check_win() == True:
        print('PLAYER2 WON!')
        break

print('GAME OVER')
