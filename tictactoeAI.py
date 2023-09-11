board = { 1: " ", 2: " ", 3: " ",
          4: " ", 5: " ", 6: " ",
          7: " ", 8: " ", 9: " "}
player = "O"
computer = "X"


def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def spaceisFree(position):
    if board[position] == " ":
        return True
    return False

def insertLetter(letter, position):
    if spaceisFree(position):
        board[position] = letter
        printBoard(board)
        if checkdraw():
            print("Draw")
            exit()
        if checkwin():
            if letter == "X":
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("Position already taken/n")
        position = int(input("Please enter new position. "))
        insertLetter(letter, position)
        return
def checkwin(): 
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
    
def checkwhichmarkwon(mark):
 if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
 elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
 elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
 elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
 elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
 elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
 elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
 elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
 else:
        return False

def checkdraw():
    for key in board.keys():
        if board[key] == " ":
            return False
    return True

def playermove():
    position = int(input("Enter a position for 'O' "))
    insertLetter(player, position)
    return

def computermove():
    
    bestscore = -800
    bestmove = 0
    for key in board.keys():
        if board[key] == " ":
            board[key] = computer
            score = minimax(board, False)
            board[key] = " "
            if score > bestscore:
              bestscore = score
              bestmove = key
    insertLetter(computer, bestmove)
    return

def minimax(board, isMaximizing):
    if checkwhichmarkwon(computer):
        return 1
    elif checkwhichmarkwon(player):
        return -1
    elif checkdraw():
        return 0
    
    if isMaximizing:
        bestscore = -800
        for key in board.keys():
            if board[key] == " ":
                board[key] = computer
                score = minimax(board, False)
                board[key] = " "
                if score > bestscore:
                    bestscore = score
        return bestscore 
    else:
        bestscore = 800
        for key in board.keys():
            if board[key] == " ":
                board[key] = player
                score = minimax(board, True)
                board[key] = " "
                if score < bestscore:
                    bestscore = score
        return bestscore 
    

while not checkwin():
    computermove()
    playermove()