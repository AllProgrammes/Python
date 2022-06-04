class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        temp = ""
        for i in range(len(self.vec)):
            temp += f" {self.vec[i]}a +"

        return temp[1:-1]

    def __add__(self, v2):
        added_list = []
        for i in range(len(self.vec)):
            added_list.append(self.vec[i] + v2.vec[i])
        return added_list

    def __mul__(self, v2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * v2.vec[i]

        return sum


data1 = vector([1, 2, 4])
data2 = vector([4, 3, 1])
print(data1)
print(data2)

print("Sum of both vectors are :", data1 + data2)
print("Product of both vectors are :", data1 * data2)
