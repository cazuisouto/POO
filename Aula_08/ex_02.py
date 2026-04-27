from enum import Enum
class Estacao(Enum):
    PRIMAVERA = 1
    VERÃO = 2
    OUTONO = 3
    INVERNO = 4

a = Estacao.PRIMAVERA
b = Estacao['INVERNO']
c = Estacao(3)