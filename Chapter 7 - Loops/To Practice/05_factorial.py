number = int(input("Enter the number : "))  # taking a number
fact = 1
for i in range(1, number + 1):
    fact = fact * i
    print(i, "! is", fact)

print(number, "factorial is", fact)
