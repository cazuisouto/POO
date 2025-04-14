class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def teste(self):
        return "Olá"
    def calc_area(self):
        return self.b * self.h / 2
    
x = Triangulo() # Executa o método __init__
y = Triangulo()

print(x)
print(x.b, x.h)

x.b = 10
x.h = 20

print(x.teste())
print(x.b, x.h)
print(x.calc_area()) #calculo de x



print(y)
print(y.teste())