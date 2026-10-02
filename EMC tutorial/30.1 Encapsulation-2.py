class company():
    def __init__(self):
        self._companyName = "Google"

class b(company):
    pass

b1 = b()

print(b1._companyName)