str1=input("Enter a string: ")
len1=len(str1)
list1=[]
for x in range(len1):
    list1.append(str1[x])
print("String without duplicates: ",end="")
for x in range(len1):
    if str1[x] not in list1[0:x]:
        print(str1[x],end="")