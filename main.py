from helpers import draw_board, check_turn, check_for_win
import os
from dataclasses import dataclass

@dataclass
class Game:
    spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    playing = True
    complete = False
    turn = 0
    prev_turn = -1
    score = {"X": 0, "O": 0, "Tie": 0}

while Game.playing:
    os.system("cls" if os.name == "nt" else "clear")
    draw_board(Game.spots)

    # if prev_turn == turn, that means the player has not made a valid move
    if Game.prev_turn == Game.turn:
        print("Invalid move, try again")
    Game.prev_turn = Game.turn
    print("It is {}'s turn.".format(check_turn(Game.turn)))

    choice = input("Choose a spot: ")
    if choice == "q":
        print("Thanks for playing!")
        Game.playing = False
    elif str.isdigit(choice) and int(choice) in Game.spots:
        print("You chose spot {}".format(choice))
        if not Game.spots[int(choice)] in {"X", "O"}:

            Game.turn += 1
            Game.spots[int(choice)] = check_turn(Game.turn)
    if check_for_win(Game.spots): Game.playing, Game.complete = False, True
    # if complete == True ask the user to continue playing
    # if the user wants to continue playing, reset the board and continue the game
    # else, print the final score and exit the game
    if Game.complete == True:
        os.system("cls" if os.name == "nt" else "clear")
        draw_board(Game.spots)
        print("Game over!")
        print("The winner is {}!".format(check_turn(Game.turn)))
        Game.score[check_turn(Game.turn)] += 1
        print("Score: X: {} O: {} Tie: {}".format(Game.score["X"], Game.score["O"], Game.score["Tie"]))
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            Game.spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
            Game.turn = 0
            Game.prev_turn = -1
            Game.playing = True
            Game.complete = False
        else: 
            Game.complete = True
            print("Thanks for playing!")

os.system("cls" if os.name == "nt" else "clear")
draw_board(Game.spots)



print("Score: X: {} O: {}".format(Game.score["X"], Game.score["O"]))
print("Thanks for playing!")
