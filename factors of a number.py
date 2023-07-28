#to print factors of a number
n=int(input("enter a number"))
i=1
print("factors are")

while i<=n:
    if n%i==0:
        print(i)
    i=i+1
