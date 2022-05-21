star = int(input("Enter the number : "))
for row in range(star):
    print(" " * (star - row - 1), end="")
    print("x" * (2 * row + 1), end="")
    print(" " * (star - row - 1))
