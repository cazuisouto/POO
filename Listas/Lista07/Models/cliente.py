import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def get_id(self):          return self.__id
    def get_nome(self):        return self.__nome
    def get_email(self):       return self.__email
    def get_fone(self):        return self.__fone
    def get_senha(self):       return self.__senha

    def set_id(self, id):
        if (id > 0) and (id == int(id)):
            self.__id = id
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")
        
    def set_nome(self, nome):
        if (nome != "") and (isinstance(nome, str)):
            self.__nome = nome
        else:
            raise ValueError("Nome deve ser do tipo string  e não pode ser vazia.")
        
    def set_email(self, email):
        if (email != "") and ("@" in email) and ("." in email) and (isinstance(email, str)):
            self.__email = email
        else:
            raise ValueError("Digite um email válido.")
    
    def set_fone(self, fone):
        if (fone !="") and (len(fone) >= 8) and (len(fone) <= 15):
            self.__fone = fone
        else:
            raise ValueError("Digite um número de telefone válido (entre 8 e 15 dígitos).")
        
    def set_senha(self, senha):
        if (senha != "") and (len(senha) >= 6):
            self.__senha = senha
        else:
            raise ValueError("A senha deve conter pelo menos 6 caracteres.")
        

    def __str__(self):
        return f"ID: {self.get_id()} - Nome: {self.get_nome()} - Email: {self.get_email()} - Telefone: {self.get_fone()}"
    
    def to_json(self):
        return json.dumps({
            "id": self.get_id(),
            "nome": self.get_nome(),
            "email": self.get_email(),
            "fone": self.get_fone(),
            "senha": self.get_senha()
        }, ensure_ascii=False)
    

class ClienteDAO:
    objetos = []
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", "r") as arquivo:
                dados = json.load(arquivo)
                for obj in dados:
                    cliente = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
                    cls.objetos.append(cliente)
        except FileNotFoundError:
            cls.objetos = []

    @classmethod
    def salvar(cls):
        with open("clientes.json", "w") as arquivo:
            json.dump(cls.objetos,arquivo, default= Cliente.to_json)

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
        cls.objetos.sort(key = lambda x : x.get_nome())
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
            x.set_nome(obj.get_nome())
            x.set_email(obj.get_email())
            x.set_fone(obj.get_fone())
            x.set_senha(obj.get_senha())
            cls.salvar()
        else:
            raise ValueError("Cliente não encontrado.")
            
    @classmethod
    def excluir(cls, id):
        x = cls.listar_id(id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
        else:
            raise ValueError("Cliente não encontrado.")
            