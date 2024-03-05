num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

for i in range(1,(num1*num2)+1):
    if((i%num1==0) and (i%num2==0)):
        print("LCM is :",i)
        break