import random
n = random.randint(1, 11)
running = True

while running:
    guess = input("Guess a number between 1 and 10: ")
    num_guess = int(guess)
    if num_guess == n:
        print("You guessed right!")
        running = False
    elif num_guess < n:
        print("Try higher")
    elif num_guess > n:
        print("Try lower")
else:
    print('The while loop is over')

print ("Done")
