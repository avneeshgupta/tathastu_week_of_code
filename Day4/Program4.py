num1=int(input("Enter no. of entries in dictionary: "))
dict1=dict()
for x in range(num1):
    key1=input("Enter key of element "+str(x+1)+": ")
    value1=int(input("Enter value of element "+str(x+1)+": "))
    dict1[key1]=value1
new_dict1=dict()
for key,value in dict1.items():
    if value not in new_dict1.values():
        new_dict1[key]=value
print("New dictionary after removing duplicate values:\n",new_dict1)