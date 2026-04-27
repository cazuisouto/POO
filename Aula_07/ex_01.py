x = []
print(type(x))
print(len(x))
print(x)
x.append(10)
x.append(20)
x.append(15)
print(len(x))
print(x)
print(x[0])

y = x
y.append(40)
print(x)

y = x[:]
y.append(50)
print(x)
print(*x)

#print(x[10])
#print(int("Teste"))

x = [1, 2, 3, 4, 5, 0]
for i in x:
    print(x[i])

print(sorted(x))
print(x)
print(x.sort())
print(x)