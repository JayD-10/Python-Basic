#To check if entered number is a lead number
n=int(input("enter a number"))
ori=n
sum_ev=0
sum_odd=0
while n!=0:
    a=n%10
    n=n//10
    if(a%2==0):
        sum_ev=sum_ev+a
    else:
        sum_odd=sum_odd+a
if sum_ev==sum_odd:
    print(ori, "is a lead number.")
else:
    print(ori,"is not a lead number")
