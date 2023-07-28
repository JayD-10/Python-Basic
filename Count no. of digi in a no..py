#To count the number of digits in a number
n=int(input("enter a number"))
cnt=0
while n!=0:
    a=n%10
    n=n//10
    cnt=cnt+1
print("number of digits=",cnt)