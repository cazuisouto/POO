import json

class Produto:
    
    #construtor da classe Produto
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)

    def __str__(self):
        return f"{self.id} - {self.descricao} - R$ {self.preco:.2f} - estoque: {self.estoque}"


    #Métodos set 
    def set_id(self, id):
        if not isinstance(id, int):                                          #verifica se o tipo do id é inteiro
            raise ValueError("ID deve ser um inteiro.")                      #retorna um erro caso o id não seja inteiro
        self._id = id                                                        #atributo para armazenar o id do produto

    def set_nome(self, nome):                                                
        if not isinstance(nome, str):                                        #verifica se o tipo do nome é string
            raise ValueError("Nome deve ser uma string.")                    #retorna um erro caso o nome não seja string
        self._nome = nome                                                    #atributo para armazenar o nome do produto

    def set_preco(self, preco):                                              
        if not isinstance(preco, float):                                     #verifica se o tipo do preco é float
            raise ValueError("Preço deve ser um float.")                     #retorna um erro caso o preco não seja float
        self._preco = preco                                                  #atributo para armazenar o preco do produto

    def set_estoque(self, estoque):                                         
        if not isinstance(estoque, int):                                     #verifica se o tipo do estoque é inteiro
            raise ValueError("estoque deve ser um inteiro.")                 #retorna um erro caso o estoque não seja inteiro
        self._estoque = estoque                                              #atributo para armazenar o estoque do produto

    def set_id_categoria(self, id_categoria):
        if not isinstance(id_categoria, int):                                #verifica se o tipo do id_categoria é inteiro
            raise ValueError("ID da categoria deve ser um inteiro.")         #retorna um erro caso o id_categoria não seja inteiro
        self._id_categoria = id_categoria                                    #atributo para armazenar o id da categoria do produto

    #Métodos get
    def get_id(self): return self.__id = id                                         #retorna o id do produto
    def get_descricao(self): return self.__descricao = descricao                    #retorna a descricao do produto
    def get_preco(self): return self.__preco = preco                                #retorna o preco do produto
    def get_estoque(self): return self.__estoque = estoque                          #retorna o estoque do produto
    def get_id_categoria(self): return self.__id_categoria = id_categoria           #retorna o id da categoria do produto

    #Método para converter o objeto Produto em um dicionário JSON.
    def to_json(self):
        return{
            "id": self.id,
            "descricao": self.descricao,
            "preco": self.preco,
            "estoque": self.estoque,
            "id_categoria": self.id_categoria
        }   
    
    #Método estático para criar um objeto Produto a partir de um dicionário JSON.
    @staticmethod
    def from_json(dic):
        return Produto(
            dic["id"],
            dic["descricao"],
            dic["preco"],
            dic["estoque"],
            dic["id_categoria"]
        )   

#Classe de Acesso a Dados (DAO) para a classe Produto. Responsável por gerenciar a persistência dos objetos Produto em um arq JSON.
class ProdutoDAO:
    objetos = []                                          #Lista para armazenar os objetos Produto em memória

    @classmethod                                        
    def inserir(cls, obj):                               
        cls.abrir()                                      #Chama o método abrir
        id = 0                                           #Inicializa o id como 0
        for aux in cls.objetos:                          #Percorre a lista de objetos Produto
            if aux.id  > id:                             #Verifica se o id do objeto atual é maior que o id armazenado       
                id = aux.id                              #Atualiza o id armazenado
        obj.id = id + 1                                  #Incrementa o id para o novo objeto
        cls.objetos.append(obj)                          #Adiciona o novo objeto à lista
        cls.salvar()                                      #Chama o método salvar                            
    
    @classmethod
    def listar(cls):
        cls.abrir()                                       #Chama o método abrir
        return cls.objetos                                #Retorna a lista de objetos Produto
    
    @classmethod
    def lista_id(cls, id):
        cls.abrir()                                       #Chama o método abrir
        for obj in cls.objetos:                           #Percorre a lista de objetos Produto
            if obj.id == id:                              #Verifica se o id do objeto atual é igual ao id fornecido
                return obj                                #Retorna o objeto Produto correspondente ao id
        return None                                       #Retorna None se nenhum objeto for encontrado com o id fornecido 
    
    @classmethod
    def atualizar(cls, obj):                            #Atualiza um objeto Produto existente
        aux = cls.lista_id(obj.id)                        #Busca o objeto pelo id                     
        if aux is not None:                              #Verifica se o objeto foi encontrado                       
            cls.objetos.remove(aux)                      #Remove o objeto antigo
            cls.objetos.append(obj)                      #Adiciona o objeto atualizado     
            cls.salvar()                                 #Salva as alterações
    
    @classmethod
    def deletar(cls, obj):                               #Deleta um objeto Produto existente
        aux = cls.lista_id(obj.id)                       #Busca o objeto pelo id                      
        if aux is not None:                              #verifica se o objeto foi encontrado                        
            cls.objetos.remove(aux)                      #Remove o objeto da lista      
            cls.salvar()                                 #Salva as alterações
    
    @classmethod
    def salvar(cls):                                     #Salva os objetos Produto em um arq JSON
        with open("produto.json", "w") as arq:        #Abre o arq JSON em modo de escrita
            json
    
    @classmethod
    def abrir(cls):                                      #Abre o arq JSON e carrega os objetos Produto na memória
       try:
           with open("produto.json", "r") as arq:      #Abre o arq JSON em modo de leitura
               dados = json.load(arq)                  #Carrega os dados do arq JSON
               for dic in dados:
                     p = Produto.from_json(dic)          #Cria um objeto Produto a partir do dicionário
                     cls.objetos.append(p)                #Adiciona o objeto à lista
        except:
            return False                             #Retorna False se o arq JSON não existir
    