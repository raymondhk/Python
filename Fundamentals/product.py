# create a product class to track products

class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status="For Sale"):
        self.price = "{:,.2f}".format(price)
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = "{:,.2f}".format(cost)
        self.status = status  

    def Sell(self):
        self.status = "Sold!"
        return "Product: %s\n Status: %s\n" %(self.item_name, self.status)

    def AddTax(self, tax):
        self.tax = tax
        self.price = float(self.price)
        self.price += self.tax*self.price
        self.price = "{:,.2f}".format(self.price) 
        return self

    def Return(self, reason):
        print "Returned Item"
        self.reason = reason.lower()
        if self.reason == "defective":
            self.item_name = "Returned %s" %self.item_name
            self.status = "Defective"
            self.price = 0
            self. price = "{:,.2f}".format(self.price)
            return "Product: %s\nStatus: %s\nNew Price: $%s\n" %(self.item_name, self.status, self.price)
        elif self.reason == "returned in box":
            self.item_name = "Returned %s" %self.item_name
            self.status = "For Sale"
            return "Product: %s\nStatus: %s\nNew Price: $%s\n" %(self.item_name, self.status, self.price)
        elif self.reason == "opened box":
            self.item_name = "Returned %s" %self.item_name
            self.status = "Used"
            self.price = float(self.price)
            self.price -= self.price*.2
            self.price = "{:,.2f}".format(self.price)
            return "Product: %s\nStatus: %s\nNew Price: $%s\n" %(self.item_name, self.status, self.price)
    
    def Display_Info(self):
        return "Product: %s\nStatus: %s\nPrice: $%s\nWeight: %s\nBrand: %s\nCost: $%s\n" %(self.item_name, self.status, self.price, self.weight, self.brand, self.cost)


apple = Product(120,"Apple",".1lb","fuji",12) 
print apple.Display_Info()
print apple.Return("opened box")
print apple.AddTax(.06).Display_Info()



