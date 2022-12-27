print("TIC TAC TOE Game")

##First Create a game board
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

boardkeys = []

for key in theBoard:
    boardkeys.append(key)


##print the board

def game_board(board):
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print("_+_+_")
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print("_+_+_")
    print(board['7'] + "|" + board['8'] + "|" + board['9'])


# implement the game logic
def game():
    turn = 'X'
    count = 0

    for i in range(9):
        game_board(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        #if input is greater than number of positions then give error
        if int(move) > 9:
            print("Invalid input! try Again.")
            continue

        #if location is empty then fill it otherwise give error.
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count = count + 1
        else:
            print("Place is already filled! try Again.")
            continue

        # check for  win conditions
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                game_board(theBoard)
                print("Game End.\n" + turn + " has won the game.")
                print("here 1")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                game_board(theBoard)
                print("Game End.\n" + turn + " has won the game.")
                print("here 2")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                game_board(theBoard)
                print("Game End.\n" + turn + " has won the game.")
                print("here 3")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                game_board(theBoard)
                print("Game End.\n" + turn + " has won the game.")
                print("here 4")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                game_board(theBoard)
                print("Game End.\n" + turn + " has won the game.")
                print("here 5")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                game_board(theBoard)
                print("Game End.\n" + turn + " has won the game.")
                print("here 6")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                game_board(theBoard)
                print("Game End.\n" + turn + " has won the game.")
                print("here 7")
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] !=  ' ':
                game_board(theBoard)
                print("Game End.\n" + turn + " has won the game.")
                print("here 8")
                break

        #if no. of attempts increases than 9 then give error
        if count == 9:
            game_board(theBoard)
            print("Game End. Its a Tie.")

        #changing the turns
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    #restart the game
    Restart = input("Do you want to restart the game ? y/n : ")
    if Restart == 'Y' or Restart == 'y':
        for key in boardkeys:
            theBoard[key] = " "
        game()

#main
if __name__ == "__main__":
    game()
