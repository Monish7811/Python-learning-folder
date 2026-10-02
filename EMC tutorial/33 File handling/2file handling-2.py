f = open("fruits.txt","w")
f.write("Banana\n")
f.write("Mango\n")
f.close

f = open("fruits.txt","r+")
content = f.read()
print(content)