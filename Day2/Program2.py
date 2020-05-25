nth=int(input("Enter nth term: "))
print("Fibonacci series")
a=0
b=1
for x in range(1, nth+1):
    if x==1:
        print(x)
    else:
        c=a+b
        a=b
        b=c
        print(c)