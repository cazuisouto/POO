import json

class Favoritos:
    def __init__(self, id, descricao, cliente_id, categoria_id):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_cliente_id(cliente_id)
        self.set_categoria_id(categoria_id)


    def get_id(self):       return self.__id
    def get_descricao(self): return self.__descricao
    def get_cliente_id(self): return self.__cliente_id
    def get_categoria_id(self): return self.__categoria_id

    def set_id(self, id):
        if (id > 0) and (id == int(id)):
            self.__id = id
        else: raise ValueError("ID deve ser um número inteiro positivo.")
    
    def set_descricao(self, descricao):
        if (len(descricao) >= 3):
            self.__descricao = descricao
        else: raise ValueError("Digite uma descrição válida (pelo menos 3 caracteres).")

    def set_cliente_id(self, cliente_id):
        if (cliente_id > 0) and (cliente_id == int(cliente_id)):
            self.__cliente_id = cliente_id
        else: raise ValueError("ID do cliente deve ser um número inteiro positivo.")

    def set_categoria_id(self, categoria_id):
        if (categoria_id > 0) and (categoria_id == int(categoria_id)):
            self.__categoria_id = categoria_id
        else: raise ValueError("ID da categoria deve ser um número inteiro positivo.")

    def __str__(self):
        return f"ID: {self.get_id()} - Descrição: {self.get_descricao()} - Cliente ID: {self.get_cliente_id()} - Categoria ID: {self.get_categoria_id()}"
    
    def to_json(self):
        return json.dumps({
            "id": self.get_id(),
            "descricao": self.get_descricao(),
            "cliente_id": self.get_cliente_id(),
            "categoria_id": self.get_categoria_id()
        })
    

class FavoritosDAO: #persistência de dados 
    objetos = []

    @classmethod
    def abrir(cls):
        try:
            with open("favoritos.json", "r") as arquivo:
                dados = json.load(arquivo)
                for obj in dados:
                    f = Favoritos(obj["id"], obj["descricao"], obj["cliente_id"], obj["categoria_id"]) 
                    cls.objetos.append(f)
        except FileNotFoundError:
            cls.objetos = []   

    
    @classmethod
    def salvar(cls):
        with open("favoritos.json", "w") as arquivo:
            json.dump(cls.objetos, arquivo, default= Favoritos.to_json) 

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
        cls.abrir()

        x = cls.listar_id(obj.get_id())

        if x != None:
            x.set_descricao(obj.get_descricao())
            x.set_cliente_id(obj.get_cliente_id())
            x.set_categoria_id(obj.get_categoria_id())
            cls.salvar()
        else: raise ValueError("Objeto não encontrado.")

    @classmethod
    def excluir(cls, id):
        cls.abrir()

        x = cls.listar_id(id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
        else: raise ValueError("Objeto não encontrado.")