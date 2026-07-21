#Names: Noah C + Ja'Lon S
#Comments: 
import random

def createBoard():
    columnRow = []
    for column in range(gridSizeQuestion):
        boardRow = []
        columnRow.append(boardRow)
        for row in range(gridSizeQuestion):
            boardRow.append(0)
    return columnRow

if __name__ == "__main__":
    shipLocationCoordinatesList = []

    while True:
        try:
            gridSizeQuestion = int(input("Enter a number, 4-10, to define the size of the board (ex, 5 = 5x5 board): "))
            if gridSizeQuestion in range(4,11):
                break
            if gridSizeQuestion not in range(4,11):
                print("Please enter your board dimensions with a number 4-10. ")
                continue
        except:
            print("Invalid board dimensions. Please try again.")
            continue
    
    gameBoard = createBoard()
    for row in gameBoard:
        print(row)

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

    continueGame = True
    while continueGame:
        if gameBoard[generatedColumn][generatedRow] == 0:
            coordinate = f"{letters[generatedColumn]}{generatedRow + 1}"
            shipLocationCoordinatesList.append(coordinate)
            break

    guesslist = []

    while True:
        playerGuess = input("Enter guess to hit a battleship letter for row and numbers for columns (ex. A3): ").upper()
        if len(playerGuess) == 3 and int(playerGuess[1]) == 1 and int(playerGuess[2]) == 0:
            length = 3
        else:
            length = 2

        if len(playerGuess) == length and playerGuess[0] in letters and int(playerGuess[1]) in numbers:
            letterchangerrows = {"A" : 0 , "B" : 1 , "C" : 2 , "D" : 3 , "E" : 4 , "F" : 5 , "G" : 6 , "H" : 7 , "I" : 8 , "J" : 9}
            rowchanger = letterchangerrows[playerGuess[0]]

            columnchanger = (int(playerGuess[1:]) - 1)

            if playerGuess in guesslist:
                print("This spot is occupied, please pick another. ")
                continue

            elif playerGuess not in guesslist:
                guesslist.append(playerGuess)
                if playerGuess in shipLocationCoordinatesList:
                    print("You hit and sunk a ship!")
                    gameBoard[rowchanger][columnchanger] = "H"
                    for row in gameBoard:
                        print(row)
                    break

                else:
                    print("You missed. Please try again.")
                    gameBoard[rowchanger][columnchanger] = "M"
                    for row in gameBoard:
                        print(row)
                    continue
        else:
            print("Please retry with the proper format. ")
            continue