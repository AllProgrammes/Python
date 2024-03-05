num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

max = 0
if num1<num2:
    for i in range(1,num1+1):
        if((num1%i==0) and (num2%i==0)):
            if(i>max):
                max=i
else:
    for i in range(1,num2+1):
        if((num1%i==0) and (num2%i==0)):
            if(i>max):
                max=i
print("HCF is :",max)