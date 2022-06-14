from time import sleep
import fontstyle


class library:
    def __init__(self, listofbooks):
        self.book_self = listofbooks

    def display(self):
        print(fontstyle.apply("\nList of available books are :-", "blue"))
        count = 1
        for books in self.book_self:
            print(fontstyle.apply(f"{count}. {books}", "blue"))
            count += 1
        options()

    def borrow_book(self, book_name):
        print("\nPlease wait till I am searching", end="")
        for i in range(11):
            print(".", end="")
            sleep(0.5)
        if book_name in self.book_self:
            print("Found !!")
            print(fontstyle.apply(f"'{book_name}' is available ^_^ !", "red,bold"))
            choice = input(
                "\nPress 'y' to confirm your borrowing else press any key to cancel the process : "
            )
            if choice == "y" or choice == "Y":
                print(
                    fontstyle.apply(
                        f"You have borrowed the book '{book_name}'",
                        "yellow_bg,bold,red",
                    )
                )
                print(
                    fontstyle.apply(
                        f"Please keep this book safely as you have to return this book after 30 days.",
                        "bold,white",
                    )
                )
                self.book_self.remove(book_name)
                options()
            else:
                options()
        else:
            print("Not found !!")
            print(
                fontstyle.apply(
                    "Sorry the book is not available at the moment ! Please wait till it gets returned or added",
                    "green,bold",
                )
            )
            options()

    def return_book(self, book_name):
        self.book_self.append(book_name)
        print(
            fontstyle.apply(
                f"\nThanks for returning the book '{book_name}'\nHave a great day ahead!!",
                "blue,bold",
            )
        )
        options()


def options():
    print(
        "\n1. To display the available books\n2. To borrow a book\n3. To return a book\n4. Display the books you have taken\n5. To exit library"
    )
    choice = input("Enter the index of you wanna do ?\n")
    try:
        choice = int(choice)
        if choice == 1:
            central_library.display()
        if choice == 2:
            book_name = input("Enter the name of the book which you want to borrow : ")
            book_name = book_name.capitalize()
            central_library.borrow_book(student.borrow_book(book_name))
        if choice == 3:
            book_name = input("Enter the name of the book which you want to return : ")
            book_name = book_name.capitalize()
            central_library.return_book(student.return_book(book_name))
        if choice == 4:
            student.display()
            options()
        if choice == 5:
            print(
                fontstyle.apply(
                    "\t\t\t\t\t\t\t\t\tThanks for choosing Central library ^_^",
                    "red,bold,yellow_bg",
                )
            )
            exit()
        else:
            print(
                fontstyle.apply(
                    "\nPlease enter a valid index from the given options\n", "red,bold"
                )
            )
            options()
    except ValueError:
        print(fontstyle.apply("\nPlease enter a valid value >_<\n", "red,bold"))
        options()


class Student:
    def __init__(self):
        self.book_list = []

    def display(self):
        temp = ",".join(self.book_list)
        if len(self.book_list) == 0:
            print(
                fontstyle.apply(
                    f"You don't have any borrowed books from this library",
                    "purple,bold",
                )
            )
            options()
        if len(self.book_list) == 1:
            print(
                fontstyle.apply(
                    f"The books which you have borrowed is '{temp}'", "purple,bold"
                )
            )
            options()
        if len(self.book_list) >= 2:
            print(
                fontstyle.apply(
                    f"The books which you have borrowed are {temp}", "purple,bold"
                )
            )
            options()

    def borrow_book(self, book_name):
        self.book_list.append(book_name)
        return book_name

    def return_book(self, book_name):
        self.book_list.remove(book_name)
        return book_name


if __name__ == "__main__":
    student = Student()
    central_library = library(["Python", "Java", "C++", "C Programming", "Rust"])
    print(
        fontstyle.apply(
            "\n\n========================================================================WELCOME TO CENTRAL LIBRARY======================================================================================",
            "red,bold,yellow_bg",
        )
    )
    options()
