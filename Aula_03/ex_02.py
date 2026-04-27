class Aluno:
    def __init__(self):
        self.nome = ""
        self.matricula = ""
    def ano_ingresso(self):
        return int(self.matricula[0:4])
    def ano_conclusao(self):
        return self.ano_ingresso() + 3
        
x = Aluno()
x.nome = "Gilbert"
x.matricula = "20272014040001"
print(x.nome)             # para acessar o atributo: sem ()
print(x.matricula)
print(x.ano_ingresso())   # para chamar o método usa-se ()
print(x.ano_conclusao())  # Aluno.ano_conclusao(x)