# Use of List,Append,Extend,Remove,Count,Key,Pop,Get,Values
list=[95,56,78,70,54,23,60]
print(list)
print(list[-1])
print(list[0:2])
print(list[0:4:3])
print(list[0:-4:1])

shop=[95,56,78,70,54,23,60]
print('shop=',shop)

a=[1,3,5]
a.append(2)
print(a)

a.extend([6,7])
print(a)

a.remove(1)
print(a)

a.pop(-2)
print(a)

l=[1,1,2,3,2,4,5,4,5,4,6,]
print(l.count(1))
print(l.count(4))

B={11:'YESH',12:'SAGAR',13:'PEYUSH',14:'ARYAN'}
print(B.keys())
print(B.values())
print(B.get(11))
