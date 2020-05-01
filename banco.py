# Linguagem de Programação II
# AC03 ADS-EaD - Banco
#
# Email: willian.vieira@aluno.faculdadeimpacta.com.br

from typing import Union, List, Dict

Number = Union[int, float]

class Cliente():

    def __init__(self, nome: str, telefone: int, email: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

        if "@" not in self.__email:
            raise ValueError("O email não é válido ele precisa conter um @")

        if type(self.__telefone) is not int:
            raise TypeError("O telefone precisa ser um número inteiro!")   

    def get_nome(self) -> str:
        return self.__nome

    def get_telefone(self) -> int:
        return self.__telefone

    def set_telefone(self, novo_telefone: int) -> None:
        if type(novo_telefone) is not int:
            raise TypeError("O telefone precisa ser um número inteiro!")
        self.__telefone = novo_telefone

    def get_email(self) -> str:
        return self.__email

    def set_email(self, novo_email: str) -> None:
        if "@" not in novo_email:
            raise ValueError("O email não é válido ele precisa conter um @")
        self.__email = novo_email

class Banco():
    def __init__(self, nome: str):
        self.__nome = nome
        self.__contas = []

    def get_nome(self) -> str:
        return self.__nome

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:

        num_conta = len(self.__contas) + 1 
        self.__contas.append(Conta(clientes, num_conta, saldo_ini))

        if saldo_ini < 0:
            raise ValueError("Valor presente na conta é menor que R$ 00,00") 

    def lista_contas(self) -> List['Conta']:
        return self.__contas

class Conta():

    def __init__(self, clientes: List[Cliente],numero_conta: int, saldo_inicial: Number):
        self.__clientes = clientes
        self.__numero_conta = numero_conta
        self.__saldo_inicial = saldo_inicial
        self.__extrato = []

        if self.__saldo_inicial < 0:
            raise ValueError("Saldo menor que zero")
        
        self.__extrato.append(('saldo_inicial', saldo_inicial))
                 
    def get_clientes(self) -> List[Cliente]:
        return self.__clientes

    def get_saldo(self) -> Number:
        return self.__saldo_inicial

    def get_numero(self) -> int:
        return self.__numero_conta

    def saque(self, valor: Number) -> None:

        if valor > self.__saldo_inicial:
            raise ValueError("Saque não autorizado, valor é maior que o saldo em conta!")

        self.__saldo_inicial -=valor
        self.__extrato.append(("saque", valor))

    def deposito(self, valor: Number):
        self.__saldo_inicial += valor
        self.__extrato.append(("deposito", valor))

    def extrato(self) -> List[Dict[str, Number]]:
        return self.__extrato