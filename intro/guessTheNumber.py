import random


def play_game(attempts):
    rand_num = random.randint(1, 100)
    correct_guess = False
    while attempts != 0 and not correct_guess:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("\nMake a guess: "))
        if guess == rand_num:
            correct_guess = True
            return print(f"Correct 🥳🍾🎈. The answer is {rand_num}.")
        else:
            attempts -= 1
            if guess < rand_num:
                print("Too low")
            else:
                print("Too high")

        if attempts == 0:
            return print(f"\nToo bad 🥹... You've lost. The number was {rand_num}.")


def pick_difficulty():
    difficulty = str(input("Pick a difficulty: Hard or Easy: ")).lower()

    if difficulty == "hard":
        return 5
    elif difficulty == "easy":
        return 10
    else:
        print("Invalid choice!!!")
        return pick_difficulty()


def continue_game():
    response = str(input("Wanna play again? 'Yes ✅' or 'No 🙅‍♂️': ").lower())
    if response == "yes":
        return True
    elif response == "no":
        return False
    else:
        print("Invalid choice!!!")
        return continue_game()


def start_playing():
    print("\nThink of a number between 1 and 100")
    attempts = pick_difficulty()
    play_game(attempts)
    continue_playing = continue_game()
    if continue_playing:
        start_playing()
    else:
        print("Have a nice time 🙂.")


start_playing()
