def replace_element(list1):
    for x in range(size1):
        for y in range(x+1,size1):
            if list1[y]>list1[x]:
                list1[x]=list1[y]
    return list1

size1=int(input("Enter number of elements in list: "))
list1=[]
print("Enter int elements of list:")
for x in range(size1):
    list1.append(int(input("Enter element "+str(x+1)+": ")))
print("New list:", replace_element(list1))