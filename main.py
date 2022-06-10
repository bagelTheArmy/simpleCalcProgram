exit = False
while not exit:

    x = input("enter a number with two decimal places -1 to exit:")
    if not x == "-1":
        try:
            num = float(x)
            finalNum = num + 2
            finalNum = finalNum + 10
            finalNum = finalNum + num * .20
            print(finalNum)
        except:
            print("not a float var")
    else:
        exit = True
