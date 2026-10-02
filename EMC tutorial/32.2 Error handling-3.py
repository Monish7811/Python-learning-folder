try:
    a=int(input())
    b=int(input())
    c=input()
    # print(c/a)
    # print(d)
    print(a+b)

except ValueError as e:
    print("Value Error", e)

except TypeError as e:
    print("Type Error", e)

except Exception:
    print("Something")

finally:
    print("Done")