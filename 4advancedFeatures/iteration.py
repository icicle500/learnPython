#list,tuple,dict好多都可以使用迭代
a = [1,2,3,4,5]
for x in a:
    print(x)

print('\n')
b = {'a':1,'b':2,'c':3}
for x in b:
    print(x)

for x in b.values(): #迭代value
    print(x)

for x,y in b.items(): #同时迭代key和value
    print(x,y)