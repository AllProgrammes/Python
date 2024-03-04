n = int(input("Enter the value of n : "))

if n == 0:
    print(f"Factorial of {n} is 1")
elif n<0:
    print(f"Factorial does not exists for negative numbers")
else:
    start = 1
    for i in range(1,n+1):
        start*=i
    
    print(f"Factorial of {n} is {start}")