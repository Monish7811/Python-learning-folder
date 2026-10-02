class phone:
    #government ordering every phone should be C-Type
    chargertype="Type-C" #the chargertype variable is a class variable

    def __init__(self, brand, price):
        self.brand = brand #these self.brand are instance variable
        self.price = price

    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("ChargerType:",self.chargertype)

#government ordering every phone should be B-Type
phone.chargertype = "Type-B"

#Samsung:
samsung = phone("Samsung",100000)
samsung.display()

#OPPO:
oppo = phone("OPPO", 70000)
oppo.display()

#Google:
google = phone("Pixel", 110000)
google.display()

#instances variable can be different for each objects
#class variable should be same for every object