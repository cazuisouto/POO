x = 5
y = 5

#id() exibe o local de memória em que o valor será armazenado
print(id(x))
print(id(y))

x = [1,2,3]
y = x
x.append(4)

print(x) #1,2,3,4
print(y) #1,2,3,4. y referencia x

x = [1,2,3]
y = [1,2,3]
x.append(4)
print(x) #1,2,3,4
print(y) #1,2,3
print(id(x))
print(id(y))