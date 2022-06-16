def find_fact():
    try:
        number = int(input("Enter the value of n : "))
        fact = 1
        if number == 0 or number == 1:
            print(f"Factorial of {number} is --> {fact}")
        else:
            for i in range(1, number + 1):
                fact = fact * i
            print(f"Factorial of {number} is --> {fact}")
    except:
        print("Please enter a valid value !")
        find_fact()


while True:
    find_fact()

# but but but factorial is a very heavy program therefore we will find a solution ni the next program stay tuned
