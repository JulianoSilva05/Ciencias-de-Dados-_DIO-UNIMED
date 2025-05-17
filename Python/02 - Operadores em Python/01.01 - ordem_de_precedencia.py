# Ordem de precedência dos operadores em Python

# Parênteses têm a maior precedência
resultado1 = (2 + 3) * 4  # Primeiro soma (2+3)=5, depois multiplica 5*4=20

# Exponenciação tem precedência maior que multiplicação
resultado3 = 2 * 3 ** 2   # Primeiro faz 3**2=9, depois multiplica 2*9=18

# Multiplicação e divisão vêm antes de adição e subtração
resultado2 = 2 + 3 * 4    # Primeiro multiplica 3*4=12, depois soma 2+12=14

# Operadores com mesma precedência são avaliados da esquerda para a direita (exceto **)
resultado4 = 10 - 2 + 3   # Primeiro 10-2=8, depois 8+3=11

# Exemplo com divisão e parênteses
resultado5 = 10 / (2 + 3) # Primeiro soma (2+3)=5, depois divide 10/5=2.0

print("resultado1:", resultado1)
print("resultado2:", resultado2)
print("resultado3:", resultado3)
print("resultado4:", resultado4)
print("resultado5:", resultado5)