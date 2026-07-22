#Names: Noah C + Ja'Lon S

import random

def createBoard():
    columnRow = []
    for column in range(gridSizeQuestion):
        boardRow = []
        columnRow.append(boardRow)
        for row in range(gridSizeQuestion):
            boardRow.append(0)
    return columnRow

def printboard(board):
    for row in board:
        print()
        for number in row:
            print(number, end="\t")
    print()

if __name__ == "__main__":
    playerShipLocationCoordinatesList = []
    computerShipLocationCoordinatesList = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWUXYZ"

    while True:
        try:
            gridSizeQuestion = int(input("Enter a number, 4-10, to define the size of the board (ex, 5 = 5x5 board): "))
            if gridSizeQuestion in range(4,11):
                break
            if gridSizeQuestion not in range(4,11):
                print("Please enter your board dimensions with a number 4-10. ")
                continue
        except:
            print("Please enter a number 4-10.")
            continue

    playerGameBoard = createBoard()
    computerGameBoard = createBoard()

    printboard(playerGameBoard)

    if gridSizeQuestion == 4:
        letters = ["A", "B", "C", "D"]
        numbers = ['1', '2', '3', '4']
    elif gridSizeQuestion == 5:
        letters = ["A", "B", "C", "D", "E"]
        numbers = ['1', '2', '3', '4', '5']
    elif gridSizeQuestion == 6:
        letters = ["A", "B", "C", "D", "E", "F"]
        numbers = ['1', '2', '3', '4', '5', '6']
    elif gridSizeQuestion == 7:
        letters = ["A", "B", "C", "D", "E", "F", "G"]
        numbers = ['1', '2', '3', '4', '5', '6', '7']
    elif gridSizeQuestion == 8:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    elif gridSizeQuestion == 9:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    elif gridSizeQuestion == 10:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    playerGeneratedColumn = random.randint(0,(gridSizeQuestion - 1))
    playerGeneratedRow = random.randint(0,(gridSizeQuestion - 1))

    if playerGameBoard[playerGeneratedRow][playerGeneratedColumn] == 0:
        playerGameBoard[playerGeneratedRow][playerGeneratedColumn] = "X"
        letter = alphabet[playerGeneratedRow]
        number = playerGeneratedColumn + 1
        playerCoordinate = f"{letter}{number}"
        playerShipLocationCoordinatesList.append(playerCoordinate)
        print(f"\nYour ship was placed at {playerCoordinate}")
        print("== PLAYER BOARD ==")
        printboard(playerGameBoard)

    computerGeneratedColumn = random.randint(0,(gridSizeQuestion - 1))
    computerGeneratedRow = random.randint(0,(gridSizeQuestion - 1))

    if computerGameBoard[computerGeneratedRow][computerGeneratedColumn] == 0:
        computerGameBoard[computerGeneratedRow][computerGeneratedColumn] = "X"
        letter = alphabet[computerGeneratedRow]
        number = computerGeneratedColumn + 1
        computerCoordinate = f"{letter}{number}"
        computerShipLocationCoordinatesList.append(computerCoordinate)
        print(f"\nComputer ship was placed at {computerCoordinate}") #this is only for checking but wil need to be removed later
        print("== COMPUTER BOARD ==")
        printboard(computerGameBoard)

    playerGuesslist = []
    computerGuesslist = []

    while True:
        playerGuess = input("\nEnter guess to hit a battleship letter for row and numbers for columns (ex. A3): ").upper().strip()
        if len(playerGuess) == 3 and int(playerGuess[1]) == 1 and int(playerGuess[2]) == 0:
            length = 3
        else:
            length = 2

        if playerGuess in playerGuesslist:
            printboard

        if len(playerGuess) == length and playerGuess[0] in letters and str(playerGuess[1:]) in numbers:
            letterchangerrows = {"A" : 0 , "B" : 1 , "C" : 2 , "D" : 3 , "E" : 4 , "F" : 5 , "G" : 6 , "H" : 7 , "I" : 8 , "J" : 9}
            playerRowchanger = letterchangerrows[playerGuess[0]]
            playerColumnchanger = (int(playerGuess[1:]) - 1)
        
            if playerGuess in playerGuesslist:
                print("PICK ANOTHER SPOT. ")
                continue

            playerGuesslist.append(playerGuess)

            while True:
                computerGuessColumn = random.randint(0,(gridSizeQuestion - 1))
                computerGuessRow = random.randint(0,(gridSizeQuestion - 1))
                computerGuess = f"{letters[computerGuessRow]}{computerGuessColumn + 1}"
                if computerGuess in computerGuesslist:
                    continue 
                elif computerGuess not in computerGuesslist:
                    computerGuesslist.append(computerGuess)
                    break


            if playerGuess in computerShipLocationCoordinatesList:
                print("YOU HAVE SUNK A SHIP.\n")
                computerGameBoard[playerRowchanger][playerColumnchanger] = "H"
                print("--- COMPUTER BOARD ---")
                printboard(computerGameBoard)
                break 

            elif playerGuess not in computerShipLocationCoordinatesList:
                print("YOU MISSED TRY AGAIN.\n")
                computerGameBoard[playerRowchanger][playerColumnchanger] = "M"
                print("--- COMPUTER BOARD ---")
                printboard(computerGameBoard)

            if computerGuess in playerShipLocationCoordinatesList:
                print("CPU: HIT AND SUNK YOUR SHIP!!\n")
                playerGameBoard[computerGuessRow][computerGuessColumn] = "H"
                print("--- PLAYER BOARD ---")
                printboard(playerGameBoard)
                break

            elif computerGuess not in playerShipLocationCoordinatesList:
                print("CPU: MISSED \n")
                playerGameBoard[computerGuessRow][computerGuessColumn] = "M"
                print("--- PLAYER BOARD ---")
                printboard(playerGameBoard)
                continue

        else:
            print("Please retry with the proper format. ")
            continue
