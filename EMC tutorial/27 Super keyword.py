class a():
    def __init__(self):
        print("A")

    def display(self):
        print("you are in class a")

class b(a):
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("you are in class b")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("you are in class c")

obj1 = c()