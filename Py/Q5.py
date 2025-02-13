n=input("Enter")
l=len(n)
print(l)
for i in n:
    temp=ord(i)+2
    print(chr(temp),end="")