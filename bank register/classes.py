from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Conta(ABC):
    def __init__(self, numero, agencia, saldo):
        self._numero = numero
        self._agencia = agencia
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Depósito inválido. Favor inserir um número. ')
        self._saldo += valor
        print(f'Depósito de R${valor} realizado.')

    def extrato(self):
        print(f' Agência:{self._agencia}\n', f'Conta: {self._numero}\n', f'Saldo: {self._saldo}')


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, saldo, limite=0):
        Conta.__init__(self, numero, agencia, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor, cliente, banco):
        if not banco.verifica_cliente(cliente):
            print('Conta não existente.')
            return
        if valor > (self._saldo + self._limite):
            print('Saldo insuficiente.')
            return
        print(f'Saque de R${valor} concluído.')
        self._saldo -= valor


class ContaPoupanca(Conta):

    def sacar(self, valor, cliente, banco):
        if not banco.verifica_cliente(cliente):
            print('Conta não existente.')
            return
        if valor > self._saldo:
            print('Saldo insuficiente.')
            return
        print(f'Saque de R${valor} concluído.')
        self._saldo -= valor


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.conta = None

    def criar_conta(self, numero, agencia, saldo, tipo, limite=0):
        if tipo == 'cc':
            self.conta = ContaCorrente(numero, agencia, saldo, limite)
        elif tipo == 'cp':
            self.conta = ContaPoupanca(numero, agencia, saldo)
        else:
            print(
                'Código de tipo de conta incorreto. Favor inserir "cc" para conta corrente ou "cp" para conta poupança.')
            return


class Banco:
    def __init__(self, agencias, contas, nome):
        self._agencias = agencias
        self._contas = contas
        self.nome = nome
        if self.procura_arquivo():
            self.escreve_arquivo()

    def escreve_arquivo(self):
        nome_arquivo = self.nome + '.txt'
        with open(nome_arquivo, 'a+') as file:
            file.write(f'{self._agencias}')
            file.write(f'{self._contas}\n')

    def procura_arquivo(self):
        nome_arquivo = self.nome + '.txt'
        registro = str(self._agencias) + str(self._contas) + '\n'
        with open(nome_arquivo, 'r') as file:
            for i, value in enumerate(file):
                if value == registro:
                    return False
            return True

    def verifica_cliente(self, cliente):
        nome_arquivo = self.nome + '.txt'
        registro = str(cliente.conta._agencia) + str(cliente.conta._numero) + '\n'
        with open(nome_arquivo, 'r') as file:
            for i, value in enumerate(file):
                if value == registro:
                    return True
            return False
