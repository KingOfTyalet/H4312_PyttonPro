try:
    try:
        print("start code")
        #print(asdadad)
        print("No errors")
    except SyntaxError:
        print("We have an error SyntaxError")
except NameError as error:
    print(error)
else:
    print("No problem")
print("code after capsule")