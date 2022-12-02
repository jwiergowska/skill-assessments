# > 1. When the user selects "X", the computer ("O") plays two moves for every one move the user makes:

# I fixed this and instead of 'player', the code displays 'X' at the end of the code where the major bug was.

import random

def askForLetterr() -> list:
    """
    The function choses if player wants to be X or O. 
    
    :returns: a list with the player's letter as the first item and the computer's letter as the second.
    """
    letter = ''
    
    while not (letter == 'X' or letter == 'O'):
        print('X or O? ')
        letter = input().upper()

    # The first element is the player, the second is the computer.
    if letter == 'X':   
        return ['X', 'O']
    else:   
        return ['O', 'X']

def printBoard(board: list) -> None:
    """
    This function prints out the board.

    :board: list of strings representing the board (without index 0).
    """
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def printBoard(board: list) -> None:
    """
    This function prints out the board.

    :board: list of strings representing the board (without index 0).
    """
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(b, l):
    """
    Given a board and a player's letter, this function returns True if that player won.
    
    :b: board
    :l: letter.
    """
    return ((b[7] == l and b[8] == l and b[9] == l) or # top
          (b[4] == l and b[5] == l and b[6] == l) or # middle
          (b[1] == l and b[2] == l and b[3] == l) or # bottoms
          (b[7] == l and b[4] == l and b[1] == l) or # left side
          (b[8] == l and b[5] == l and b[2] == l) or # middle
          (b[9] == l and b[6] == l and b[3] == l) or # right side
          (b[7] == l and b[5] == l and b[3] == l) or # diagonal
          (b[9] == l and b[5] == l and b[1] == l)) # diagonald

def copyBoard(board):
    """
    Making a copy of the board list and return it.
    """
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    """
    Returning True if the passed move is free on the passed board.
    """
    return board[move] == ' '

def getPlayerMove(board):
    """
    Leting the player enter their move.
    """
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMove(board, movesList):
    """
    Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move.
    """
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def isBoardFull(board):
    """
    Return True if every space on the board has been taken. Otherwise, return False.
    """
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def juliaAiBot(board, computerLetter):
    """
   Choosing which move is the most optial and playing till the game is finished. 
   Each time printing the board, also asking for a letter and asking if the player wants to play again.

   :board: given board
   :computerLetter: the letter which is attributed to computer.
    """
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is Julia's AI bot:
    # Checking, who can win in one move.
    for i in range(1, 10):
        boardCopy = copyBoard(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

   # Checking if the player could win in the next move, if so, block them.
    for i in range(1, 10):
        boardCopy = copyBoard(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Taking corners (if free).
    move = chooseRandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Taking the center (if free).
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMove(board, [2, 4, 6, 8])

while True:
    # Reset the board.
    ourBoard = [' '] * 10
    playerLetter, computerLetter = askForLetterr()
    turn = playerLetter
    if turn == "X":
        print('The player will go first.')
    else:
        print("Julia's AI will go first.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "X":
            # Player's turn
            printBoard(ourBoard)
            move = getPlayerMove(ourBoard)
            makeMove(ourBoard, playerLetter, move)

            if isWinner(ourBoard, playerLetter):
                printBoard(ourBoard)
                print('Yeah! You have won the game!')
                gameIsPlaying = False
                break
            else:
                if isBoardFull(ourBoard):
                    printBoard(ourBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
            if turn == 'player':
                # Player's turn
                printBoard(ourBoard)
                move = getPlayerMove(ourBoard)
                makeMove(ourBoard, playerLetter, move)

                if isWinner(ourBoard, playerLetter):
                    printBoard(ourBoard)
                    print('Yeah! You have won the game!')
                    gameIsPlaying = False
                    break
                else:
                    if isBoardFull(ourBoard):
                        printBoard(ourBoard)
                        print('The game is a tie!')
                        break
                    else:
                         turn = 'computer'
            else:
                # Computer's turn
                move = juliaAiBot(ourBoard, computerLetter)
                makeMove(ourBoard, computerLetter, move)

                if isWinner(ourBoard, computerLetter):
                    printBoard(ourBoard)
                    print("Julia's AI won.")
                    gameIsPlaying = False
                    break
                else:
                    if isBoardFull(ourBoard):
                        printBoard(ourBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'X'
        else:
            # Computer's turn
            move = juliaAiBot(ourBoard, computerLetter)
            makeMove(ourBoard, computerLetter, move)

            if isWinner(ourBoard, computerLetter):
                printBoard(ourBoard)
                print("Julia's AI won.")
                gameIsPlaying = False
                break
            else:
                if isBoardFull(ourBoard):
                    printBoard(ourBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
            if turn == 'player':
                # Player's turn
                printBoard(ourBoard)
                move = getPlayerMove(ourBoard)
                makeMove(ourBoard, playerLetter, move)

                if isWinner(ourBoard, playerLetter):
                    printBoard(ourBoard)
                    print('Yeah! You have won the game!')
                    gameIsPlaying = False
                    break
                else:
                    if isBoardFull(ourBoard):
                        printBoard(ourBoard)
                        print('The game is a tie!')
                        break
                    else:
                         turn = 'computer'
            else:
                # Computer's turn
                move = juliaAiBot(ourBoard, computerLetter)
                makeMove(ourBoard, computerLetter, move)

                if isWinner(ourBoard, computerLetter):
                    printBoard(ourBoard)
                    print("Julia's AI won.")
                    gameIsPlaying = False
                    break
                else:
                    if isBoardFull(ourBoard):
                        printBoard(ourBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

    print('Would you like to play again? (yes or no)') 
    if not input().lower().startswith('y'):
        break
        ```
