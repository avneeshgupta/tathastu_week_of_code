num=int(input("Enter a no.: "))



if num%2==0:
    print("Number is even")
else:
    print("Number is odd")
c=0



for x in range(1, num):
    if num%x==0:
        c+=1
if c==1:
    print("Number is prime")
else:
    print("Number is not prime")



num1=num
rev=0
while num1>0:
    rem=num1%10
    rev=(rev*10)+rem
    num1=num1//10
if rev==num:
    print("Number is pallindrome")
else:
    print("Number is not pallindrome")



num2=num
num3=0
while num2>0:
    dig=num2%10
    num3+=(dig**3) 
    num2=num2//10
if num3==num:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
