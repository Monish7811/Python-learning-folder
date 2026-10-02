class laptop:
    chargertype = "Type-C"

    def __init__(self):
        self.brand = ""
        self.price = 34

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        print(self.price)

    @classmethod
    def changeChargerType(cls):
        cls.chargertype = "Type-B"
        print("Charger type changed to B")

    @staticmethod
    def info():
        print("This is the laptop class")

hp = laptop()
hp.setPrice(20000)
hp.getPrice()

laptop.changeChargerType()

hp.info()