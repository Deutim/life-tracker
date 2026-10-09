""" Life Tracker

 Lista Inicial de Hábitos

Arrumar a cama
Oração AM
Higiene
Trabalho
Estudos
Leitura
Atividade Fisica
Alimentação Limpa
Água
Atualizar Finanças
Sem Vicios
Autocuidado
Oração PM

"""

habitos = [
    {"nome": "Arrumar a cama", "concluido": False},
    {"nome": "Oração AM", "concluido": False},
    {"nome": "Higiene", "concluido": False},
    {"nome": "Trabalho", "concluido": False},
    {"nome": "Estudos", "concluido": False},
    {"nome": "Leitura", "concluido": False},
    {"nome": "Atividade fisica", "concluido": False},
    {"nome": "Alimentação limpa", "concluido": False},
    {"nome": "Água", "concluido": False},
    {"nome": "Atualizar finanças", "concluido": False},
    {"nome": "Sem vicios", "concluido": False},
    {"nome": "Autocuidado", "concluido": False},
    {"nome": "Oração PM", "concluido": False}
]

def mostrar_habitos():
    print("\n===== Meus hábitos =====")

    for indice, habito in enumerate(habitos, start=1):
        if habito["concluido"]:
            status = "[X]"
        else:
            status = "[ ]"

        print(f"{indice}. {status} {habito['nome']}")

def alterar_habito():
    mostrar_habitos()

    entrada = input("\nDigite o número do hábito: ")

    if not entrada.isdigit():
        print("\nDigite um número válido")
        return

    numero = int(entrada)

    if numero < 1 or numero > len(habitos):
        print("\nHábito não encontrado.")
        return

    indice = numero - 1
    habito = habitos[indice]

    habito["concluido"] = not habito["concluido"]

    if habito["concluido"]:
        print(f"\nConcluido: {habito['nome']}")
    else:
        print(f"\nDesmarcado: {habito['nome']}")


def executar():
    while True:
        print("\n===== Life Tracker =====")
        print("1 - Visualizar hábitos")
        print("2 - Marcar/desmarcar hábito")
        print("0 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            mostrar_habitos()

        elif opcao == "2":
            alterar_habito()

        elif opcao =="0":
            print("Encerrando Life Tracker...")
            break

        else:
            print("Opção inválida.")

executar()
