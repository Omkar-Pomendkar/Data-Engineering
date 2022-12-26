class RailwayForm:
    formType = "Railwayform"
    def prindata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
omkarsApplication = RailwayForm()
omkarsApplication.name = "Omkar"
omkarsApplication.train = "Tejas Train"
omkarsApplication.prindata();
