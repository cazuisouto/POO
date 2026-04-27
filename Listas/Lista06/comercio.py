class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class ClienteDAO:
    def __init__(self):
        self.objetos = []
    def inserir(self, obj):
        self.objetos.append(obj)
    def listar(self):
        return self.objetos
    def salvar(self):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default= vars)
    def abrir(self):
        self.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                self.objetos = json.load(arquivo)
                for obj in clientes_json: