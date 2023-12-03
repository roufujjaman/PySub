class Star_Cinema:
    __hall_list = list()
    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = dict()
        self.__show_list = list()
        self.__hall_no = hall_no
        self.__rows = rows
        self.__cols = cols
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        seats = list(list())
        
        for i in range(self.__rows):
            seats.append([])
            for j in range(self.__cols):
                seats[i].append(0)
        
        self.__seats[id] = seats

    def book_seats(self, id, seats):
        if id in self.__seats:
            for row, col in seats:
                if (row > 0 and row <= self.__rows) and (col > 0 and col <= self.__cols):
                    if self.__seats[id][row - 1][col - 1] == 0:
                        self.__seats[id][row - 1][col - 1] = 1
                        print(f"SEAT [{row}, {col}]\t : Booked")
                    else:
                        print(f"SEAT [{row}, {col}]\t : Not Available")
                else:
                    print("\t\t : < Invalid Row, Column >")
        else:
            print("\t\t : < Invalid ID >")
        
    def view_show_list(self):
        for n, (id, show, time) in enumerate(self.__show_list):
            print(f"{n + 1}. ID: {id}, MOVIE: {show}, TIME: {time}")
    
    def view_available_seats(self, id):
        if id in self.__seats:
            for row in range(self.__rows):
                for col in range(self.__cols):
                    if self.__seats[id][row][col] == 0:
                        print(f"[{row + 1},{col + 1}]".center(7), end=" ")
                    else:
                        print("---".center(7), sep="  ", end=" ")
                print()
        else:
            print("\t\t : < Invalid ID >")

h1 = Hall(10, 10, 1)
h1.entry_show("M1", "The Creator", "1:00 PM")
h1.entry_show("M2", "The Lost City", "4:30 PM")
h1.entry_show("M3", "Guardians Of the Galaxy", "8:30")

while(True):
    print("[1] NOW SHOWING\n[2] AVAILABLE SEATS\n[3] BUY TICKET\n[4] EXIT")
    input_val = int(input("SELECT OPTION\t : "))
    if input_val == 1:
        print("NOW SHOWING")
        h1.view_show_list()
        print()
    elif input_val == 2:
        input_val_id = input("INSERT ID\t : ")
        h1.view_available_seats(input_val_id.upper())
        print()
    elif input_val == 3:
        input_val_id = input("INSERT ID\t : ")
        input_val_quantity = int(input("INSERT QUANTITY\t : "))
        seats = []
        for i in range(input_val_quantity):
            row = int(input("INSERT ROW\t : "))
            col = int(input("INSERT COLUMN\t : "))
            seats.append((row, col))
        h1.book_seats(input_val_id.upper(), seats)
        print()
    if input_val == 4:
        break