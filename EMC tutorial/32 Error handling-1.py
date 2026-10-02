try:
    a = int(input())
    b = int(input())
    print(a+b)

except Exception as e:
    print("Please write two numbers.",e)