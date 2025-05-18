
# Em Python, repetição (ou laço/loop) permite executar um bloco de código várias vezes. Existem dois principais tipos de laços:

# 1. for
# Usado para percorrer sequências (listas, strings, ranges, etc.).
# Exemplo: Imprimir números de 0 a 4
for i in range(5):
    print(i)

print("EXEMPLO PERCORRER TEXTO DIGITASO PELO USUARIO")
texto = input("Ditie um texto: ")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
print("\n")

# range(5) gera os números 0, 1, 2, 3, 4.
# i recebe cada valor da sequência a cada iteração.
# 2. while
# Repete enquanto uma condição for verdadeira.
# Exemplo: Imprimir números de 0 a 4
i = 0
while i < 5:
    print(i)
    i += 1
# O bloco dentro do while executa enquanto i < 5 for verdadeiro.
# Dicas importantes
# Use break para sair do laço antes do fim.
# Use continue para pular para a próxima iteração.
# Exemplo com break e continue
for i in range(10):
    if i == 5:
        break  # Sai do laço quando i for 5
    if i % 2 == 0:
        continue  # Pula números pares
    print(i)  # Imprime apenas números ímpares menores que 5