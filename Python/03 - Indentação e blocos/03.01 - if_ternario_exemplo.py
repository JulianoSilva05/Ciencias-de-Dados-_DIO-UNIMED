saldo = 2000
saque = 2500

# status = "Sucesso" if saldo >= saque else "Falha"
status = {True: "Sucesso", False: "Falha"}[saldo >= saque]
print(f"{status} ao realizar o saque")