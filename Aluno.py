alunos = []

class Aluno:
    def __init__(self, nome, endereco, curso, email, matricula):
        self.nome = nome
        self.endereco = endereco
        self.curso = curso
        self.email = email
        self.matricula = matricula
        self.notas = []

    def __str__(self):
            return f"{self.nome} - {self.matricula} ({self.curso})"
    
    def cadastrar_aluno(self, nome, endereco, email, matricula):
        alunos.append()
        print(f"Aluno {self.nome} cadastrado com sucesso!")

    def remover_aluno(self, matrícula):
         alunos.pop()
         print(f"Aluno {self.nome} removido com sucesso!")