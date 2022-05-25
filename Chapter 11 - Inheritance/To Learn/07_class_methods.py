class student:
    name = "Stranger"
    # -------------THIS WORKS AT OBJECT LEVEL ONLY------#
    # def change_name(self,external_name):
    #     self.name=external_name
    
    
    # -------------THIS WORKS AT CLASS LEVEL---------#
    @classmethod
    def change_name(cls, external_name):
        cls.name = external_name


test = student()
print(test.name)
test.change_name("Biswa")
print(test.name)
print(student.name)
