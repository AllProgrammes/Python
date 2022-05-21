def pattern(num):
    for i in range(num):
        print("x" * (num - i))


number = int(input("Enter the number : "))
pattern(number)
