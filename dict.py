d={1:"hello",2:"Hi",'a':'welcome'}

print(d.keys())

print(d.values())

print(d.items())

print(d.get('a'))

a=d.copy()
print(a)

print(d.pop(1))

print(d)

print(d.popitem())

b={4:'welcome'}

d.update(b)

print(d)

c={'q','s','c'}

e=dict.fromkeys(c,1)
print(e)