import pytest
import os
from random import randrange


os.system("cls" if os.name == "nt" else "clear")


def valida_cpf(cpf):
    def calcula_dv1(cpf):
        soma = 0
        i = 10
        while i >= 2:
            for digito in cpf[:9]:
                soma += digito * i
                i -= 1
        resto1 = (soma * 10) % 11
        if resto1 == 10:
            resto1 = 0
        return resto1

    def calcula_dv2(cpf):
        soma = 0
        i = 11
        while i >= 2:
            for digito in cpf[:10]:
                soma += digito * i
                i -= 1
        resto2 = (soma * 10) % 11
        if resto2 == 10:
            resto2 = 0
        return resto2

    def adiciona_mascara_cpf(cpf):
        cpf_sem_mascara = [str(digito) for digito in cpf]
        cpf_com_mascara = cpf_sem_mascara[:]
        cpf_com_mascara.insert(3, ".")
        cpf_com_mascara.insert(7, ".")
        cpf_com_mascara.insert(11, "-")
        return "".join(cpf_com_mascara), "".join(cpf_sem_mascara)

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

    return cpf_valido, calcula_dv1(cpf), calcula_dv2(cpf), adiciona_mascara_cpf(cpf)


def gera_cpf_valido():
    numeros = "".join([f"{randrange(0, 10)}" for i in range(9)])

    dv1 = valida_cpf(numeros)[1]
    numeros = numeros + f"{dv1}"

    dv2 = valida_cpf(numeros)[2]
    numeros = numeros + f"{dv2}"

    cpf_com_mascara = valida_cpf(numeros)[3][0]
    cpf_sem_mascara = valida_cpf(numeros)[3][1]

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
        cpf_valido = valida_cpf(cpf)[0]
        cpf_com_mascara = valida_cpf(cpf)[3][0]
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
    assert valida_cpf("75405260681")[0]
    assert valida_cpf("77136427495")[0]
    assert valida_cpf("68322145454")[0]
    assert valida_cpf("01334623589")[0]
    assert valida_cpf("54144353320")[0]

    assert not valida_cpf("00000000000")[0]
    assert not valida_cpf("33333333333")[0]
    assert not valida_cpf("99999999999")[0]
    assert not valida_cpf("23891375711")[0]
    assert not valida_cpf("11434221074")[0]

    main()
