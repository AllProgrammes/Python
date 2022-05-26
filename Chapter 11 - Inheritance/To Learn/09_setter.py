class employee:
    salary = 12000
    bonus = 1300

    @property  # acts as a getter
    def totalsalary(self):  # works as a variable not as a Fx [reason: @property]
        return self.bonus + self.salary

    @totalsalary.setter  # declaring a setter to take total salary of that object and change the value of bonus accordingly
    def totalsalary(self, total):
        self.bonus = total - self.salary


biswajit = employee()  # made an object
biswajit.totalsalary = 15000  # runs with the help of setter declared at line 9
print(biswajit.bonus)  # print bonus of object [biswajit]
