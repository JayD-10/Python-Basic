#To count number of consonants
s=input("enter a string")
i=0
cnt=0
for i in range(0,len(s)):
    x=ord(s[i])
    if x>=65 and x<=90 or x>=97 and x<=122:
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
            a=1
        else:
            cnt=cnt+1
print("no of consonants in the string are=",cnt)


