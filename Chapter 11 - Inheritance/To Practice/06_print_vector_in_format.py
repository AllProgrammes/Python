class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}j + {self.vec[1]}j + {self.vec[2]}k"


data1 = vector([8, 3, 4])
data2 = vector([4, 5, 10])
print(data1)
print(data2)
