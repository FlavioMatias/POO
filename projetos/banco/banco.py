from random import *


class Banco_jujubas():

contas = []

    class usuario():
        def __init__(self, titular):
            self.titular = titular
            self.conta = self.gerar_conta()
            self.saldo = 0
            self.creditos = 0
            self.fatura = 0

        def Gerar_conta():
            while True:
                n = randint(10000,99999)
                if n not in Banco.contas: 
                    Banco.contas.append(n)
                    return n

        def Deposito(self, deposito):
            self.saldo += deposito

        
        def Saque(self, valor):
            if self.saldo >= valor and valor > 0:
                self.saldo -= valor
                return valor
                
        def Pix(self, recebedor, valor):
            if self.saldo >= valor:
                self.saldo -= valor
                recebedor.saldo += valor

            

    

