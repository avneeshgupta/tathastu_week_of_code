def replace_int(a):
    print("Replaced number: ",end="")
    list1=list(a)
    for x in list1:
        if x=='0':
            print("5",end="")
        else:
            print(x,end="")
replace_int(input("Enter a number: "))