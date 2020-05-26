num_list=int(input("Enter number of tuples to input in list: "))
num_tuple=int(input("Enter number of elements in each tuple: "))
list1=[]
for x in range(num_list):
    print("Enter elements of tuple no. "+str(x+1)+":")
    tuple_list=[]
    for y in range(num_tuple):
        tuple_list.append(int(input()))
    tuple1=tuple(tuple_list)
    list1.append(tuple1)
num1=int(input("Enter nth term of tuple to sort the list: "))
list1.sort(key = lambda x : x[num1])
print("Sorted list by nth index of tuple:", list1)