from logging import exception
import random

# Welcome part of this game
for i in range(1, 100):
    print("-", end="")
print("\n\n\t\t\t\tWELCOME TO GUESS THE NUMBER GAME\n")
for i in range(1, 100):
    print("-", end="")

print(
    "\n\nHow to play -->> Computer will choose a number between 1 to 10 and you have to guess what is that number"
)

# All required variables
count = 1
computer = random.randint(1, 10)

# Working of the game
while count <= 3:
    human = input("\nEnter your guessed number here : ")
    try:  # this will try changing tha data type to int
        human = int(human)
        if human == computer and count == 1:
            print("Dam !! You guessed it in first attempt")
            exit(0)
        elif human == computer and count > 1:
            print(f"You guessed it in {count} attempts")
            exit(0)
        elif human != computer:
            if count == 3:
                print(f"\nYou have lost the game\nThe correct number was {computer}")
            else:
                print(f"\nOops You are wrong , You have {3-count} attempts left")
                if human > computer:
                    print("Hint : The number is less than what you have entered")
                elif human < computer:
                    print("Hint : The number is more than what you have entered")
        count += 1
    except:  # if the data conversion fails somehow then the user will get the below message and the program will continue
        print(f"You have entered {type(human)} value")
        continue
