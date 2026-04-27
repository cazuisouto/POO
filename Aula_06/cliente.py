class Cliente:
    def __init__(self, nome, cpf, limite):
        self.__nome = nome
        self.__cpf = cpf
        self.__limite = limite
        self.__socio = None
    def set_socio(self, aux):
        if self.__socio != None:   # a.set_socio(c) self = a, aux = c
            #x = self.__socio      # x é o sócio de a
            #x.__socio = None
            self.__socio.__socio = None
        if aux.__socio != None:
            aux.__socio.__socio = None
        self.__socio = aux  
        aux.__socio = self  
    def get_limite(self):
        if self.__socio == None: return self.__limite
        return self.__limite + self.__socio.__limite
    def __str__(self):
        if self.__socio == None: return f"{self.__nome} {self.__cpf} {self.__limite}"
        return f"{self.__nome} {self.__cpf} {self.__socio.__nome} {self.__limite} {self.get_limite()}"
        

a = Cliente("Gilbert", "1234", 1000)
b = Cliente("Eduardo", "4321", 500)
c = Cliente("Jorgiano", "8888", 5000)
d = Cliente("Lucena", "9999", 2000)
print(a)
print(b)
print(c)
print(d)
print()

a.set_socio(b)
c.set_socio(d)
print(a)
print(b)
print(c)
print(d)
print()

a.set_socio(c)
print(a)
print(b)
print(c)
print(d)