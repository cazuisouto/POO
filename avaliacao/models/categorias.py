import json

class Categoria:
    #Construtor, inicializa os atributos da classe. Onde 'id' é um identificador único para a categoria e 'descricao' é uma descrição textual da categoria.
    #id é inteiro e descricao é string.

    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)

    #Métodos set 
    def set_id(self, id):
        if not isinstance(id, int):                            #isinstance verifica se o tipo do id é inteiro
            raise ValueError("ID deve ser um inteiro.")        #retorna um erro caso o id não seja inteiro
        self._id = id                                          #atributo para armazenar o id da categoria
    def set_descricao(self, descricao):
        if not isinstance(descricao, str):                      #verifica se o tipo da descricao é string
            raise ValueError("Descrição deve ser uma string.")  #retorna um erro caso a descricao não seja string
        self._descricao = descricao                             #atributo para armazenar a descricao da categoria

    #Métodos get
    def get_id(self):
        return self._id                                        #retorna o id da categoria
    def get_descricao(self):
        return self._descricao                                 #retorna a descricao da categoria    
    
    #Representação em string da categoria. Exibe o id e a descrição da categoria formatados.
    def __str__(self):
        return f"{self.get_id()} - {self.get_descricao()}"
    
    #Método para converter o objeto Categoria em um dicionário JSON.
    def to_json(self):
        return { "id": self.get_id(), "descricao": self.get_descricao() }
    
    #Método estático para criar um objeto Categoria a partir de um dicionário JSON.
    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"]) 

#Classe de Acesso a Dados (DAO) para a classe Categoria. Responsável por gerenciar a persistência dos objetos Categoria em um arquivo JSON.
    class CategoriaDAO:
        objeto = []                                          #Lista para armazenar os objetos Categoria em memória

        @classmethod                                        
        def inserir(cls, obj):                               
            cls.abrir()                                      #Chama o método abrir
            id = 0                                           #Inicializa o id como 0
            for aux in cls.objeto:                           #Percorre a lista de objetos Categoria
                if aux.get_id() > id:                        #Verifica se o id do objeto atual é maior que o id armazenado       
                    id = aux.get_id()                        #Atualiza o id armazenado
            obj.set_id(id + 1)                               #Incrementa o id para o novo objeto
            cls.objeto.append(obj)                           #Adiciona o novo objeto à lista
            cls.salvar()                                 
        
        @classmethod
        def listar(cls):
            cls.abrir()                                      #Chama o método abrir
            return cls.objeto                                #Retorna a lista de objetos Categoria
        
        classmethod
        def listar_id(cls, id):
            cls.abrir()                                      #Chama o método abrir
            for obj in cls.objeto:                           #Percorre a lista de objetos Categoria
                if obj.get_id() == id:                       #Verifica se o id do objeto atual é igual ao id fornecido
                    return obj                               #Retorna o objeto encontrado
            return None                                      #Retorna None se nenhum objeto for encontrado

        @classmethod
        def atualizar(cls, obj):                            #Atualiza um objeto Categoria existente
            aux = cls.listar_id(obj.get_id())               #Busca o objeto pelo id                     
            if aux is not None:                             #Verifica se o objeto foi encontrado                       
                cls.objeto.remove(aux)                      #Remove o objeto antigo
                cls.objeto.append(obj)                      #Adiciona o objeto atualizado     
                cls.salvar()                                #Salva as alterações      
        
        @classmethod
        def deletar(cls, obj):                             #Deleta um objeto Categoria existente
            aux = cls.listar_id(obj.get_id())              #Busca o objeto pelo id                      
            if aux is not None:                            #verifica se o objeto foi encontrado                        
                cls.objeto.remove(aux)                     #Remove o objeto da lista      
                cls.salvar()                               #Salva as alterações
        
        @classmethod
        def salvar(cls):                                                                       #Salva a lista de objetos Categoria em um arquivo JSON
            with open("categorias.json", "w") as arq:                                          #Abre o arquivo categorias.json em modo de escrita
                json.dump(cls,objetos, arq, default = Categoria.to_json, indent=4)             #Salva os objetos no arquivo usando a função json.dump

        @classmethod
        def abrir(cls):
            cls.objeto = []                                               #Inicializa a lista de objetos Categoria
            try:
                with open("categorias.json", "r") as arq:                 #Abre o arquivo categorias.json em modo de leitura
                    list_dic = json.load(arq)                             #Carrega os dados do arquivo usando a função json.load
                    for dic in list_dic:                                  #Percorre os dicionários carregados
                        c = Categoria.from_json(dic)                      #Cria um objeto Categoria a partir do dicionário
                        cls.objeto.append(c)                              #Adiciona o objeto à lista     
            except:
                pass                                                       #Ignora erros 
        