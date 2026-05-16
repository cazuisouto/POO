import json
from datetime import datetime

class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.set_id(id)
        self.set_data(data)
        self.set_carrinho(carrinho)
        self.set_total(total)
        self.set_id_cliente(id_cliente)

    def get_id(self):        return self.__id
    def get_data(self):      return self.__data
    def get_carrinho(self):   return self.__carrinho
    def get_total(self):     return self.__total
    def get_id_cliente(self): return self.__id_cliente 

    def set_id(self, id):
        if (id >0) and (id == int(id)):
            self.__id = id
        else: raise ValueError("ID deve ser um número inteiro positivo.")

    def set_data(self, data):
        if ...:
            ... #necessário validar o formato da data (ex: "dd/mm/aaaa")
        else:
            ...

    def set_carrinho(self, carrinho):
        if carrinho == bool:
            self.__carrinho = carrinho
        else: raise ValueError("Carrinho deve ser do tipo booleano.")

    def set_total(self, total):
        if total >= 0:
            self.__total = total
        else: raise ValueError("Total deve ser um número não negativo.")

    def set_id_cliente(self, id_cliente):
        if (id_cliente >0) and (id_cliente == int(id_cliente)):
            self.__id_cliente = id_cliente
        else: raise ValueError("ID do cliente deve ser um número inteiro positivo.")

    #falta o método __str__ e to_json
    #falta a classe VendaDAO para persistência de dados