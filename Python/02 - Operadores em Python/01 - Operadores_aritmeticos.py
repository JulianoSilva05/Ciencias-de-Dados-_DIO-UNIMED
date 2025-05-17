#Conhecendo os operadores aritméticos
# Operadores aritméticos são símbolos usados para realizar operações matemáticas básicas entre valores numéricos. Em Python, eles funcionam tanto com números inteiros (int) quanto com números de ponto flutuante (float). Aqui estão os principais operadores aritméticos:

# Operador	Nome	Exemplo	Resultado
# +	Adição	2 + 3	5
# -	Subtração	5 - 2	3
# *	Multiplicação	4 * 3	12
# /	Divisão	10 / 2	5.0
# Divisão inteira	10 // 3	3
# %	Módulo (resto)	10 % 3	1
# **	Exponenciação	2 ** 3	8
# Exemplos em Python
# Dicas e 'gotchas'
# O operador / sempre retorna um número do tipo float, mesmo que a divisão seja exata.
# O operador  faz a divisão inteira, descartando qualquer parte decimal.
# O operador % é útil para saber se um número é divisível por outro (ex: x % 2 == 0 verifica se x é par).
# A ordem das operações segue as regras matemáticas (parênteses, potências, multiplicação/divisão, adição/subtração).
# Exemplos de operadores aritméticos em Python

# Adição (+)
a = 10
b = 5
resultado_adicao = a + b  # Soma os valores de a e b
print("Adição (10 + 5):", resultado_adicao)

# Subtração (-)
resultado_subtracao = a - b  # Subtrai b de a
print("Subtração (10 - 5):", resultado_subtracao)

# Multiplicação (*)
resultado_multiplicacao = a * b  # Multiplica a por b
print("Multiplicação (10 * 5):", resultado_multiplicacao)

# Divisão (/)
resultado_divisao = a / b  # Divide a por b (resultado float)
print("Divisão (10 / 5):", resultado_divisao)

# Divisão inteira (//)
resultado_divisao_inteira = a // b  # Divide a por b e retorna o valor inteiro
print("Divisão inteira (10 // 5):", resultado_divisao_inteira)

# Módulo (%)
resultado_modulo = a % b  # Retorna o resto da divisão de a por b
print("Módulo (10 % 5):", resultado_modulo)

# Exponenciação (**)
resultado_exponenciacao = a ** b  # Eleva a à potência de b
print("Exponenciação (10 ** 5):", resultado_exponenciacao)

# Ordem das operações
resultado_ordem = 2 + 3 * 4  # Multiplicação antes da adição
print("Ordem das operações (2 + 3 * 4):", resultado_ordem)

resultado_parenteses = (2 + 3) * 4  # Parênteses alteram a ordem
print("Ordem das operações com parênteses ((2 + 3) * 4):", resultado_parenteses)