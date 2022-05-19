age = int(input("Enter your age : "))
if age < 18:
    print("We don't work with kids.")
elif age >= 18 and age <= 32:
    print("You can give your CV in our office")
elif age > 32 and age <= 50:
    print("You can work with us")
elif age > 50:
    print("We need hot blood, not cold")
