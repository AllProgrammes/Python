import random


while True:
    computer = random.randint(1, 10)
    print("To exit this program press 'q'")
    number = input("Enter the number here : ")
    if number == "q" or number == "Q":
        break
    try:
        print("Trying.....")
        number = int(number)
        if number == computer:
            print("HEHE ! You gotch me")
        else:
            print("Naaaa You can't catch me ^_^")
    except Exception as error:
        print_error = input(
            "Oops !! seems like got an error *_*\nWanna see ? if yes press 'y' else press any key to continue : "
        )
        if print_error == "y" or print_error == "Y":
            print(f"Error : {error}")
        else:
            continue
print("Thanks for playing ^_^")
