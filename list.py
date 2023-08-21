l1=[1,2,"Hello",3.4]
print(type(l1))

print(l1[0:])

print(l1[:])

print(l1[2:4])

print(l1[:4])

print(l1[1:4:2])

print(l1[-1])

print(l1[-3:-1])

l1[2]=10
print(l1)
l1[2:4]=[89,36]
print(l1)

l2=[]
n=int(input("Enter no of elements:"))

for i in range(0,n):
    l2.append(input("Enter elements:"))

print(l2)   


print("\nlength of list:",len(l2))

print("\nmaximum of list:",max(l2))

print("\nminimum of list:",min(l2))