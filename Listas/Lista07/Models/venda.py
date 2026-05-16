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
        try:
            # converte a string para datetime
            data_convertida = datetime.strptime(data, '%d/%m/%Y')

            # salva no atributo
            self.__data = data_convertida         

        except ValueError:
            print("Data inválida! Use dd/mm/aaaa")

    def set_carrinho(self, carrinho):
        if carrinho == bool(carrinho):
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

    def __str__(self):
        return f"ID: {self.get_id()} - Data: {self.get_data().strftime('%d/%m/%Y')} - Carrinho: {self.get_carrinho()} - Total: R${self.get_total():.2f} - ID Cliente: {self.get_id_cliente()}"
    
    def to_json(self):
        return json.dumps({
            "id": self.get_id(),
            "data": self.get_data().strftime('%d/%m/%Y'),
            "carrinho": self.get_carrinho(),
            "total": self.get_total(),
            "id_cliente": self.get_id_cliente()
        },ensure_ascii=False)


class VendaDAO: #persistência de dados
    objetos = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendas.json", "r") as arquivo:
                data = json.load(arquivo)
                for obj in data:
                    v = Venda(obj['id'], obj['data'], obj['carrinho'], obj['total'], obj['id_cliente'])
                    cls.objetos.append(v)
        except FileNotFoundError:
            return cls.objetos

    @classmethod    
    def salvar(cls):
        with open("vendas.json", "w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Venda.to_json)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        if len(cls.objetos) == 0:
            id = 1
        else:
            id = max(cls.objetos, key = lambda x : x.get_id()).get_id() + 1

        obj.set_id(id)
        cls.objetos.append(obj)

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos  
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None:
            cls.set_data(obj.get_data())
            cls.set_carrinho(obj.get_carrinho())
            cls.set_total(obj.get_total())
            cls.set_id_cliente(obj.get_id_cliente())   

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
        else:
            raise ValueError("Cliente não encontrado.")
        
