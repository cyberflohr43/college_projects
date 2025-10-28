from models.Aluno import Aluno
from models.Professor import Professor
from models.Admin import Admin
import random
import json


#----------------objeto aluno----------------------#
alunos = [] 
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    matricula = gerar_matricula()
    curso = input("Curso: ")
    endereco = input("Endereco do aluno: ")
    email = input("Email do aluno: ")

    aluno = Aluno(nome, endereco, curso, email, matricula)
    alunos.append(aluno)
    print(f"\nAluno {nome} cadastrado com sucesso!")

def remover_aluno():
    remNome = input("Insira o nome do aluno a ser removido: ")
    remMatricula  = int(input("Insira a matrícula do aluno para ser removido: "))
    alunos.pop(remMatricula, remNome)
    print(f"Aluno {remNome} removido com sucesso!")

def gerar_matricula():
    print(random.randint(2025000,2025999))

def listar_alunos():
    if not alunos:
        print("\nNenhum usuario cadastrado...\n")
    else:
        for aluno in alunos:
            print(aluno)

#----------------------objeto professor----------------------#
professores = []
tarefas = []
notas = []

def cadastrar_professor():
    nome = input("Nome do professor: ")
    data_admissao = input("Data de admissao do professor: ")
    email = input("Email do professor: ")
    materia = input("Materia que o professor leciona: ")
    professor = Professor(nome, data_admissao, email, materia)
    professores.append(professor)
    print(f"Professor {nome} cadastrado com sucesso!")

def listar_professores():
    if not professores:
        print("\nNenhum usuario cadastrado...\n")
    else:
        for professor in professores:
            print(professor)

def enviar_tarefas():
    tarefaTitulo = input("Digite o titulo da tarefa: ")
    dataEntrega = input("Digite a data de entrega: ")
    tarefas.append(tarefaTitulo)
    tarefas.append(dataEntrega)
    for tarefa in tarefas:
        print(tarefa)

def ver_tarefas():
    for tarefa in tarefas:
        print(tarefa)

def atribuir_notas():
    while True:
        nota_aluno = input("Nome do Aluno: ")
        nota_materia = input("Materia: ")
        nota_nota = float(input("Nota: "))
        notas.append(nota_aluno,nota_materia,nota_nota)
        nota_nova = input("deseja atribuir uma nova nota?[s/n]: ")
        if nota_nova == "n" or "N":
            break
        else:
            continue

def mostrar_notas():
    for nota in notas:
        print(nota)

#--------------------objeto ADMIN---------------------#
adm = []
chave_admin = 666777

def cadastrar_admin():
    permissao = int(input("Insira a chave: "))
    if permissao == chave_admin:
        print("/_Criar cadastro de novo ADMIN_/")
        adm_nome = input("Digite o nome do Administrador: ")
        adm_senha = input("Insira a senha do Adminstrador: ")
        adm_email = input("E-Mail: ")
        adm_ID = (random.randint(111111,999999))
        salvar_credenciais(adm_nome, adm_senha)
        adm.append(adm_ID)
        adm.append(adm_email)
        print("Um novo ADM nasce.")
    else:
        print("Chave inválida!")

#---------------sistema de login---------------------------#

def salvar_credenciais(usuario, senha):
    credenciais = {"usuario": usuario, "senha": senha}
    with open("credenciais.json", "w") as arquivo:
        json.dump(credenciais, arquivo)

def carregar_credenciais():
    try:
        with open("credenciais.json", "r") as arquivo:
            credenciais = json.load(arquivo)
            return credenciais.get("usuario"), credenciais.get("senha")
    except (FileNotFoundError, json.JSONDecodeError):
        return None, None