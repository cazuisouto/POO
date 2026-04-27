import enum

class Dia(enum.IntFlag):
    Domingo = 1
    Segunda = 2
    Terca = 4
    Quarta = 8
    Quinta = 16
    Sexta = 32
    Sabado = 64

a = Dia(0)
b = Dia.Sexta
c = Dia.Segunda | Dia.Sexta
d = Dia.Sabado | Dia.Domingo

print(a) # Dia.0
print(b) # Dia.Sexta
print(c) # Dia.Sexta|Segunda
print(d) # Dia.Sabado|Domingo