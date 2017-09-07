# create a class called car
# specify: price, speed, fuel, mileage

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0
        if self.price > 10000:
            self.tax = .15
        if self.price <= 10000:
            self.tax = .12

    
    def display_all(self):
        return "Price: %s\nSpeed: %s\nFuel: %s\nMileage: %s\nTax: %s" %(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(3000, "60mph", "Full", "20mpg")
car3 = Car(12000, "100mph", "Not Full", "10mpg")
car4 = Car(40000, "100mph", "Maybe Full?", "17mpg")
car5 = Car(200000, "40mph", "Kind of Full", "19mpg")
car6 = Car(3500, "80mph", "Full", "25mpg")
print car1.display_all()
print car2.display_all()
print car3.display_all()
print car4.display_all()
print car5.display_all()
print car6.display_all()