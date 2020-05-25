for x in range(8):
    for y in range(8):
        if x==y:
            print("*", end="")
        elif x+y==7:
            print("*", end="")
        else:
            print(" ", end="")
    print("")