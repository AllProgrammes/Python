def factorial_simple(number):
    product = 1
    for i in range(1, number + 1):
        product = product * i

    return product


def factorial_recursive(number):
    if number == 1 or number == 0:
        return 1
    return number * factorial_recursive(number - 1)


number = int(input("Enter the number : "))
print("Factorial of", number, "is", factorial_recursive(number))
