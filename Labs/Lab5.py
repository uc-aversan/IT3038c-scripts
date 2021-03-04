import random

print("Guess what number I am thinking of between 1 and 100")
answer = random.randint(1,100)
guess = int(input())

print("Your guess was: " + str(guess))

while guess != answer:
    if guess > answer:
        print("Too high")
        guess = int(input())
    elif guess < answer:
        print("Too low")
        guess = int(input())

print("Congrats thats it!")
print("The right answer was: " + str(answer))