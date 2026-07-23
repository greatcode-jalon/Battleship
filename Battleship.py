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

    letters = []
    numbers = []

    for num in range(gridSizeQuestion): 
        letters.append(chr(65 + num))

    for num in range(1, gridSizeQuestion + 1):
        numbers.append(str(num))


    playerPossibleShipsList = [None, "dinghy", "destroyer"]
    playerShipCounter = 0
    playerStartCoordinatesList = []
    playerShipNamesList = []


    for ship in range(2):
        playerShipName = playerPossibleShipsList[playerShipCounter]
        playerShipCounter += 1
        playerDestroyerCoordinate = []


        if playerShipCounter == 1:
            playerGeneratedColumn = random.randint(0,(gridSizeQuestion - 1))
            playerGeneratedRow = random.randint(0,(gridSizeQuestion - 1))
            playerDinghyStartCoordinate = []
            playerDinghyStartCoordinate.append(playerGeneratedRow)
            playerDinghyStartCoordinate.append(playerGeneratedColumn)
            playerStartCoordinatesList.append(playerDinghyStartCoordinate)
            playerShipNamesList.append("dinghy")

        elif playerShipCounter == 2:
                horizontalOrVerticle = random.randint(0, 1)
                horitontal = 0
                verticle = 1
                if horizontalOrVerticle == horitontal:
                    playerGeneratedColumn = random.randint(0,(gridSizeQuestion - 1))
                    playerGeneratedRow = random.randint(0,(gridSizeQuestion - 2))

                elif horizontalOrVerticle == verticle:
                    playerGeneratedColumn = random.randint(0,(gridSizeQuestion - 2))
                    playerGeneratedRow = random.randint(0,(gridSizeQuestion - 1))

                for x in range(2):
                    playerStartCoordinate = []
                    if horizontalOrVerticle == horitontal:
                        playerStartCoordinate.append(playerGeneratedRow + x)
                        playerStartCoordinate.append(playerGeneratedColumn)

                    elif horizontalOrVerticle == verticle:
                        playerStartCoordinate.append(playerGeneratedRow)
                        playerStartCoordinate.append(playerGeneratedColumn + x)
                    playerDestroyerCoordinate.append(playerStartCoordinate)
                playerShipNamesList.append("destroyer")
                playerStartCoordinatesList.append(playerDestroyerCoordinate)

    print(playerStartCoordinatesList)
    print(playerShipNamesList)


    if playerGameBoard[playerStartCoordinatesList[0][0]][playerStartCoordinatesList[0][1]] == 0:
        playerGameBoard[playerStartCoordinatesList[0][0]][playerStartCoordinatesList[0][1]] = "X"
        letter = chr(65 + playerStartCoordinatesList[0][0])
        number = playerStartCoordinatesList[0][1] + 1
        playerCoordinate = f"{letter}{number}"
        playerShipLocationCoordinatesList.append(playerCoordinate)
        print(f"\nPlayer dignhy was placed at {playerCoordinate}")

    if playerGameBoard[playerStartCoordinatesList[1][0][0]][playerStartCoordinatesList[1][0][1]] == 0 and playerGameBoard[playerStartCoordinatesList[1][1][0]][playerStartCoordinatesList[1][1][1]] == 0:
        playerGameBoard[playerStartCoordinatesList[1][0][0]][playerStartCoordinatesList[1][0][1]] = "X"
        playerGameBoard[playerStartCoordinatesList[1][1][0]][playerStartCoordinatesList[1][1][1]] = "X"
        letter1 = chr(65 + playerStartCoordinatesList[1][0][0])
        number1 = playerStartCoordinatesList[1][0][1] + 1
        letter2 = chr(65 + playerStartCoordinatesList[1][1][0])
        number2 = playerStartCoordinatesList[1][1][1] + 1
        playerCoordinate1 = f"{letter1}{number1}"
        playerCoordinate2 = f"{letter2}{number2}"
        playerShipLocationCoordinatesList.append(playerCoordinate1)
        playerShipLocationCoordinatesList.append(playerCoordinate2)
        print(f"\nPlayer destroyer was placed at {playerCoordinate1} and {playerCoordinate2}")



    computerPossibleShipsList = [None, "dinghy", "destroyer"]
    computerShipCounter = 0
    computerStartCoordinatesList = []
    computerShipNamesList = []


    for ship in range(2):
        computerShipName = computerPossibleShipsList[computerShipCounter]
        computerShipCounter += 1
        computerDestroyerCoordinate = []


        if computerShipCounter == 1:
            computerGeneratedColumn = random.randint(0,(gridSizeQuestion - 1))
            computerGeneratedRow = random.randint(0,(gridSizeQuestion - 1))
            computerDinghyStartCoordinate = []
            computerDinghyStartCoordinate.append(computerGeneratedRow)
            computerDinghyStartCoordinate.append(computerGeneratedColumn)
            computerStartCoordinatesList.append(computerDinghyStartCoordinate)
            computerShipNamesList.append("dinghy")

        elif computerShipCounter == 2:
                horizontalOrVerticle = random.randint(0, 1)
                horitontal = 0
                verticle = 1
                if horizontalOrVerticle == horitontal:
                    computerGeneratedColumn = random.randint(0,(gridSizeQuestion - 1))
                    computerGeneratedRow = random.randint(0,(gridSizeQuestion - 2))

                elif horizontalOrVerticle == verticle:
                    computerGeneratedColumn = random.randint(0,(gridSizeQuestion - 2))
                    computerGeneratedRow = random.randint(0,(gridSizeQuestion - 1))

                for x in range(2):
                    computerStartCoordinate = []
                    if horizontalOrVerticle == horitontal:
                        computerStartCoordinate.append(computerGeneratedRow + x)
                        computerStartCoordinate.append(computerGeneratedColumn)

                    elif horizontalOrVerticle == verticle:
                        computerStartCoordinate.append(computerGeneratedRow)
                        computerStartCoordinate.append(computerGeneratedColumn + x)
                    computerDestroyerCoordinate.append(computerStartCoordinate)
                computerShipNamesList.append("destroyer")
                computerStartCoordinatesList.append(computerDestroyerCoordinate)

    print(computerStartCoordinatesList)
    print(computerShipNamesList)


    if computerGameBoard[computerStartCoordinatesList[0][0]][computerStartCoordinatesList[0][1]] == 0:
        computerGameBoard[computerStartCoordinatesList[0][0]][computerStartCoordinatesList[0][1]] = "X"
        letter = chr(65 + computerStartCoordinatesList[0][0])
        number = computerStartCoordinatesList[0][1] + 1
        computerCoordinate = f"{letter}{number}"
        computerShipLocationCoordinatesList.append(computerCoordinate)
        print(f"\nComputer dignhy was placed at {computerCoordinate}")

    if computerGameBoard[computerStartCoordinatesList[1][0][0]][computerStartCoordinatesList[1][0][1]] == 0 and computerGameBoard[computerStartCoordinatesList[1][1][0]][computerStartCoordinatesList[1][1][1]] == 0:
        computerGameBoard[computerStartCoordinatesList[1][0][0]][computerStartCoordinatesList[1][0][1]] = "X"
        computerGameBoard[computerStartCoordinatesList[1][1][0]][computerStartCoordinatesList[1][1][1]] = "X"
        letter1 = chr(65 + computerStartCoordinatesList[1][0][0])
        number1 = computerStartCoordinatesList[1][0][1] + 1
        letter2 = chr(65 + computerStartCoordinatesList[1][1][0])
        number2 = computerStartCoordinatesList[1][1][1] + 1
        computerCoordinate1 = f"{letter1}{number1}"
        computerCoordinate2 = f"{letter2}{number2}"
        computerShipLocationCoordinatesList.append(computerCoordinate1)
        computerShipLocationCoordinatesList.append(computerCoordinate2)
        print(f"\nComputer destroyer was placed at {computerCoordinate1} and {computerCoordinate2}")


    print("\n== PLAYER BOARD ==")
    printboard(playerGameBoard)
    print("\n== COMPUTER BOARD ==")
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
                if playerGuess == computerShipLocationCoordinatesList[0]:
                    print("YOU HIT & SUNK THE COMPUTER DINGHY.\n")
                    computerGameBoard[playerRowchanger][playerColumnchanger] = "H"
                    print("--- COMPUTER BOARD ---")
                    printboard(computerGameBoard)
                elif playerGuess in computerShipLocationCoordinatesList[1]:
                    if playerGuess == computerShipLocationCoordinatesList[1][0] or playerGuess == computerShipLocationCoordinatesList[1][1]:
                        print("YOU HIT THE COMPUTER DESTROYER.\n")
                    if playerGuess == computerShipLocationCoordinatesList[1][0] and playerGuess == computerShipLocationCoordinatesList[1][1]:
                        print("YOU SUNK THE COMPUTER DESTROYER.\n")
                        continue
                if playerGuess == computerShipLocationCoordinatesList[1][0] and playerGuess == computerShipLocationCoordinatesList[1][1] and playerGuess == computerShipLocationCoordinatesList[0]:
                    print("You have sunk all ships. YOU WIN!")
                    break
                else:
                    continue

            elif playerGuess not in computerShipLocationCoordinatesList:
                print("YOU MISSED TRY AGAIN.\n")
                computerGameBoard[playerRowchanger][playerColumnchanger] = "M"
                print("--- COMPUTER BOARD ---")
                printboard(computerGameBoard)

            if computerGuess in playerShipLocationCoordinatesList:
                if computerGuess == playerShipLocationCoordinatesList[0]:
                    print("THE CPU HIT & SUNK YOUR DINGHY.\n")
                    computerGameBoard[playerRowchanger][playerColumnchanger] = "H"
                    print("--- COMPUTER BOARD ---")
                    printboard(computerGameBoard)
                elif computerGuess in playerShipLocationCoordinatesList[1]:
                    if computerGuess == playerShipLocationCoordinatesList[1][0] or computerGuess == playerShipLocationCoordinatesList[1][1]:
                        print("THE CPU HIT YOUR DESTROYER.\n")
                    if computerGuess == playerShipLocationCoordinatesList[1][0] and computerGuess == playerShipLocationCoordinatesList[1][1]:
                        print("THE CPU SUNK YOUR DESTROYER.\n")
                        continue
                if computerGuess == playerShipLocationCoordinatesList[1][0] and computerGuess == playerShipLocationCoordinatesList[1][1] and computerGuess == playerShipLocationCoordinatesList[0]:
                    print("You have sunk all ships. YOU WIN!")
                    break
                else:
                    continue

            elif computerGuess not in playerShipLocationCoordinatesList:
                print("CPU: MISSED \n")
                playerGameBoard[computerGuessRow][computerGuessColumn] = "M"
                print("--- PLAYER BOARD ---")
                printboard(playerGameBoard)
                continue

        else:
            print("Please retry with the proper format. ")
            continue
        