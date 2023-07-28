#To display all armstrong numbers in  1 to 1000
print("armstrong numbers in  1 to 1000")
for i in range(1,1001):
    sum=0
    ori=i
    while i!=0:
        a=i%10
        i=i//10
        sum=sum+(a*a*a)
    if(ori==sum):
        print(ori)