#To check if entered mobile number is valid or not
n=int(input("enter mobile number"))
cnt=0
while n!=0:
    a=n%10
    n=n//10
    cnt=cnt+1
if cnt==10:
    print("Valid mobile number")
else:
    print("Invalid mobile number")