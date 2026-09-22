a={
    "name":"Monish",
    "age":12,
    "location":"Chennai"
}

a["age"] = 13 #modifying the age from 12 to 13
a["colour"] = "red" #adding new keys and values
a.update({"colour":"blue"}) #updating colour from red to blue
del a["location"] #deletes the key location, can also use a.pop("location") for this

print(a)