# Condicionais em Python permitem que você execute diferentes blocos de código dependendo de condições lógicas. O principal comando para isso é o if, junto com elif (else if) e else.

# Estrutura básica
'''
if condição:
    # código executado se a condição for verdadeira
elif outra_condição:
    # código executado se a primeira for falsa e esta for verdadeira
else:
    # código executado se todas as condições anteriores forem falsas
    # '''

# Exemplo prático
print("IF")
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
if idade < 18:
    print("Você é menor de idade.")

print("Outro exemplo")
print("IF / ELSE")
#Se a condição IF (SE) não for verdadeira, ela pode ter um ELSE (SENÃO)
saldo = 200000
saque = float(input("Informe o valor do saque: \nR$"))
if (saldo >= saque):
    print("Realizando saque")
else:
    print("Saldo insuficiente!")
# Pontos importantes:
# A condição deve ser uma expressão que retorna True ou False.
# Os blocos de código são definidos pela indentação (espaços à esquerda).
# Você pode ter quantos elif quiser, mas apenas um if e um else.
# Dica
# Cuidado com a indentação! Em Python, ela é obrigatória para definir blocos de código.
print("IF / ELIF / ELSE")
# O elif em Python significa "else if" (senão se). Ele é usado em estruturas condicionais para testar múltiplas condições de forma sequencial, após um if inicial.
# Exemplo:
valor = 10

if valor > 20:
    print("Maior que 20")
elif valor > 5:
    print("Maior que 5 e menor ou igual a 20")
else:
    print("Menor ou igual a 5")
# Como funciona:
# O Python avalia a condição do if primeiro.
# Se for falsa, ele verifica a condição do elif.
# Se nenhuma for verdadeira, executa o bloco do else (opcional).
# Resumo:
# Use elif para testar várias condições diferentes, evitando múltiplos if independentes. Isso torna o código mais claro e eficiente.

print("OUTRO EXEMPLO:")
opcao = int(input("INFORME UMA OPÇÃO: \n[1] - Sacar \n[2] - Extrato \n[3] - Depositar \n"))
if opcao == 1:
    print("Qual o valor deseja sacar:\nR$ ")
    ...
elif opcao == 2:
    print("Exibindo extrato: ")
    ...
elif opcao == 3:
    print("Qual o valor do deposito: \nR$ ")
else:
    print("Digite um valor valido!")
