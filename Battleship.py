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

    guesslist = []

    print(shipLocationCoordinatesList)

    while True:
            playerGuess = input("Enter guess to hit a battleship letter for row and numbers for columns (ex. A3): ").upper()
            if len(playerGuess) == 2 and playerGuess[0] in "ABCD" and playerGuess[1] in "1234":

                letterchangerrows = {"A" : 0 , "B" : 1 , "C" : 2 , "D" : 3}
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
                        print(gameBoard[0])
                        print(gameBoard[1])
                        print(gameBoard[2])
                        print(gameBoard[3])
                        break
                    else:
                        print("You missed. Please try again.")
                        gameBoard[rowchanger][columnchanger] = "M"
                        print(gameBoard[0])
                        print(gameBoard[1])
                        print(gameBoard[2])
                        print(gameBoard[3])
                        continue
            else:
                print("Please retry with the proper format. ")
                continue
