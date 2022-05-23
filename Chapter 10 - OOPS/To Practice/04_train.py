class Train:
    total_seats = 5
    fare = 2034

    def __init__(self, name):
        self.name = name

    def start(self, book_seats):
        self.book_seats = book_seats
        print(
            "\n*****************************************Welcome to Indian Railways*****************************************\n"
        )
        print("Train Name :", self.name)
        print("Searching for seats..............")
        self.check_for_seats()
        self.ticket_price()

    def check_for_seats(self):
        if self.total_seats >= self.book_seats:
            print(
                "Thanks for keeping patience !You can book your",
                self.book_seats,
                "seats",
            )
        elif self.total_seats < self.book_seats:
            print(
                "Sorry No seats are available !\nPlease book your",
                self.book_seats,
                "seats in tatkal\n",
            )
            exit(0)

    def ticket_price(self):
        print(
            f"Total Price = {self.book_seats} x {self.fare} = {self.book_seats*self.fare}"
        )
        ask = int(
            input("Press 1 to finalize your booking ,else press any number to exit : ")
        )
        if ask == 1:
            self.total_seats = self.total_seats - self.book_seats
            print(
                "Tickets for",
                self.name,
                "have been booked successfully\nHave a nice journey\n",
            )
        else:
            exit(0)


biswajit = Train("Satabdi Express 1023")
biswajit.start(2)
biswajit.start(3)
biswajit.start(1)
