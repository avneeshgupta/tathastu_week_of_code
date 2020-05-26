len1=int(input("Enter the no. of items in 1st list to be created: "))
len2=int(input("Enter the no. of items in 2nd list to be created: "))
list1=[]
list2=[]
list3=[]
print("Enter items of 1st list:")
for x in range(len1):
    list1.append(input())
print("Enter items of 2nd list:")
for x in range(len2):
    list2.append(input())
for x in range(len1):
    if list1[x] not in list1[0:x] and list1[x] in list2:
        list3.append(list1[x])
print("Intersection of lists:",list3)