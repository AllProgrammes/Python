from operator import truediv


class calculator:
    def __init__(self, num):
        self.num = num

    def __add__(number1, number2):
        print("Lets add")
        return number1.num + number2.num

    def __mul__(number1, number2):
        print("Lets multiply")
        return number1.num * number2.num

    def __sub__(number1, number2):
        print("Lets substract")
        if number1.num > number2.num:
            return number1.num - number2.num
        else:
            return number2.num - number1.num

    def __truediv__(number1, number2):
        print("Lets Divide")
        if number1.num > number2.num:
            return number1.num / number2.num
        else:
            return number2.num / number1.num


num1 = calculator(5)
num2 = calculator(4)
sum = num1 + num2
print(sum)

mul = num1 * num2
print(mul)

sub = num1 - num2
print(sub)

truediv = num1 / num2
print(truediv)
