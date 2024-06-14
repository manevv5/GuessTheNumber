import random

computer_number = random.randint(1, 100)


while True:
    player_number = input("Guess the number (1 - 100): ")

    if not player_number.isdigit():
        print(f"Invalid input. Try again...")
        continue
    player_number = int(player_number)

    if player_number == computer_number:
        print(f"You guessed it!")
        break
    elif player_number > computer_number:
        print(f"Too high!")
    else:
        print(f"Too low!")
