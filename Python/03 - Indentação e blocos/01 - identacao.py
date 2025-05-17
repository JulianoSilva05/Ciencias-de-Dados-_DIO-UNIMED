"""
Identação refere-se ao espaçamento colocado no início de cada linha de código, geralmente usando espaços ou tabulações. Em Python, a identação é fundamental para definir blocos de código, como o corpo de funções, loops e condicionais. Um bloco corretamente identado indica quais instruções pertencem a determinada estrutura de controle, garantindo a correta execução do programa e evitando erros de sintaxe.
"""
import time
numero = 10

if (numero > 5):
    print("O número é maior que 5.")
else:
    print("O número é 5 ou menor.")

print("############ CONTA BANCARIA ###########")

saldo = 0
nome = ""
numero_cc = ""
numero_ag = ""
cpf = ""

def cadastrar():
    nome = input("Digite seu nome: ")
    cpf = input("CPF: ")

def depositar(valor_deposito):
    global saldo
    saldo += valor_deposito
    print(f"VALOR DEPOSITADO: R${valor_deposito}\nNNOVO SALDO: R${saldo}")

def sacar(valor):
    global saldo
    if saldo >= valor:
        saldo -= valor
        print("CONTANDO AS NOTAS....")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print("retire as notas....")
        print(f"VALOR SACADO: R${valor}\nNOVO SALDO: R${saldo}")
    else:
        print("Saldo insuficiente")

cadastrar()

depositar(1000)
sacar(100)
depositar(200)

# saldo = 1000
# valor_saque = float(input("Quanto deseja sacar?:"))
# sacar(saldo, valor_saque)