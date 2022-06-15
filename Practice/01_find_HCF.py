num1 = input("Enter the value of num1 : ")
num2 = input("Enter the value of num2 : ")
try:
    num1 = int(num1)
    num2 = int(num2)
    factors = []
    if num1 > num2:
        for factor in range(2, num1):
            if num1 % factor == 0 and num2 % factor == 0:
                factors.append(factor)
    else:
        for factor in range(2, num2):
            if num1 % factor == 0 and num2 % factor == 0:
                factors.append(factor)
    print(f"HCF of {num1} and {num2} is", max(factors))
except:
    print("Please enter a valid int value !!")
