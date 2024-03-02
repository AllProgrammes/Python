def isPrime(number):
    if(number==1):
        return False
    for factor in range(2,number):
        if(number%factor==0):
            return False
    return True

n = int(input("Enter the value of n : "))

for number in range(1,n+1):
    if(isPrime(number)):
        print(number,"is a prime number")