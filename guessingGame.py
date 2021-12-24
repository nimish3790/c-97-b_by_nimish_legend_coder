import random
print("Number Guessing Game")
number = random.randint(1, 9)
chances = 0
print("guess a number between(1 to 9)")

while chances < 5 :
    guess = int(input("Enter your guess"))

    if guess == number:
        print("Congratulations you guessed correct")
        break

    elif guess < number :
        print("your guessed number is lower than the generated number")
    else:
        print("your guessed number is greater than the generated number")

        chances += 1

if not chances < 5 :
    print("All chances are finished, Correct answer was: ", number,"!!")
