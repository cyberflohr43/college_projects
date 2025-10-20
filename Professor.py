class Professor:
    def __init__(self, nome, data_admissao, materia, email):
        self.nome = nome
        self.data_admissao = data_admissao
        self.materia = materia
        self.email = email
    
    def cadastrar_professor():
        return f"{professor1.nome} cadastrado com sucesso!"

professor1 = Professor(
    nome = input("nome: ").upper(),
    data_admissao= int(input("data de admissao: ")),
    materia= input("materia lecionada: "),
    email= input("email: ")
)
