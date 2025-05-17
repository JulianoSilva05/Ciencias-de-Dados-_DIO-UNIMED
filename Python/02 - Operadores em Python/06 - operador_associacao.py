
# Operadores de associação em Python são usados para verificar se um valor está presente (ou não) em uma sequência, como listas, strings ou tuplas. Existem dois operadores principais:

# in: Retorna True se o valor estiver presente na sequência.
# not in: Retorna True se o valor não estiver presente na sequência.
# Exemplos
# Verificando se um elemento está em uma lista
frutas = ['maçã', 'banana', 'laranja']
print('maçã' in frutas)      # True
print('uva' not in frutas)   # True

# Verificando em uma string
texto = "Visual Studio Code"
print('Code' in texto)       # True
print('Python' not in texto) # True

# Dicas
# Esses operadores funcionam com qualquer objeto iterável (listas, tuplas, strings, dicionários, etc.).
# No caso de dicionários, in verifica as chaves, não os valores.
# Possível uso no seu arquivo

frutas = ['maçã', 'banana', 'laranja']

if 'maçã' in frutas:
    print('Tem maçã na lista!')

if 'uva' not in frutas:
    print('Não tem uva na lista.')

# Esses operadores são muito usados em verificações de presença e filtros em coleções.

#EXERCICIOS
print("LISTA DE EXECÍCIOS")
# Exercício 1: Verifique se 'banana' está na lista de frutas e imprima uma mensagem apropriada.



# Exercício 2: Crie uma lista de números e verifique se o número 10 não está presente nela.


# Exercício 3: Verifique se a palavra 'Python' está em uma string e imprima o resultado.
