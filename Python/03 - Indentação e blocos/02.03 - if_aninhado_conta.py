conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif( saque <= saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso") 
    else:
        print("Saldo insuficiente")
elif conta_especial:
    print("Conta especial selecionada")
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif( saque > saldo ):
        print("Saque realizado com uso do cheque especial")
else:
    print("Sistema não reconheceu o tipo de conta, entre em contato com o seu gerente!")
