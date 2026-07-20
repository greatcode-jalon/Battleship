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
            letters = ["A", "B", "C", "D"]
            coordinate = f"{letters[generatedColumn]}{generatedRow + 1}"
            shipLocationCoordinatesList.append(coordinate)
            break

    print(shipLocationCoordinatesList)      

    playerinput = True
    guesslist = []

    while playerinput:
            playerGuess = input("Enter guess to hit a battleship letter for row and numbers for columns (ex. A3): ").upper()
            
            if len(playerGuess) == 2 and playerGuess[0] in "ABCD" and playerGuess[1] in "1234":
                letterchangerrows = {"A" : 0 , "B" : 1 , "C" : 2 , "D" : 3}
                rowchanger = letterchangerrows[playerGuess[0]]
                columnchanger = (int(playerGuess[1]) - 1)
                playerGuessconvert = rowchanger + columnchanger

                if playerGuess in guesslist:
                    print("SPOT IS TAKEN, PICK ANOTHER SPOT.")
                    continue

                if playerGuess in shipLocationCoordinatesList:
                    guesslist.append(playerGuess)
                    print(f"You have guessed: {playerGuess}")
                    print("You hit and sunk a ship!")
                    playerinput = False
                    break
                else:
                    guesslist.append(playerGuess)
                    print(f"You have guessed: {playerGuess}")
                    print("You missed, Please try again.")
                    
            else:
                print("Make sure you use letters A-D and a number 1-4.")
