english = int(input("Enter your english marks : "))
hindi = int(input("Enter your hindi marks : "))
maths = int(input("Enter your maths marks : "))
total_percentage = (english + hindi + maths) / 3
if 90 < total_percentage and total_percentage <= 100:
    print("Excellent Job !")
elif 80 < total_percentage and total_percentage <= 90:
    print("A Grade")
elif 70 < total_percentage and total_percentage <= 80:
    print("B Grade")
elif 60 < total_percentage and total_percentage <= 70:
    print("C Grade")
elif 50 < total_percentage and total_percentage <= 60:
    print("D Grade")
elif total_percentage < 50:
    print("E Grade")
