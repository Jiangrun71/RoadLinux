class Cars:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def decribe_car(self):
        print(f"the car {self.brand} {self.model} is made in year {self.year}")
mycar = Cars('Audi','XT6','2022')
mycar.decribe_car()
