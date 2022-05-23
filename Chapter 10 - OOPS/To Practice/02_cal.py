import math


class calc:
    @staticmethod
    def __init__(num):
        print("Square root value of", num, "is", math.sqrt(num))
        print("Square of", num, "is", math.pow(num, 2))
        print("Cube value of", num, "is", math.pow(num, 3))


data = calc(100)
