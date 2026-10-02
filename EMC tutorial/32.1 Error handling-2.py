try:
    a = input()
    b = input()
    print(a/b)

except Exception as e:
    print("Strings can't be used in operations.", e)