c=3
for x in range(3):
    for y in range(5):
        if y<(c*2)-1:
            if y%2==0:
                print(c,end="")
            else:
                print("*",end="")
    print("")
    c-=1

c=1
for x in range(3):
    for y in range(5):
        if y<(c*2)-1:
            if y%2==0:
                print(c,end="")
            else:
                print("*",end="")
    print("")
    c+=1