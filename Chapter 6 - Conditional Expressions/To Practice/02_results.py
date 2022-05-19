english = int(input("Enter your english marks : "))
hindi = int(input("Enter your hindi marks : "))
maths = int(input("Enter your maths marks : "))
total_percentage = (english + hindi + maths) / 3
if english >= 33 and hindi >= 33 and maths >= 33:
    if total_percentage >= 40:
        print("You are passed !")
    else:
        print("You are failed !")
else:
    print("You are failed !")
