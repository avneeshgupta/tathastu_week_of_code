c=0
for x in range(5):
    for y in range(11):
        if x+y<5:
            print("*",end="")
        elif x+y>5+c:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    c+=2
c=1
for x in range(5):
    for y in range(11):
        if x+y<c:
            print("*",end="")
        elif x+y>9:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    c+=2