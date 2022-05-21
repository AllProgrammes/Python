def maximum(num1, num2, num3):
    arr = [num1, num2, num3]
    arr.sort()  # why to write big big functions when we have easy way to do it LOL XD
    return arr[2]


num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num 2 : "))
num3 = int(input("Enter num 3 : "))
print(maximum(num1, num2, num3), "is the greatest among all")
