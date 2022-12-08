import random
n=random.randint(1,99)
guess = int(input("ENter an integer from 1 to 99: "))
while n!="guess":
    print
    if guess<n:
        print("Guess is too low")
        guess = int(input("ENter an integer from 1 to 99: "))
    elif guess>n:
        print("Guess is high")
        guess = int(input("ENter an integer from 1 to 99: "))
    else:
        print("You guessed it!")
        break
    print