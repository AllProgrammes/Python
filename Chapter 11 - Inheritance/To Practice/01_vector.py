class vector_2d:
    def take_2d(self):
        self.x1 = int(input("Enter the value of x1 : "))
        self.y1 = int(input("Enter the value of y1 : "))
        self.x2 = int(input("Enter the value of x2 : "))
        self.y2 = int(input("Enter the value of y2 : "))

    def display1(self):
        print(
            f"Dimensions of 2D vector are as folows :-\n{self.x1}\t{self.y1}\n{self.x2}\t{self.y2}\n"
        )


class vector_3d(vector_2d):
    def take_3d(self):
        self.x3 = int(input("Enter the value of x3 : "))
        self.y3 = int(input("Enter the value of y3 : "))
        self.z1 = int(input("Enter the value of z1 : "))
        self.z2 = int(input("Enter the value of z2 : "))
        self.z3 = int(input("Enter the value of z3 : "))

    def display2(self):
        print(
            f"Dimensions of 3D vector are as folows :-\n{self.x1}\t{self.y1}\t{self.z1}\n{self.x2}\t{self.y2}\t{self.z2}\n{self.x3}\t{self.y3}\t{self.z3}"
        )


vector = vector_3d()
vector.take_2d()  # Giving 2D arrays values
vector.take_3d()  # Giving 3D arrays values
vector.display1()  # Displaying 2D arrays values
vector.display2()  # Displaying 3D arrays values
