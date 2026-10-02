class dad():
    def phone(self):
        print("Dad's Phone")

class mom():
    def sweet(self):
        print("Mom's Sweet")

class son(dad,mom):
    def laptop(self):
        print("Son's laptop")

ram = son()
ram.laptop()
ram.phone()
ram.sweet()