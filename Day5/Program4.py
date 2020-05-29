def knapsack(wt,list1):
    if wt==0 or len(list1)==0:
        return 0
    if len(list1)==1:
        if list1[0][0]>wt:
            return 0 
        return list1[0][1]  
    if list1[0][0]>wt:
        return knapsack(wt,list1[1:])
    return max(list1[0][1]+knapsack(wt-list1[0][0],list1[1:]),knapsack(wt, list1[1:]))

num1=int(input("Enter the number of items: "))
list1=[]
for x in range(num1):
    wt = int(input("Enter weight of item "+str(x+1)+": "))
    val = int(input("Enter value of item "+str(x+1)+": "))
    list1.append((wt,val))

wt = int(input("Enter the weight capacity: "))
print("The maximum value is:",knapsack(wt,list1))