import json

class Cliente:
    def __init__(self,id, nome, email, senha, telefone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
        self.set_telefone(telefone)
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.telefone}"
    
    #Métodos Get e Set

    def set_id(self, id):
        if not isinstance(id, int):                                           #isinstance verifica se o tipo do id é inteiro
            raise ValueError("ID deve ser um inteiro.")                       #retorna um erro caso o id não seja inteiro
        self._id = id                                                         #atributo para armazenar o id do cliente    
    def get_id(self):                                                         #retorna o id do cliente
        return self._id

    def set_nome(self, nome):
        if not isinstance(nome, str):                                        #verifica se o tipo do nome é string
            raise ValueError("Nome deve ser uma string.")                    #retorna um erro caso o nome não seja string
        self._nome = nome                                                    #atributo para armazenar o nome do cliente
    def get_nome(self):                                                      #retorna o nome do cliente
        return self._nome 
    
    def set_email(self, email):
        if not isinstance(email, str):                                       #verifica se o tipo do email é string
            raise ValueError("Email deve ser uma string.")                   #retorna um erro caso o email não seja string
        self._email = email                                                 #atributo para armazenar o email do cliente
    def get_email(self):                                                     #retorna o email do cliente
        return self._email
    
    def set_senha(self, senha):
        if not isinstance(senha, str):                                      #verifica se o tipo da senha é string
            raise ValueError("Senha deve ser uma string.")                  #retorna um erro caso a senha não seja string
        self._senha = senha                                                #atributo para armazenar a senha do cliente
    def get_senha(self):                                                    #retorna a senha do cliente
        return self._senha 
    
    def set_telefone(self, telefone):
        if not isinstance(telefone, str):                                   #verifica se o tipo do telefone é string
            raise ValueError("Telefone deve ser uma string.")               #retorna um erro caso o telefone não seja string
        self._telefone = telefone                                          #atributo para armazenar o telefone do cliente
    def get_telefone(self):                                                 #retorna o telefone do cliente
        return self._telefone
    
    #Método para converter o objeto Cliente em um dicionário JSON.
    def to_json(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone
        }
    
    #Método estático para criar um objeto Cliente a partir de um dicionário JSON.
    @staticmethod
    def from_json(dic):
        return Cliente(
            dic["id"],
            dic["nome"],
            dic["email"],
            dic["senha"],
            dic["telefone"]
        )
    
#Classe de Acesso a Dados (DAO) para a classe Cliente. Responsável por gerenciar a persistência dos objetos Cliente em um arquivo JSON.
class ClienteDAO:
    objetos = []                                          #Lista para armazenar os objetos Cliente em memória

    @classmethod
    def inserir(cls, obj):
        cls.abrir()                                      #Chama o método abrir
        id = 0                                           #Inicializa o id como 0
        for aux in cls.objetos:                          #Percorre a lista de objetos Cliente
            if aux.get_id() > id:                        #Verifica se o id do objeto atual é maior que o id armazenado       
                id = aux.get_id()                        #Atualiza o id armazenado
        obj.set_id(id + 1)                               #Incrementa o id para o novo objeto
        cls.objetos.append(obj)                          #Adiciona o novo objeto à lista
        cls.salvar()                                     #Chama o método salvar

    @classmethod
    def listar(cls):
        cls.abrir()                                      #Chama o método abrir
        return cls.objetos                               #Retorna a lista de objetos Cliente
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()                                      #Chama o método abrir
        for obj in cls.objetos:                          #Percorre a lista de objetos Cliente
            if obj.get_id() == id:                       #Verifica se o id do objeto atual é igual ao id fornecido
                return obj                               #Retorna o objeto Cliente correspondente
        return None                                     #Retorna None se nenhum objeto for encontrado com o id fornecido
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())                #Chama o método listar_id para encontrar o objeto a ser atualizado
        if aux is not None:                              #Verifica se o objeto foi encontrado
           cls.objetos.remove(aux)                         
           cls.objetos.append(obj)                       #Adiciona o objeto atualizado
        cls.salvar()                                     #Chama o método salvar

    @classmethod
    def deletar(cls, obj):
        aux = cls.listar_id(obj.id)                      #Chama o método listar_id para encontrar o objeto a ser deletado
        if aux is not None:                              #Verifica se o objeto foi encontrado
            cls.objetos.remove(aux)                      #Remove o objeto da lista
        cls.salvar()                                     #Chama o método salvar

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []                          #Inicializa a lista de objetos como vazia
            with open("cliente.json", "r") as arq:
                dados = json.load(arq)                 #Carrega os dados do arquivo JSON
                for dic in dados:                       #Percorre cada dicionário no arquivo JSON
                    obj = Cliente.from_json(dic)       #Cria um objeto Cliente a partir do dicionário
                    cls.objetos.append(obj)             #Adiciona o objeto à lista  
        except:
            return False                            #Retorna False se o arquivo JSON não existir