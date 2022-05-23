import math


class calc:
    @staticmethod
    def start():
        num = int(input("Enter the number : "))
        print("Square root value of", num, "is", math.sqrt(num))
        print("Square of", num, "is", math.pow(num, 2))
        print("Cube value of", num, "is", math.pow(num, 3))

    @staticmethod
    def welcome():
        print(
            "\n\n-----------------------------Welcome Sir/Mam-------------------------------------\n\n"
        )

    @staticmethod
    def bye():
        print(
            "\n\n-------------------------Thanks for using my program------------------------------"
        )


data = calc()
data.welcome()
data.start()
data.bye()
