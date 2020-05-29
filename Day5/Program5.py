def sort_list(list1,num1):
    c=0
    for x in range(num1):
        if list1[x]%2==0:
            for y in range(x+1,num1):
                if list1[y]%2!=0:
                    list1[x],list1[y]=list1[y],list1[x]
                    c+=1
                    break
        else:
            continue
    list1=sorted(list1[:c],reverse=True)+sorted(list1[c:])
    return list1

num1=int(input("Enter total number of integer elements: "))
list1=[]
for x in range(num1):
    list1.append(int(input("Enter integer element "+str(x+1)+": ")))
print("Updated list:",sort_list(list1,num1))