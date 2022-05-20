number = int(input("Enter the number : "))  # taking a number
sum = 0
for i in range(number):
    sum += i
    print("Count", i, "-->Sum =", sum, "\n")

print("Sum of first",number,"natural numbers is",sum)