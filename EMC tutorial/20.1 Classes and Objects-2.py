class goa:
    name=""
    drink=""
    def party(self):
        print("Let's Party.....")
    def beach(self):
        print("Enjoying the beach.")

ramesh = goa()
suresh = goa()

ramesh.name = "Ramesh" #each object has its own space in class if i done anything in one object it will not be saved in another object
ramesh.drink = "Yes"
suresh.name = "Suresh"
suresh.drink = "No"


#Suresh object:
print(ramesh.name)
print("Drink:",ramesh.drink)
ramesh.party()

#Ramesh object:
print(suresh.name)
print("Drink:",suresh.drink)
suresh.beach()