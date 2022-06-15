num1 = input("Enter the value of num1 : ")
num2 = input("Enter the value of num2 : ")
try:
    num1 = int(num1)
    num2 = int(num2)
    x = max(num1, num2)
    while True:
        if x % num1 == 0 and x % num2 == 0:
            print(f"LCM of {num1} and {num2} is {x}")
            break
        else:
            x+=1
except:
    print("Please enter a valid int value !!")
