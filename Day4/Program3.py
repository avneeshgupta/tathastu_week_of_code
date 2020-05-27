num1=int(input("Enter no. of entries in dictionary: "))
dict1=dict()
for x in range(num1):
    key1=input("Enter key of element "+str(x+1)+": ")
    value1=int(input("Enter value of element "+str(x+1)+": "))
    dict1[key1]=value1
sorted_dict1 = dict(sorted(dict1.items(), key=lambda x: x[1]))
print("Second largest item in dictionary:",list(sorted_dict1.items())[-2])