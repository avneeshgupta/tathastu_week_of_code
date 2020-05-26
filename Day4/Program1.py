len1=int(input("Enter the no. of items in tuple to be created: "))
list1=[]
print("Enter items of tuple:")
for x in range(len1):
    list1.append(input())
tuple1=tuple(list1)
input1=input("Enter element to be counted: ")
print("No. of occurence of given element:",tuple1.count(input1))