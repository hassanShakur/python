import random


def playGame(attempts):
    randNum = random.randint(1, 100)
    correctGuess = False
    while attempts != 0 and not correctGuess:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("\nMake a guess: "))
        if guess == randNum:
            correctGuess = True
            return print(f"Correct 🥳🍾🎈. The answer is {randNum}.")
        else:
            attempts -= 1
            if guess < randNum:
                print("Too low")
            else:
                print("Too high")

        if attempts == 0:
            return print("\nToo bad 🥹... You've lost")


def pickDifficulty():
    difficulty = str(input("Pick a difficulty: Hard or Easy: ")).lower()

    if difficulty == "hard":
        return 5
    elif difficulty == "easy":
        return 10
    else:
        print("Invalid choice!!!")
        return pickDifficulty()


def continueGame():
    response = str(input("Wanna play again? 'Yes ✅' or 'No 🙅‍♂️': ").lower())
    if response == "yes":
        return True
    elif response == "no":
        return False
    else:
        print("Invalid choice!!!")
        return continueGame()


def startPlaying():
    print("\nThink of a number between 1 and 100")
    attempts = pickDifficulty()
    playGame(attempts)
    continuePlaying = continueGame()
    if continuePlaying:
        startPlaying()
    else:
        print("Have a nice time 🙂.")


startPlaying()
