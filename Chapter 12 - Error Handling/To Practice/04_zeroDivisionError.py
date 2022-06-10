import fontstyle

print(
    fontstyle.apply(
        "\n\n\t\t\t\t\t\tI am a Small Program which does division of 2 numbers i.e a/b\n\n",
        "underline,black,yellow_bg",
    )
)
a = input("Enter the value of a : ")
b = input("Enter the value of b : ")
try:
    a = int(a)
    b = int(b)
    try:
        print(f"If we divide {b} from {a} then we will get {a/b}")
    except ZeroDivisionError:
        print(f"If we divide {b} from {a} then we will get ♾️")
except:
    print("Please enter a valid input")
