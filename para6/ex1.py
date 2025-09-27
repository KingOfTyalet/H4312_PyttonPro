try:
    print("start code")
    print(10/0)
    print("No errors")
except NameError:
    print("We have an error Error")
except ZeroDivisionError:
    print("We have an error div0Error")
print("code after capsule")