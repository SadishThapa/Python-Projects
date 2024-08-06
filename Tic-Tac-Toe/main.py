from utilities import draw_board, check_turn, check_win
import os

# dictionary used for spaces on board
spaces = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}
playing = True
finished = False
turn = 0
prev_turn = -1

while playing:

    # prints board
    os.system("cls" if os.name == "nt" else "clear")
    draw_board(spaces)

    # if turn does not increment, input was invalid
    if prev_turn == turn:
        print("Invalid space selected, select another space")

    prev_turn = turn
    print("It is Player " + str((turn % 2) + 1) + " turn, Select your spot or press q to quit")

    move = input()
    
    # checks if input was valid
    if move == "q":
        playing = False
    elif str.isdigit(move) and int(move) in spaces:
        if not spaces[int(move)] in {"O", "X"}:
            turn += 1
            spaces[int(move)] = check_turn(turn)

    # checks whether game ends with winner or tie
    if check_win(spaces):
        playing = False
        finished = True
    if turn > 8:
        playing = False

os.system("cls" if os.name == "nt" else "clear")
draw_board(spaces)

# prints winner or if there was a tie
if finished:
    if check_turn(turn) == "X":
        print("Player 1 Won")
    else:
        print("Player 2 Won")
else:
    print("There was no Winner")

print("Thanks for playing")