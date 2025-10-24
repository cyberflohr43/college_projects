from models.Aluno import Aluno
from models.Professor import Professor
from controllers.funcoes import cadastrar_professor, cadastrar_aluno, listar_alunos, enviar_tarefas, ver_tarefas, atribuir_notas

def main():

    while True:
        print("===SISTEMA ACADEMICO===")
        print("\n===1.0===\n")
        print("1. Fazer Login")
        print("2. Criar cadastro")
        print("3. Sair")
        selecao1 = input("\n\nselecione uma opcao: ")

        if selecao1 == "1":
            login = input("login: ")
            senha = input("senha: ")

            if login == "professor" and senha == "123":
                print("===SISTEMA ACADEMICO===")
                print("\n===beta 0.1===\n")
                print("selecione uma opcao: ")
                print("\n1. Enviar Tarefas")
                print("2. Atribuir Notas")
                print("3. Listar Alunos")
                print("4. Sair")

                selecao_professor = input("selecione uma opcao: ")
                
                if selecao_professor == "1":
                    enviar_tarefas()
                elif selecao_professor == "2":
                    atribuir_notas()
                elif selecao_professor == "3":
                    listar_alunos()
                elif selecao_professor == "4":
                    print("Até logo!")
                    break
                

            elif login == "aluno" and senha == "123":
                print("++==__AREA DO ALUNO__==++")
                print("\n1. Ver Notas")
                print("2. Ver atividades")
                print("3. ")
                selecao_aluno = input("Selecione uma opcao: ")

                if selecao_aluno == "1":
                    pass
                elif selecao_aluno == "2":
                    ver_tarefas()

        elif selecao1 == "2":
                print("--- Criar cadastro ---")
                print("1. Aluno")
                print("2. Professor")
                print("3. Sair")

                opcao = input("selecione: ")

                if opcao == "1":
                    cadastrar_aluno()

                elif opcao == "2":
                    cadastrar_professor()
                    
        elif selecao1 == "3":
            print("encerrando...")
            break
        
        else:
            print("opcao invalida...")

if __name__ == "__main__":
    main()