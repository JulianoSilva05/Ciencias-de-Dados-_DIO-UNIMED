# If aninhado (nested if) ocorre quando você coloca uma estrutura if dentro de outra. Isso permite testar condições mais complexas, onde uma decisão depende de outra.

# Exemplo
# Verifica se um número é positivo e, se for, se é par
numero = 8

if numero > 0:
    print("O número é positivo.")
    if numero % 2 == 0:
        print("E também é par.")
    else:
        print("Mas é ímpar.")
else:
    print("O número não é positivo.")

# Quando usar
# Quando uma condição só faz sentido ser avaliada se outra já foi satisfeita.
# Para criar decisões em múltiplos níveis (ex: autenticação, permissões, validações em etapas).
# Dicas
# Evite muitos níveis de aninhamento, pois o código pode ficar difícil de ler.
# Considere usar elif ou funções para simplificar lógicas muito complexas.

#Exemplo 2
#Conta normal pode sacar mesmo sem saldo com uso do cheque especial
#Conta universitaria só realiza saque se tiver saldo
saldo = 2000
conta = int(input("Digite 1 para conta normal e 2 para universitaria"))
if conta == 1:
    saque = float(input("VALOR PARA SAQUE: "))
    if saldo >= saque:
        saldo -= saque
        print(f"Saque realizado com sucesso. Seu saldo atual é R$ {saldo}")
    elif saldo < saque:
        saldo -= saque
        print(f"Saque realizado usando limite do cheque especial. Seu saldo atual é R$ {saldo}")
elif conta == 2:
    saque = float(input("VALOR PARA SAQUE: "))
    if saldo >= saque:
        saldo -= saque
        print(f"Saque realizado com sucesso. Seu saldo atual é R$ {saldo}")
    elif saldo < saque:
        print(f"SALDO INSUFICIENTE")