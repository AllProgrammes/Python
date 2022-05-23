class student:
    std = "12"

    def details(self):
        print(f"Name = {self.name}\nClass = {self.std}\nRoll no. = {self.roll}")

    @staticmethod  # no need of writing self if using static method
    def greet():
        print("Good Morning !")


biswajit = student()
biswajit.name = "Biswajit"
biswajit.roll = 31
biswajit.greet()
biswajit.details()
