class Triangulo:
    def __init__(self):             # init - Define os atributos do objeto
        self.b = 0
        self.h = 0
    def calc_area(self):            # método que realiza uma operação com os dados do objeto
        return self.b * self.h / 2    
x = Triangulo()
y = Triangulo()
z = x
print(x, x.b, x.h)
print(y, y.b, y.h)
print(z, z.b, z.h)

print(id(x.b))
print(id(x.h))
print(id(y.b))
print(id(y.h))

x.b = 10
x.h = 20
y.b = 30
y.h = 40
print(x, x.b, x.h, x.b * x.h / 2)
print(y, y.b, y.h, y.b * y.h / 2)
print(x, x.b, x.h, x.calc_area())
print(y, y.b, y.h, y.calc_area())
print(z, z.b, z.h, z.calc_area())

print(id(x.b))
print(id(x.h))
print(id(y.b))
print(id(y.h))
a = 0
b = 0
print(id(a))
print(id(b))

c = int(10)
print(c)
d = 10
print(d)