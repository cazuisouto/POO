class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2
    
x = Triangulo()

x.b = 10
x.h = 20
print(x.b, x.h, x.calc_area())

y = Triangulo()
y.b = 5
y.h = 15
print(y.b, y.h, y.calc_area())

z = x
z.b = 40
z.h = 50
print(z.b, z.h, z.calc_area())
print(x.b, x.h, x.calc_area())
