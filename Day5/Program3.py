def thief_value(house_value,house_count):
    value_odd,value_even=0,0
    if house_count%2!=0:
        house_value.append(0)
        house_count+=1
    for x in range(0,house_count-1,2):
        value_odd+=house_value[x]
        value_even+=house_value[x+1]
    return max(value_even,value_odd)

house_count=int(input("Enter number of houses in line: "))
house_value=[]
for x in range(house_count):
              house_value.append(int(input("Enter value in house "+str(x+1)+": ")))
print("The maximum value stole by thief is: ",thief_value(house_value,house_count))