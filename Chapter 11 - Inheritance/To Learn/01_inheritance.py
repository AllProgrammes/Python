class Student:  # base class
    maths = 00
    science = 00
    hindi = 00
    name = ""


class std12(Student):  # derived class
    def __init__(self):
        self.name = input("Enter your name : ")
        self.std = int(input("Enter your class : "))
        if self.std == 12:
            self.subjects()
            self.results()
        else:
            print("Come after", 12 - self.std, "yrs kid !")

    def subjects(self):
        self.maths = int(input("Enter your maths marks : "))
        self.science = int(input("Enter your science marks : "))
        self.hindi = int(input("Enter your hindi marks : "))

    def marks(self):
        percentage = (self.maths + self.science + self.hindi) / 3
        return percentage

    def results(self):
        print("Name =", self.name)
        print("Std =", self.std)
        print("Maths =", self.maths)
        print("Science =", self.science)
        print("Hindi =", self.hindi)
        print("Percentage =", int(self.marks()), "%")


biswajit = std12()
