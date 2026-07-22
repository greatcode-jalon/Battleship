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

def printboard(board): #Help from Michael Do
    for row in board:
        print()
        for number in row:
            print(number, end="\t")
    print()


if __name__ == "__main__":
    listforplayerships = []
    listforcomputerships = []
    shipLocationCoordinatesList = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWUXYZ"
    computershipssunk = 0
    playershipssunk = 0
    manualList = []
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

    print("\n--- PLAYER BOARD ---")
    printboard(playerGameBoard)

    if gridSizeQuestion == 4:
        letters = ["A", "B", "C", "D"]
        numbers = [1, 2, 3, 4]
    elif gridSizeQuestion == 5:
        letters = ["A", "B", "C", "D", "E"]
        numbers = [1, 2, 3, 4, 5]
    elif gridSizeQuestion == 6:
        letters = ["A", "B", "C", "D", "E", "F"]
        numbers = [1, 2, 3, 4, 5, 6]
    elif gridSizeQuestion == 7:
        letters = ["A", "B", "C", "D", "E", "F", "G",]
        numbers = [1, 2, 3, 4, 5, 6, 7]
    elif gridSizeQuestion == 8:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H",]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    elif gridSizeQuestion == 9:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    elif gridSizeQuestion == 10:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    generatedColumn = random.randint(0,(gridSizeQuestion - 1))
    generatedRow = random.randint(0,(gridSizeQuestion - 1))

    numships = gridSizeQuestion // 2

    for x in range(numships):
        while True:
            placementoption = input("\nWould you rather place your ships randomly or manually? ").lower().strip()
            if placementoption == "randomly" or placementoption == "manually":
                break
            print("Please reinput randomly or manually. ")


        if placementoption == "manually":
            while True:
                shipplacement = input("Where would you like to place your ship (ex. A3 rows | columns): ").upper().strip()
                if len(shipplacement) == 3 and int(shipplacement[1]) == 1 and int(shipplacement[2]) == 0:
                    length = 3
                else:
                    length = 2
                
                if shipplacement in manualList:
                    print("This spot is occupied, please pick another. ")
                    continue

                elif len(shipplacement) == length and shipplacement[0] in letters and int(shipplacement[1]) in numbers:
                    letterchangerrows = {"A" : 0 , "B" : 1 , "C" : 2 , "D" : 3 , "E" : 4 , "F" : 5 , "G" : 6 , "H" : 7 , "I" : 8 , "J" : 9}
                    rowchanger = letterchangerrows[shipplacement[0]]
                    columnchanger = (int(shipplacement[1:]) - 1)
                    manualList.append(shipplacement)
                    print(manualList)
                    break

                else:
                    print("Please retry with the proper format. ")
                    continue

            rowplacement = shipplacement[0]
            colplacement = shipplacement[1:]
            rowind = alphabet.index(rowplacement)
            numcol = int(colplacement)
            colindex = numcol - 1
            playerGameBoard[rowind][colindex] = "X"
            print("\n--- PLAYER BOARD ---")
            printboard(playerGameBoard)


    for ship in range(numships):
        while True:
            generatedColumn = random.randint(0, (gridSizeQuestion - 1))
            generatedRow = random.randint(0, (gridSizeQuestion - 1))
            letter = alphabet[generatedRow]
            number = generatedColumn + 1
            coordinate = f"{letter}{number}"
            if coordinate not in listforcomputerships:
                listforcomputerships.append(coordinate)
                break

    print("\n--- GAME START ---")               
    playerguesslist = []
    computerguesslist = []
    computershipssunk = 0
    playershipssunk = 0
    
    while True:
        while True:
            playerGuess = input("\nEnter guess to hit a battleship letter for row and numbers for columns (ex. A3): ").upper().strip()
            if len(playerGuess) == 3 and int(playerGuess[1]) == 1 and int(playerGuess[2]) == 0:
                length = 3
            else:
                length = 2

            if len(playerGuess) == length and playerGuess[0] in letters and int(playerGuess[1:]) in numbers:
                letterchangerrows = {"A" : 0 , "B" : 1 , "C" : 2 , "D" : 3 , "E" : 4 , "F" : 5 , "G" : 6 , "H" : 7 , "I" : 8 , "J" : 9}
                rowchanger = letterchangerrows[playerGuess[0]]
                columnchanger = (int(playerGuess[1:]) - 1)
            else:
                print("CORRECT YOUR INPUT (EX. D3) ")
                continue

            if playerGuess in playerguesslist:
                print("PICK ANOTHER SPOT. ")
                continue
            else:
                playerguesslist.append(playerGuess)
                print(f"User's Guess: {playerGuess}")
                if playerGuess in listforcomputerships:
                    print("YOU HAVE SUNK A SHIP. ")
                    computerGameBoard[rowchanger][columnchanger] = "H"
                    computershipssunk += 1
                    print("\n--- PLAYER BOARD ---")
                    printboard(playerGameBoard)
                    print("\n--- COMPUTER BOARD ---")
                    printboard(computerGameBoard)
                    break
                else:
                    print("YOU MISSED TRY AGAIN.\n")
                    computerGameBoard[rowchanger][columnchanger] = "M"
                    print("\n--- PLAYER BOARD ---")
                    printboard(playerGameBoard)
                    print("\n--- COMPUTER BOARD ---")
                    printboard(computerGameBoard)
                    break

        if computershipssunk == numships:
            break

        while True:
            rowindc = random.randint(0, gridSizeQuestion - 1)
            colindc = random.randint(0, gridSizeQuestion - 1)
            computerletter = alphabet[rowindc]
            numcomputer = colindc + 1
            computerGuess = f"{computerletter}{numcomputer}"

            if computerGuess not in computerguesslist:
                computerguesslist.append(computerGuess)
                print(f"\nComputer's Guess: {computerGuess}")
                
                if computerGuess in listforplayerships:
                    print("CPU: HIT AND SUNK YOUR SHIP!! ")
                    playerGameBoard[rowindc][colindc] = "H"
                    playershipssunk += 1
                    print("\n--- PLAYER BOARD ---")
                    printboard(playerGameBoard)
                    break
                else:
                    print("CPU: MISSED \n")
                    playerGameBoard[rowindc][colindc] = "M"
                    print("\n--- PLAYER BOARD ---")
                    printboard(playerGameBoard)
                    break
                    
        if playershipssunk == numships:
            break

        if len(playerguesslist) == 5 and len(computerguesslist) == 5:
            break
                
    if playershipssunk == numships:
        print(f"\nTHE CPU HAVE WON THE GAME!! CPU SUNK ALL {numships} ships. ")

    elif computershipssunk == numships:
        print(f"\nYOU HAVE WON THE GAME!! YOU SUNK ALL {numships} ships. ")

    else:
        print("\nNO MORE GUESSES")