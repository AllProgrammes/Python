n = int(input("Enter the number to check for armstrong : "))

sum = 0
n_cpy = n
n_cpy2 = n
digit_count=0

while(n!=0):
    n = n//10
    digit_count+=1

for i in range(digit_count):
    sum+=pow(n_cpy%10,digit_count)
    n_cpy//=10

if sum==n_cpy2:
    print(f"{n_cpy2} is a armstrong number")
else:
    print(f"{n_cpy2} is not a armstrong number")
