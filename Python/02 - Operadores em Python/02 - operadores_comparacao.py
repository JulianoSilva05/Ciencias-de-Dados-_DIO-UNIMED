#Operadores de Comparação
# Comparando números
a = 10
b = 20

# Essas linhas usam operadores de comparação em Python para comparar os valores das variáveis a e b. Cada comparação retorna um valor booleano: True (verdadeiro) ou False (falso).

# Explicação dos operadores:
# == : verifica se dois valores são iguais.
# != : verifica se dois valores são diferentes.
# < : verifica se o valor à esquerda é menor que o da direita.
# > : verifica se o valor à esquerda é maior que o da direita.
# <= : verifica se o valor à esquerda é menor ou igual ao da direita.
# >= : verifica se o valor à esquerda é maior ou igual ao da direita.
# O que cada linha faz:

print("a = 10 \nb = 20")
print("a == b", a == b)
# Imprime True se a for igual a b, senão imprime False.
# Comentário indica que o resultado esperado é False.

print("a != b",a != b)
# Imprime True se a for diferente de b.
# Resultado esperado: True.

print("a < b", a < b)
# Imprime True se a for menor que b.
# Resultado esperado: True.

print("a > b",a > b)
# Imprime True se a for maior que b.
# Resultado esperado: False.

print("a <= 10", a <= 10)
# Imprime True se a for menor ou igual a 10.
# Resultado esperado: True.

print("b >= 15", b >= 15)
# Imprime True se b for maior ou igual a 15.
# Resultado esperado: True.

# Observações importantes
# Para que essas comparações funcionem, as variáveis a e b devem estar definidas antes desse trecho.
# Os comentários ao lado (# True ou # False) mostram o resultado esperado, assumindo valores típicos para a e b (por exemplo, a = 10, b = 15).
# O comando print() serve para exibir o resultado de cada comparação no console do VS Code.

# Comparando strings
nome1 = "Alice"
nome2 = "Bob"
print(nome1 == nome2)  # False
print(nome1 != nome2)  # True

# Comparando listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(lista1 == lista2)  # True (valores iguais)
print(lista1 is lista2)  # False (objetos diferentes na memória)

print("EXERCÍCIOS")
# Exercício 1: Verifique se o número 5 é maior que 3

# Exercício 2: Verifique se a string "Python" é igual a "python"

# Exercício 3: Verifique se a lista [1, 2] é diferente da lista [2, 1]
