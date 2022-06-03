class dunder_methods:
    def __str__(self):  # str method
        return f"I am used when you want to print the object and without me you will get strange fucntions strings in the output terminal"

    def __len__(
        self,
    ):  # len method : it is used to print the lenght of the object as per [return] is set
        return 69


data = dunder_methods()
print(data)
print(len(data))
