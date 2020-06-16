from classes import Cliente, ContaPoupanca, ContaCorrente, Banco

banco1 = Banco(agencias=54654, contas=161, nome='Santander')
banco2 = Banco(agencias=1111, contas=188, nome='Itaú')

cliente1 = Cliente('Maria', 52)
cliente1.criar_conta(numero=161, agencia=54654, saldo=100, tipo='cc', limite=400)
cliente1.conta.sacar(100, cliente1, banco1)
cliente1.conta.depositar(1000)
cliente1.conta.extrato()

cliente2 = Cliente('Marcos', 18)
cliente2.criar_conta(numero=188, agencia=1111, saldo=500, tipo='cp')
cliente2.conta.sacar(100, cliente2, banco2)
