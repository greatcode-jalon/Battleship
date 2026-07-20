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
        
    generatedColumn1 = random.randint(0,3)
    generatedRow1 = random.randint(0,3)

    generatedColumn2 = random.randint(0,3)
    generatedRow2 = random.randint(0,3)

    generatedColumn3 = random.randint(0,3)
    generatedRow3 = random.randint(0,3)

    generatedColumn4 = random.randint(0,3)
    generatedRow4 = random.randint(0,3)

    continueGame = True
    while continueGame:
        if gameBoard[generatedColumn1][generatedRow1] == 0:
            letters = ["A", "B", "C", "D"]
            print(f"{letters[generatedColumn1]},{generatedRow1 + 1}")
            break

    guesslist = []      

    while True:
            playerGuess = input("Enter guess to hit a battleship letter for row and numbers for columns (ex. A3): ").lower()
            if len(playerGuess) == 2 and playerGuess[0] in "abcd" and playerGuess[1] in "1234":

                letterchangerrows = {"a" : 0 , "b" : 1 , "c" : 2 , "d" :3 }
                rowchanger = letterchangerrows[playerGuess[0]]

                columnchanger = str(int(playerGuess[1]) - 1)

                playerGuessconvert = rowchanger + columnchanger

                if playerGuess in guesslist:
                    print("SPOT IS TAKE, PICK ANOTHER SPOT.")
                    continue
                guesslist.append(playerGuessconvert)
                print(f"You have guest {playerGuessconvert}: GOOD HIT!! ")

                break
            else:
                print("Please retry")

    guesslist.append(playerGuess)






