def sum_using_recursion(number, sum=0):
    if number == 1:
        return 1

    sum = sum + number
    return sum + sum_using_recursion(number - 1)


number = int(input("Enter the number : "))
print("Sum of first", number, "numbers is", sum_using_recursion(number))
