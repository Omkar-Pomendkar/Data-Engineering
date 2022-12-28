class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Name is {self.train}")

omkar = RailwayForm()
omkar.name = "Omkar"
omkar.train = "Deccan Express"
omkar.printData()
