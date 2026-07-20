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

    if gridSizeQuestion == 4:
        letters = ["A", "B", "C", "D"]
    elif gridSizeQuestion == 5:
        letters = ["A", "B", "C", "D", "E"]
    elif gridSizeQuestion == 6:
        letters = ["A", "B", "C", "D", "E", "F"]
    elif gridSizeQuestion == 7:
        letters = ["A", "B", "C", "D", "E", "F", "G",]
    elif gridSizeQuestion == 8:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H",]
    elif gridSizeQuestion == 9:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    elif gridSizeQuestion == 10:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

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
            if len(playerGuess) == 2 and playerGuess[0] in letters and playerGuess[1] in range(0, (gridSizeQuestion - 1)):

                letterchangerrows = {"A" : 0 , "B" : 1 , "C" : 2 , "D" : 3 , "E" : 4 , "F" : 5 , "G" : 6 , "H" : 7 , "I" : 8 , "J" : 9}
                rowchanger = letterchangerrows[playerGuess[0]]

                columnchanger = (int(playerGuess[1]) - 1)

                if playerGuess in guesslist:
                    print("This spot is occupied, please pick another. ")
                    continue
                
                elif playerGuess not in guesslist:
                    guesslist.append(playerGuess)
                    if playerGuess in shipLocationCoordinatesList:
                        print("You hit and sunk a ship!")
                        gameBoard[rowchanger][columnchanger] = "H"
                        print(gameBoard)
                        break

                    else:
                        print("You missed. Please try again.")
                        gameBoard[rowchanger][columnchanger] = "M"
                        print(gameBoard)
                        continue
            else:
                print("Please retry with the proper format. ")
                continue