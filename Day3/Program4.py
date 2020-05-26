len1=int(input("Enter the no. of items in list to be created: "))
list1=[]
list2=[]
print("Enter items of list:")
for x in range(len1):
    list1.append(input())
for x in range(len1):
    if list1[x] not in list1[0:x]:
        list2.append(list1[x])
print("List without duplicates:",list2)