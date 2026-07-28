#Names: Noah C + Ja'Lon S

import random

def validation():
    while True:
        try:
            gridSizeQuestion = int(input("Enter a number, 4-10, to define the size of the board (ex, 5 = 5x5 board): "))
            if gridSizeQuestion in range(4,11):
                return gridSizeQuestion
            if gridSizeQuestion not in range(4,11):
                print("Please enter your board dimensions with a number 4-10. ")
                continue
        except:
            print("Please enter a number 4-10.")
            continue

def validatePlacement(compPlayGuess):
    




def createBoard(gridSizeQuestion):
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

def shipPlacement(gridSizeQuestion):
        shipCounter = 0
        startCoordinatesList = []
        shipNamesList = []

        while True:
            shipCounter = 0
            startCoordinatesList = []
            shipNamesList = []

            shipCounter += 1
            destroyerCoordinates = []

            generatedColumn = random.randint(0,(gridSizeQuestion - 1))
            generatedRow = random.randint(0,(gridSizeQuestion - 1))
            dinghyStartCoordinates = []
            dinghyStartCoordinates.append(generatedRow)
            dinghyStartCoordinates.append(generatedColumn)
            startCoordinatesList.append(dinghyStartCoordinates)
            shipNamesList.append("dinghy")

            shipCounter += 1
            
            horizontalOrVerticle = random.randint(0, 1)
            horitontal = 0
            verticle = 1
            if horizontalOrVerticle == horitontal:
                generatedColumn2 = random.randint(0,(gridSizeQuestion - 1))
                generatedRow2 = random.randint(0,(gridSizeQuestion - 2))
            elif horizontalOrVerticle == verticle:
                generatedColumn2 = random.randint(0,(gridSizeQuestion - 2))
                generatedRow2 = random.randint(0,(gridSizeQuestion - 1))

            for ship in range(2):
                startCoordinate = []
                if horizontalOrVerticle == horitontal:
                    startCoordinate.append(generatedRow2 + ship)
                    startCoordinate.append(generatedColumn2)
                elif horizontalOrVerticle == verticle:
                    startCoordinate.append(generatedRow2)
                    startCoordinate.append(generatedColumn2 + ship)
                destroyerCoordinates.append(startCoordinate)
            shipNamesList.append("destroyer")
            startCoordinatesList.append(destroyerCoordinates)

            overlap = False
            if dinghyStartCoordinates == destroyerCoordinates[0] or dinghyStartCoordinates == destroyerCoordinates[1]:
                overlap = True

            if overlap == False:
                break

        return startCoordinatesList

def win_checker(shipLocationCoordinatesList):
    for targetcoor in shipLocationCoordinatesList:
        if targetcoor != "M" and targetcoor != "H":
            return False
    return True




if __name__ == "__main__":
    playerShipLocationCoordinatesList = []
    computerShipLocationCoordinatesList = []

    gridSizeQuestion = validation()

    playerGameBoard = createBoard(gridSizeQuestion)
    computerGameBoard = createBoard(gridSizeQuestion)

    playerGameBoard = createBoard(gridSizeQuestion)
    computerGameBoard = createBoard(gridSizeQuestion)
    playerStartCoordinatesList = shipPlacement(gridSizeQuestion)
    computerStartCoordinatesList = shipPlacement(gridSizeQuestion)

    playerGameBoard[playerStartCoordinatesList[0][0]][playerStartCoordinatesList[0][1]] = "X"
    letter = chr(65 + playerStartCoordinatesList[0][0])
    number = playerStartCoordinatesList[0][1] + 1
    playerCoordinate = f"{letter}{number}"
    playerShipLocationCoordinatesList.append(playerCoordinate)
    print(f"\nPlayer dinghy was placed at {playerCoordinate}")

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
    print(f"Player destroyer was placed at {playerCoordinate1} and {playerCoordinate2}")

    letter = chr(65 + computerStartCoordinatesList[0][0])
    number = computerStartCoordinatesList[0][1] + 1
    computerCoordinate = f"{letter}{number}"
    computerShipLocationCoordinatesList.append(computerCoordinate)
    
    letter1 = chr(65 + computerStartCoordinatesList[1][0][0])
    number1 = computerStartCoordinatesList[1][0][1] + 1
    letter2 = chr(65 + computerStartCoordinatesList[1][1][0])
    number2 = computerStartCoordinatesList[1][1][1] + 1
    computerCoordinate1 = f"{letter1}{number1}"
    computerCoordinate2 = f"{letter2}{number2}"
    computerShipLocationCoordinatesList.append(computerCoordinate1)
    computerShipLocationCoordinatesList.append(computerCoordinate2)
    
    print("\n== PLAYER BOARD ==")
    printboard(playerGameBoard)
    
    print("\n== COMPUTER BOARD ==")
    printboard(computerGameBoard)

    while True:
        playerGuess = input("\nEnter guess to hit a battleship letter for row and numbers for columns (ex. A3): ").upper().strip()    
        
        length = 2
        if len(playerGuess) == 3 and playerGuess[1:].isdigit():
            if int(playerGuess[1:]) == 10:
                length = 3

        if playerGuess == "H" or playerGuess == "M":
            print("PICK ANOTHER SPOT. ")
            continue

        rungame = False
        if len(playerGuess) == length:
            conversion = ord(playerGuess[0])
            if conversion >= 65 and conversion < (65 + gridSizeQuestion):
                if playerGuess[1:].isdigit():
                    if int(playerGuess[1:]) >= 1 and int(playerGuess[1:]) <= gridSizeQuestion:
                        rungame = True

        if rungame == True:
            playerRowchanger = ord(playerGuess[0]) - 65
            playerColumnchanger = (int(playerGuess[1:]) - 1)

            if computerGameBoard[playerRowchanger][playerColumnchanger] == "H" or computerGameBoard[playerRowchanger][playerColumnchanger] == "M":
                continue
            if playerGameBoard[computerGuessRow][computerGuessColumn] == "H" or playerGameBoard[computerGuessRow][computerGuessColumn] == "M":
                continue

            while True:
                computerGuessColumn = random.randint(0, (gridSizeQuestion - 1))
                computerGuessRow = random.randint(0, (gridSizeQuestion - 1))
                compterletter = chr(65 + computerGuessRow)
                computernum = computerGuessColumn + 1
                computerGuess = f"{compterletter}{computernum}"
                if computerGuess == "H" or computerGuess == "M":
                    continue 
                elif computerGuess != "H" and computerGuess != "M":
                    break
                    
            if playerGuess in computerShipLocationCoordinatesList:
                computerGameBoard[playerRowchanger][playerColumnchanger] = "H"
                print("HIT!")
                
                if playerGuess == computerShipLocationCoordinatesList[0]:
                    print("You sank a dinghy!\n")
                elif playerGuess in computerShipLocationCoordinatesList[1:]:
                    destroyership = True
                    for targetcoor in computerShipLocationCoordinatesList[1:]:
                        if targetcoor != "H" and targetcoor != "M":
                             destroyership = False
                    if destroyership == True:
                        print("You sank a destroyer!\n")
                    else:
                        print("YOU HIT THE COMPUTER DESTROYER.\n")
                
                print("--- PLAYER BOARD ---")
                printboard(playerGameBoard)
                print("--- COMPUTER BOARD ---")
                printboard(computerGameBoard)
                
                playerwin = win_checker(computerShipLocationCoordinatesList)
                if playerwin == True:
                    print("You have sunk all ships. YOU WIN!")
                    break

            elif playerGuess not in computerShipLocationCoordinatesList:
                print("YOU MISSED TRY AGAIN.\n")
                computerGameBoard[playerRowchanger][playerColumnchanger] = "M"
                print("--- PLAYER BOARD ---")
                printboard(playerGameBoard)
                print("--- COMPUTER BOARD ---")
                printboard(computerGameBoard)
                
            if computerGuess in playerShipLocationCoordinatesList:
                if playerGameBoard[computerGuessRow][computerGuessColumn] == "X":
                    playerGameBoard[computerGuessRow][computerGuessColumn] = "H"
                print(f"CPU guessed {computerGuess}, HIT!")
                if computerGuess == playerShipLocationCoordinatesList[0]:
                    print("The computer sank your dinghy!\n")
                elif computerGuess in playerShipLocationCoordinatesList[1:]:
                    destroyership = True
                    for targetcoor in playerShipLocationCoordinatesList[1:]:
                        if targetcoor != "H" and targetcoor != "M":
                            destroyership = False
                    if destroyership == True:
                        print("The computer sank your destroyer!\n")
                    else:
                        print("THE CPU HIT YOUR DESTROYER.\n")
                
                print("--- PLAYER BOARD ---")
                printboard(playerGameBoard)
                print("--- COMPUTER BOARD ---")
                printboard(computerGameBoard)
                
                cpuwin = win_checker(playerShipLocationCoordinatesList)
                if cpuwin == True:
                    print("Computer has sunk all ships. YOU LOSE!")
                    break
            elif computerGuess not in playerShipLocationCoordinatesList:
                print(f"The CPU fires at {computerGuess}... MISSED\n")
                if playerGameBoard[computerGuessRow][computerGuessColumn] != "X":
                    playerGameBoard[computerGuessRow][computerGuessColumn] = "M"
                print("--- PLAYER BOARD ---")
                printboard(playerGameBoard)
                print("--- COMPUTER BOARD ---")
                printboard(computerGameBoard)
        else:
            print("Invalid input format or out of bounds. Example format: A3")