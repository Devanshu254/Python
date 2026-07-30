import random
jackpot = random.randint(1, 100)

guess = int(input("Take a guess: "))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Wrong, please go for higher value")
    else:
        print("Wrong, please go for lower value!")
    guess = int(input("Enter the jackpot value again: "))
    counter = counter + 1
else:
    print("correct guess!")
    print("attempts", counter)