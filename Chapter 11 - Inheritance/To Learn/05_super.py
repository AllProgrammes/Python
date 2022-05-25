class test1:
    def human(self):
        print("COSMOS is a super human")


class test2(test1):
    def human(self):
        print("Biswajit is a human")
        super().human()  # it is used to call the function from its parent class --> here in this case it will call tht Fx human from test1


marvel = test2()
marvel.human()
