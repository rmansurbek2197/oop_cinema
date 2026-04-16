class Cinema:
    def __init__(self, size=10):
        self.seats = [False] * size

    def book(self, seat):
        if 0 <= seat < len(self.seats) and not self.seats[seat]:
            self.seats[seat] = True

    def cancel(self, seat):
        if 0 <= seat < len(self.seats):
            self.seats[seat] = False

    def show(self):
        for i, s in enumerate(self.seats):
            print(i, "Booked" if s else "Free")


def menu():
    c = Cinema()

    while True:
        print("\n1.Book 2.Cancel 3.Show 0.Exit")
        choice = input(">> ")

        if choice == "1":
            c.book(int(input("Seat: ")))
        elif choice == "2":
            c.cancel(int(input("Seat: ")))
        elif choice == "3":
            c.show()
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()
