#to check if no. is armstrong no.
n=int(input("enter a number"))
ori=n
sum=0
while n!=0:
    a=n%10
    n=n//10
    sum=sum+(a*a*a)
if(ori==sum):
    print("Armstrong no.")
else:
    print("Not a armstrong no.")