# sistema_bancario_oo.py

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class ContaBancaria:
    LIMITE_SAQUE = 500
    LIMITE_DIARIO = 3

    def __init__(self, numero, agencia, cliente):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []
        self.saques_realizados = 0

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            re
