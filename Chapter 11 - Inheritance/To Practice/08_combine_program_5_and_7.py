from regex import D


class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        temp = ""
        for i in range(len(self.vec)):
            temp += f" {self.vec[i]}a +"

        return temp[1:-1]

    def __len__(self):
        return len(self.vec)

    def __add__(self, v2):
        if len(self.vec) != len(v2.vec):
            print(
                "The process can't be excuted as the length of these 2 vectors are not equal"
            )
        else:
            added_list = []
            for i in range(len(self.vec)):
                added_list.append(self.vec[i] + v2.vec[i])
            return f"Product of both vectors are : {added_list}"

    def __mul__(self, v2):
        if len(self.vec) != len(v2.vec):
            print(
                "The process can't be excuted as the length of these 2 vectors are not equal"
            )
        else:
            sum = 0
            for i in range(len(self.vec)):
                sum += self.vec[i] * v2.vec[i]

            return f"Sum of both vectors are : {sum}"


data1 = vector([1, 2, 4])
data2 = vector([4, 3, 1, 5])
print("Length of vector 1 is -->", len(data1))
print("Length of vector 2 is -->", len(data2))

print(data1 + data2)
print(data1 * data2)
