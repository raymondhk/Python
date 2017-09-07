# create a new class called Bike
# need following properties - price, max_speed, miles
# Create 3 instances of the Bike class

class bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    
    def displayInfo(self):
        return "Price: $%s \nMax Speed: %s \nMiles: %s" %(self.price, self.max_speed, self.miles)    
    
    def ride(self, count=0,):
        self.count = count
        for i in range(0,self.count):
            print "Riding..."
            self.miles += 10
            print self.miles
        return self

    def reverse(self, count=0,):
        self.count = count
        for i in range(0,self.count):
            print "Reversing..."
            if self.miles > 4:
                self.miles -= 5
            print self.miles
        return self

bike1 = bike(200, "25mph")
bike2 = bike(300, "50mph")
bike3 = bike(250, "30mph")

print bike1.ride(3).reverse(1).displayInfo()
print bike2.ride(2).reverse(2).displayInfo()
print bike3.reverse(3).displayInfo()