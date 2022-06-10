from time import sleep
import fontstyle

user_number = input("Enter the number which you want to get the table : ")
try:
    user_number = int(user_number)
    multiples = [user_number * i for i in range(1, 11)]

    print("Creating a file", end="")
    for temp in range(10):
        print(".", end="")
        sleep(0.3)
    data = open("table.txt", "w")  # lets open the file in write mode
    print("Done !!")

    print("Writing on it", end="")
    for temp in range(10):
        print(".", end="")
        sleep(0.3)
    data.write(str(multiples))
    print("Done !!")
    print(fontstyle.apply(f"Print Preview : {multiples}", "bold/blue"))
    print(fontstyle.apply("Proccess Executed Successfully !!", "bold/red/underline"))
except:
    print("Please enter a number ＞﹏＜")
