class employee:
    salary = 12000
    bonus = 1300

    @property  # acts as a getter
    def totalsalary(self):  # works as a variable not as a Fx [reason: @property]
        return self.bonus + self.salary


biswajit = employee()
print(biswajit.totalsalary)
