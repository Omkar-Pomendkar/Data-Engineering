class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the Train is {self.name}")
        print(f"The seats available in the Train are {self.seats}")

    def fareInfo(self):
        print(f"The Price of Ticket is : {self.fare}")

    def bookTicket(self):
        if(self.seats > 0):
            print(f"Your ticket has been Booked ! Your seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("This train is full Kindly try in Tatkal")


deccanqueen = Train("Deccan Queen ",100 ,300)
deccanqueen.getStatus()
deccanqueen.bookTicket()
deccanqueen.fareInfo()
deccanqueen.bookTicket()