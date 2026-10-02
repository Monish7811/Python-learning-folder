class grandpa():
    def phone(self):
        print("grandpa's phone")

class dad(grandpa):
    def money(self):
        print("dad's money")

class son(dad):
    def laptop(self):
        print("Son's laptop")

d1 = dad()
d1.phone()

s1 = son()
s1.money()
s1.phone()