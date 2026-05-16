import json

class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)

    def get_id(self):        return self.__id
    def get_descricao(self): return self.__descricao
    def get_preco(self):     return self.__preco
    def get_estoque(self):   return self.__estoque
    def get_id_categoria(self): return self.__id_categoria

    def set_id(self, id):
        if (id >0) and (id == int(id)):
            self.__id = id
        else: raise ValueError("ID deve ser um número inteiro positivo.")

    def set_descricao(self, descricao):
        if len(descricao) > 0:
            self.__descricao = descricao
        else: raise ValueError("Descrição deve conter pelo menos um caractere.")

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else: raise ValueError("Preço deve ser um número não negativo.")

    def set_estoque(self, estoque):
        if estoque >= 0:
            self.__estoque = estoque
        else: raise ValueError("Estoque deve ser um número não negativo.")

    def set_id_categoria(self, id_categoria):
        if (id_categoria >0) and (id_categoria == int(id_categoria)):
            self.__id_categoria = id_categoria
        else: raise ValueError("ID da categoria deve ser um número inteiro positivo.")
    
    def __str__(self):
        return f"ID: {self.get_id()} - Descrição: {self.get_descricao()} - Preço: R${self.get_preco():.2f} - Estoque: {self.get_estoque()} - ID Categoria: {self.get_id_categoria()}"
    
    def to_json(self):
        return json.dumps({
            "id": self.get_id(),
            "descricao": self.get_descricao(),
            "preco": self.get_preco(),
            "estoque": self.get_estoque(),
            "id_categoria": self.get_id_categoria()
        }, ensure_ascii=False)
    

class ProdutoDAO: #persistência de dados
    objetos = []

    @classmethod
    def abrir(cls):
        objetos = []
        try:
            with open("produtos.json", "r") as arquivo:
                dados = json.load(arquivo)
                for obj in dados:
                    p = Produto(obj['id'], obj['descricao'], obj['preco'], obj['estoque'], obj['id_categoria'])
                    cls.objetos.append(p)
        except FileNotFoundError:
            cls.objetos = []

    @classmethod
    def salvar(cls):
        with open("produtos.json", "w") as arquivo:
            json.dump(cls.objetos,arquivo, default= Produto.to_json)

    @classmethod
    def inserir(cls, obj):
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
            x.set_descricao(obj.get_descricao())
            x.set_preco(obj.get_preco())
            x.set_estoque(obj.get_estoque())
            x.set_id_categoria(obj.get_id_categoria())
            cls.salvar()
        else: raise ValueError("Produto não encontrado para atualização.")

    @classmethod
    def excluir(cls, id):
        x = cls.listar_id(id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
        else: raise ValueError("Produto não encontrado para exclusão.")
        
      