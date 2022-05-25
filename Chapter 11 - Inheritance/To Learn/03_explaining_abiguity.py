class Employee:
    company = "Awaken"


class work_as:
    company = "Awaken unoffcial"


class details(Employee, work_as):
    name = "Biswajit"


data = details()
print(data.company)  # gives output --> Awaken
# but if I inherit [work_as] class first then it will print Awaken unofficial
# reason : order of inhertance
