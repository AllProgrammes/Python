n = int(input("Enter the value of n : "))

start1 = 0
start2 = 1
fibbo = 0
for i in range(1,n):
    fibbo = start1 + start2
    start1 = start2
    start2 = fibbo
    
print(fibbo)