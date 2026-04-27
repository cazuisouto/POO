class Cliente:
    def __init__(self, nome, cpf): 
        self.nome = nome 
        self.cpf = cpf
        self.socio = None
    
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    
    def set_cpf(self, cpf):
        self.cpf = cpf
    def get_cpf(self): 
        return self.cpf
    
    def set_socio(self, c):
        if self.socio != None:  #Verifica se o cliente já tem um sócio
           self.socio.socio = None  #Se tiver, o sócio do cliente tem seu sócio setado para None, ou seja, o cliente deixa de ser sócio do outro cliente
        
        if c.socio != None:  #Verifica se o cliente que será sócio já tem um sócio
            c.socio.socio = None  #Se tiver, o sócio do cliente que será sócio tem seu sócio setado para None, ou seja, o cliente deixa de ser sócio do outro cliente
     
        self.socio = c     #Aqui, o cliente recebe o outro cliente como sócio, e o sócio recebe o cliente como sócio também
        c.socio = self 
    
    def get_socio(self):
        if self.socio != None:  #Verifica se o cliente tem um sócio
            return self.socio.nome  #Se tiver, retorna o nome do sócio
        else:
            return None  #Se não tiver, retorna None
        
    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Sócio: {self.get_socio()}"
    
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    
    def inserir_cliente(self, cliente):
        self.clientes.append(cliente) 

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)
    
    def __str__(self):
        return f"Empresa: {self.nome}, Quantidade de clientes: {len(self.clientes)}"

      

