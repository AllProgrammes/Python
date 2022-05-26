class animal:
    # @staticmethod ---> idk why but with static method it didn't work .....I will find a reason for sure
    def __init__(self):
        print("I am animal class")


class pet(animal):
    # @staticmethod ---> idk why but with static method it didn't work .....I will find a reason for sure
    def __init__(self):
        super().__init__()
        print("I am pet class")


class dog(pet):
    # @staticmethod ---> idk why but with static method it didn't work .....I will find a reason for sure
    def __init__(self):
        super().__init__()
        print("I am Sheru and I am barking.")


piyush = dog()
