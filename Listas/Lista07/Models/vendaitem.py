import json

class VendaItem:
    def __init__(self, id, qtd, preco, id_venda, id_produto):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_preco(preco)
        self.set_id_venda(id_venda)
        self.set_id_produto(id_produto)

    def get_id(self):        return self.__id
    def get_qtd(self):       return self.__qtd
    def get_preco(self):     return self.__preco
    def get_id_venda(self):  return self.__id_venda
    def get_id_produto(self): return self.__id_produto

    def set_id(self, id):
        if (id >0) and (id == int(id)):
            self.__id = id
        else: raise ValueError("ID deve ser um número inteiro positivo.")

    def set_qtd(self, qtd):
        if qtd > 0:
            self.__qtd = qtd
        else: raise ValueError("Quantidade deve ser um número positivo.")

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else: raise ValueError("Preço deve ser um número não negativo.")
    
    def set_id_venda(self, id_venda):
        if (id_venda >0) and (id_venda == int(id_venda)):
            self.__id_venda = id_venda
        else: raise ValueError("ID da venda deve ser um número inteiro positivo.")
    def set_id_produto(self, id_produto):
        if (id_produto >0) and (id_produto == int(id_produto)):
            self.__id_produto = id_produto
        else: raise ValueError("ID do produto deve ser um número inteiro positivo.")

    def __str__(self):
        return f"ID: {self.get_id()} - Quantidade: {self.get_qtd()} - Preço: R${self.get_preco():.2f} - ID Venda: {self.get_id_venda()} - ID Produto: {self.get_id_produto()}"
    
    def to_json(self):
        return json.dumps({
            "id": self.get_id(),
            "qtd": self.get_qtd(),
            "preco": self.get_preco(),
            "id_venda": self.get_id_venda(),
            "id_produto": self.get_id_produto()
        }, ensure_ascii=False)
    
class VendaItemDAO: #persistência de dados
    objetos = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendaitens.json", "r") as arquivo:
                data = json.load(arquivo)
                for obj in data:
                    vi = VendaItem(obj['id'], obj['qtd'], obj['preco'], obj['id_venda'], obj['id_produto'])
                    cls.objetos.append(vi)
                
        except FileNotFoundError:
            cls.objetos = []

    @classmethod
    def salvar(cls):
        with open("vendasitens.json", "w") as arquivo:
            json.dump(cls.objetos,arquivo, default= VendaItem.to_json)
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()

        if len(cls.objetos) == 0:
            id = 1
        else:
            id = max(cls.objetos, key = lambda x : x.get_id()).get_id() + 1

        obj.set_id(id)
        cls.objetos.append(obj)
        cls.salvar()

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
            x.set_qtd(obj.get_qtd())
            x.set_preco(obj.get_preco())
            x.set_id_venda(obj.get_id_venda())
            x.set_id_produto(obj.get_id_produto())
            cls.salvar()
    
    @classmethod
    def excluir(cls, id):
        obj = cls.listar_id(id)
        if obj != None:
            cls.objetos.remove(obj)
            cls.salvar()
            