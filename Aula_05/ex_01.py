class Triangulo:
    def __init__(self, b, h):             # init - Define os atributos do objeto
        self.set(b)
        self.set(h)
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError("Valor não pode ser negativo")
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError("Valor não pode ser negativo")
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):            # método que realiza uma operação com os dados do objeto
        return self.__b * self.__h / 2 
    def __str__(self):
        return f"Triangulo com base = {self.__b} e altura = {self.__h}"

# Interface do Usuário - Visão
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
    @staticmethod
    def menu():
        print("1 - Triângulo, 9 - Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def triangulo():
        x = Triangulo(float(input("Informa a base do triângulo: ")), float(input("Informa a altura: ")))
        print(x)
        print(f"A área do triângulo de base {x.get_base()} e altura {x.get_altura()} é {x.calc_area()}")

UI.main()