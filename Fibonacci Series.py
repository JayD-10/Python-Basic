#To print the fibonacci series upto 10 terms
a=0
b=1
print(a,end=",")
print(b,end=",")
for i in range(1,11):
    c=a+b
    print(c,end=",")
    a=b
    b=c
print("\n is the fibonacci series")