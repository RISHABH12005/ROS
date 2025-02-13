r=""
s=input()
for i in s:
    r=r+str((int(i)+1)%10)
print(r)
