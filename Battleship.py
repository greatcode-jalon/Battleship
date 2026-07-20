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
        
    while continueGame:
        if gameBoard[generatedColumn2][generatedRow2] == 0:
            letters = ["A", "B", "C", "D"]
            print(f"{letters[generatedColumn2]},{generatedRow2 + 1}")
            break

    while continueGame:
        if gameBoard[generatedColumn3][generatedRow3] == 0:
            letters = ["A", "B", "C", "D"]
            print(f"{letters[generatedColumn3]},{generatedRow3 + 1}")
            break

    while continueGame:
        if gameBoard[generatedColumn4][generatedRow4] == 0:
            letters = ["A", "B", "C", "D"]
            print(f"{letters[generatedColumn4]},{generatedRow4 + 1}")
            break
                
    playerGuess = input("Enter guess (ex. A,3): ")