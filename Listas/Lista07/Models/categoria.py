import json

class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)

    def get_id(self):          return self.__id
    def get_descricao(self):   return self.__descricao

    def set_id(self, id):
        if (id > 0) and (id == int(id)):
            self.__id = id
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")
    
    def set_descricao(self, descricao):
        if (len(descricao) >= 3) and (isinstance(descricao, str)):
            self.__descricao = descricao
        else:
            raise ValueError("Digite uma descrição válida (pelo menos 3 caracteres).")
        
    def __str__(self):
        return f"ID: {self.get_id()} - Descrição: {self.get_descricao()}"
    
    def to_json(self):
        return json.dumps({
            "id": self.get_id(),
            "descricao": self.get_descricao()
        }, ensure_ascii=False)

class CategoriaDAO: #persistência de dados 
    objetos = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("categorias.json", "r") as arquivo:
                dados = json.load(arquivo)
                for obj in dados:
                    c = Categoria(obj["id"], obj["descricao"]) 
                    cls.objetos.append(c)
        except FileNotFoundError:
            cls.objetos = []   

    
    @classmethod
    def salvar(cls):
        with open("categorias.json", "w") as arquivo:
            json.dump(cls.objetos, arquivo, default= Categoria.to_json) 
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
            cls.salvar()
        else:
            raise ValueError("Categoria não encontrada.")
        
    @classmethod
    def excluir(cls, id):
        cls.abrir()

        x = cls.listar_id(id)

        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
        else:
            raise ValueError("Categoria não encontrada.")
        