import random
n = random.randint(1, 11)

while True:
    guess = input("Guess a number between 1 and 10: ")
    num_guess = int(guess)
    if (num_guess == n):
        print("You guessed right!")
        break
    elif num_guess < n:
        print("Try higher")
    elif num_guess > n:
        print("Try lower")