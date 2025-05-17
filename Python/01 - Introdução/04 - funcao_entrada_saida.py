# Funções de entrada e saída em Python geralmente se referem ao uso das funções input() (entrada de dados) e print() (saída de dados). Veja um exemplo comentado:

#Explicação:

input() #pausa o programa e espera o usuário digitar algo. O texto digitado é retornado como string.
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print("Olá,", nome, "! Você tem", idade, "anos.")

print() # mostra informações na tela, útil para exibir resultados ou mensagens.
# Essas funções são essenciais para interagir com o usuário em programas simples.
print("Exemplo 1: Olá, mundo!")
print("Exemplo 2:", 10 + 5)
print("Exemplo 3: Meu nome é", nome)
print("Exemplo 4: Você tem", idade, "anos.")
print("Exemplo 5: Valor booleano:", True)
print("Exemplo 6: Lista de números:", [1, 2, 3, 4])


# Parâmetros 'end' e 'sep' na função print():

# 'sep' define o separador entre os argumentos passados para print().
print("A", "B", "C", sep="-")  # Saída: A-B-C

# 'end' define o que será impresso ao final da linha (por padrão é '\n', ou seja, nova linha).
print("Linha 1", end="... ")
print("continuação da linha 1")  # Saída: Linha 1... continuação da linha 1

# Exemplo combinando 'sep' e 'end':
print("Python", "é", "legal", sep="*", end="!\n")  # Saída: Python*é*legal!


# Variações do print() com exemplos:

# 1. Printando múltiplos valores de diferentes tipos:
print("Nome:", nome, "| Idade:", idade, "| Lista:", [1, 2, 3])

# 2. Usando diferentes separadores (sep):
print("banana", "maçã", "laranja", sep=", ")
print("2024", "06", "01", sep="/")

# 3. Mudando o final da linha (end):
print("Sem quebra de linha", end=" ")
print("continua na mesma linha.")

# 4. Printando com caracteres especiais:
print("Linha 1\nLinha 2\t<- tabulação")

# 5. Printando valores formatados:
print(f"Olá, {nome}! Você tem {idade} anos.")

# 6. Printando sem argumentos (linha em branco):
print()

# 7. Printando objetos compostos:
dicionario = {"a": 1, "b": 2}
print("Dicionário:", dicionario)

# 8. Printando com sep e end juntos:
print("A", "B", "C", sep="*", end=" FIM\n")