def draw_board(spots):
    board = """
    {} | {} | {}
    ---------
    {} | {} | {}
    ---------
    {} | {} | {}
    """.format(spots[1], spots[2], spots[3], spots[4], spots[5], spots[6], spots[7], spots[8], spots[9])
    print(board)
    return board

def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"
def check_for_win(spots):
    # horizontal win
    if spots[1] == spots[2] == spots[3]:
        return True
    elif spots[4] == spots[5] == spots[6]:
        return True
    elif spots[7] == spots[8] == spots[9]:
        return True
    # vertical win
    elif spots[1] == spots[4] == spots[7]:
        return True
    elif spots[2] == spots[5] == spots[8]:
        return True
    elif spots[3] == spots[6] == spots[9]:
        return True
    # diagonal win
    elif spots[1] == spots[5] == spots[9]:
        return True
    elif spots[3] == spots[5] == spots[7]:
        return True
    else:
        return False
def continue_game(playing):
    # if the player wants to continue the game
    return True
    # else
    return False
    pass