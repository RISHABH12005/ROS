a=int(input("enter the no."))
b=int(input("enter the no."))
temp=a
a=b
b=temp
print(a,b)
a,b=b,a
print(a,b)
