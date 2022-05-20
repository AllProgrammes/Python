number = int(input("Enter the number : "))#taking a number
count = 0#init a count variable with 0
for i in range(2,number):#goes from 2 to (number-1)
    if number % i == 0:
        count += 1
    i += 1

if count >= 1:
    print(number, "is a not prime number")
elif count == 0:
    print(number, "is a prime number")
