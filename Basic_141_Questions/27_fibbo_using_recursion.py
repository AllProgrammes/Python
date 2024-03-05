def fibbo(n):
    if(n<=1):
        return n
    else:
        return fibbo(n-1)+fibbo(n-2)

n = int(input("Enter the value of n : "))
print(f"Fibonacci value of {n} is {fibbo(n)}")