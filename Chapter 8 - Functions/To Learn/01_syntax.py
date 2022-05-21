def percent(marks):
    return sum(marks) / len(marks)


(subject1) = int(input("Enter the number of subjects 1 : "))
(subject2) = int(input("Enter the number of subjects 2 : "))
(subject3) = int(input("Enter the number of subjects 3 : "))

sub_marks = [subject1, subject2, subject3]
percentage = percent(sub_marks)
print("Percent =", percentage, "%")
