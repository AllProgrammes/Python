def check_armstrong(num):
    cpy=num
    sum=0
    for i in range(len(str(cpy))):
        sum+=pow(num%10,len(str(cpy)))
        num//=10
    if(cpy==sum):
        return True

lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))

for i in range(lower,upper):
    if(check_armstrong(i)):
        print(f"{i} is an armstring number")