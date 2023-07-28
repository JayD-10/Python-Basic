#to calculate addition of digits of a number
n=int(input("enter a number"))
sum=0
while n!=0:
    a=n%10
    n=n//10
    sum=sum+a
print("digit sum=",sum)
