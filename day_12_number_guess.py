import random


def number_of_guess(level):
    if level == 'e':
        return 10
    elif level == 'h':
        return 5


print('Welcome to the number guessing game.')
print("I am thinking of a number between 1 and 100.")

game_on = True

while game_on:
    mode = input("Select the mode of game: Type 'E' for Easy(10 attempts) or Type 'H' for Hard(5 attempts) = ").strip().lower()
    number = random.randint(1, 101)
    total_attempts = number_of_guess(mode)
    i = 1
    while total_attempts > 0:
        guess = int(input(f"Enter you guess {i}: "))
        if guess == number:
            print(f"\nThat's correct. I was thinking of the number {number}")
            game_on = False
            break
        elif guess > number:
            print("Your guess is higher than the actual number.")
        elif guess < number:
            print("Your guess is lower than the actual number.")

        total_attempts -= 1
        print(f"You have {total_attempts} attempts left to guess the number.\n")
        i += 1
    if total_attempts == 0 and guess != number:
        print(f"\nYou lose. The correct number is {number}.")
        game_on = False




