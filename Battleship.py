#Names: Noah C + Ja'Lon S
#Comments: 
import random

def createBoard():
     return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

gameBoard = createBoard()

if __name__ == "__main__":
    shipLocationCoordinatesList = []
        
    generatedColumn = random.randint(0,3)
    generatedRow = random.randint(0,3)

    continueGame = True
    while continueGame:
        if gameBoard[generatedColumn][generatedRow] == 0:
            letters = ["a", "b", "c", "d"]
            coordinate = f"{letters[generatedColumn]}{generatedRow + 1}"
            shipLocationCoordinatesList.append(coordinate)
            break

    guesslist = []

    print(shipLocationCoordinatesList)      

    while True:
            playerGuess = input("Enter guess to hit a battleship letter for row and numbers for columns (ex. A3): ").lower()
            if len(playerGuess) == 2 and playerGuess[0] in "abcd" and playerGuess[1] in "1234":

                letterchangerrows = {"a" : 0 , "b" : 1 , "c" : 2 , "d" : 3}
                rowchanger = letterchangerrows[playerGuess[0]]

                columnchanger = (int(playerGuess[1]) - 1)

                playerGuessconvert = rowchanger + columnchanger

                if playerGuess in guesslist:
                    print("SPOT IS TAKE, PICK ANOTHER SPOT.")
                    continue
                guesslist.append(playerGuess)
                print(f"You have guest {playerGuess}")

                break
            else:
                print("Please retry")
                continue
    print(guesslist)
    guesslist.append(playerGuess)

    if playerGuess in shipLocationCoordinatesList:
        print("You hit and sunk a ship!")

    else:
        print("You missed. Please try again.")

