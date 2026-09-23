class laptop:
    price = 0
    processor = ""
    ram = ""

hp = laptop()
dell = laptop()
lenova = laptop()

#hp:
hp.price = 50000
hp.processor = "i5"
hp.ram = "8GB"

#dell:
dell.price = 100000
dell.processor = "i7"
dell.ram = "16GB"

#lenova:
lenova.price = 70000
lenova.processor = "i6"
lenova.ram = "12GB"

print(hp.price)
print(dell.price)
