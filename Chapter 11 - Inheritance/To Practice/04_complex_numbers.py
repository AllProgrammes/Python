class complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        print(f"Real part is {self.real} and Imaginary part is {self.imaginary}")

    def __add__(self, num):
        return f"{self.real+num.real}a + {self.imaginary+num.imaginary}i"

    def __mul__(self, num1):
        return f"{(self.real*num1.real)-(self.imaginary*num1.imaginary)} + {(self.real*num1.imaginary)+(self.imaginary*num1.real)}i"
        # formula used is -->> (ac-bd)+(ad+bc)i


c1 = complex(2, 3)
c2 = complex(4, 1)
sum = c1 + c2
mul = c1 * c2
print(sum)
print(mul)
