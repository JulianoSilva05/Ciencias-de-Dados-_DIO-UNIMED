# O if ternário em Python é uma forma compacta de escrever uma estrutura condicional simples (if-else) em uma única linha. Ele é útil quando você quer atribuir um valor a uma variável dependendo de uma condição.

# Sintaxe

print("variavel = valor_se_verdadeiro if condicao else valor_se_falso")


# Exemplo
idade = 18
status = "maior de idade" if idade >= 18 else "menor de idade"
print(status)  # Saída: maior de idade

# Como funciona
# condicao: expressão que será avaliada como True ou False.
# Se a condição for verdadeira, o resultado será valor_se_verdadeiro.
# Se a condição for falsa, o resultado será valor_se_falso.
# Equivalente ao if-else tradicional
if idade >= 18:
    status = "maior de idade"
else:
    status = "menor de idade"
# Vantagens
# Código mais curto e legível para condições simples.
# Útil em atribuições e retornos de funções.
# Cuidados
# Evite usar o if ternário para condições complexas, pois pode dificultar a leitura.
# Não substitui estruturas if-elif-else com múltiplas condições.
# Exemplo prático
numero = 5
par_ou_impar = "par" if numero % 2 == 0 else "ímpar"
print(par_ou_impar)  # Saída: ímpar


