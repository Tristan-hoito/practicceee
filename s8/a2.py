class Car:
    def __init__(self,model,brand, month, year):
        self.model = model
        self.brand = brand
        self.year = year
        self.month = month

    def haha(self):
        print(f"broom broom {self.model}.\nbroom broom {self.brand}.\nMade during {self.month}, {self.year}.")

pogi1 = Car("Innova","Toyota", "August", 2004)

print("")
pogi1.haha()
print("")