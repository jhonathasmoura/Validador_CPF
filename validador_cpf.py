import os
from random import randrange


os.system("cls" if os.name == "nt" else "clear")


def calcula_dv1(cpf):
    soma = 0
    i = 10
    while i >= 2:
        for digito in cpf[:9]:
            soma += int(digito) * i
            i -= 1
    dv1 = (soma * 10) % 11
    return 0 if dv1 == 10 else dv1


def calcula_dv2(cpf):
    soma = 0
    i = 11
    while i >= 2:
        for digito in cpf[:10]:
            soma += int(digito) * i
            i -= 1
    dv2 = (soma * 10) % 11
    return 0 if dv2 == 10 else dv2


def valida_cpf(cpf):
    cpf = [int(digito) for digito in cpf]
    if len(set(cpf)) == 1:
        cpf_valido = False
    else:
        dv1 = calcula_dv1(cpf)
        dv2 = calcula_dv2(cpf)
        if dv1 == cpf[-2] and dv2 == cpf[-1]:
            cpf_valido = True
        else:
            cpf_valido = False
    return cpf_valido


def adiciona_mascara_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def gera_cpf_valido():
    numeros = "".join([f"{randrange(0, 10)}" for i in range(9)])
    while len(set(numeros)) == 1:
        numeros = "".join([f"{randrange(0, 10)}" for i in range(9)])
    dv1 = calcula_dv1(numeros)
    numeros = numeros + f"{dv1}"
    dv2 = calcula_dv2(numeros)
    numeros = numeros + f"{dv2}"
    cpf_com_mascara = adiciona_mascara_cpf(numeros)
    cpf_sem_mascara = numeros
    return cpf_com_mascara, cpf_sem_mascara


def gera_lista_cpfs(qtd_cpfs):
    return [gera_cpf_valido() for i in range(qtd_cpfs)]


def main():
    opcao = int(
        input(
            "Escolha uma das opções: \n[1] Validar CPF\n[2] Gerar CPF válido\n[0] SAIR\n> "
        )
    )
    while opcao not in (0, 1, 2):
        opcao = int(input("Opção inválida! Tente novamente.\n> "))
    if opcao == 1:
        cpf = input("Digite o CPF para validação (apenas números): ")
        while len(cpf) != 11:
            cpf = input(
                "CPF incorreto!\nDigite o CPF para validação (apenas números): "
            )
        cpf_valido = valida_cpf(cpf)
        cpf_com_mascara = adiciona_mascara_cpf(cpf)
        print(f"\nCPF: {cpf_com_mascara}")
        print(
            f"Situação: \033[32mCPF válido!\033[m"
            if cpf_valido == True
            else "Situação: \033[31mCPF inválido!\033[m"
        )
    elif opcao == 2:
        qtd_cpfs = int(input("Deseja gerar quantos CPFs?: "))
        while qtd_cpfs <= 0:
            qtd_cpfs = int(input("Tente novamente!\nDeseja gerar quantos CPFs?: "))
        lista_cpfs = gera_lista_cpfs(qtd_cpfs)
        print("\nCPFs gerados:")
        for cpf_com_mascara, cpf_sem_mascara in lista_cpfs:
            print(f"\033[32m{cpf_com_mascara}\033[m | \033[32m{cpf_sem_mascara}\033[m")
    else:
        exit()


if __name__ == "__main__":
    main()
    while True:
        continuar = input("\nDeseja continuar? (S/N) ")
        if continuar not in ("S", "s", ""):
            break
        main()
