class board10:
    def passed_student_10(self):
        pass_10 = int(input("Enter the number of students who passed in 10th board : "))
        return pass_10


class board12:
    def passed_student_12(self):
        pass_12 = int(input("Enter the number of students who passed in 12th board : "))
        return pass_12


class combined_board_results(board10, board12):
    school_name = ""

    def __init__(self, name):
        self.school_name = name

    def total_passed_board_students(self):
        print(
            "Total number of passed board students of",
            self.school_name,
            "is",
            self.passed_student_10() + self.passed_student_12(),
        )


holy_cross_school = combined_board_results("Holy Cross School")
holy_cross_school.total_passed_board_students()
