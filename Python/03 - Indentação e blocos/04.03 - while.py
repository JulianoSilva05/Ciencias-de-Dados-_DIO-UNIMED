# O laço while em Python executa um bloco de código repetidamente enquanto uma condição for verdadeira. Ele é útil quando não sabemos antecipadamente quantas vezes o bloco deve ser executado.

# Sintaxe básica:
print("while condicao:\nprint('far alguma coisa')")
    # bloco de código
# Exemplo 1: Contando de 1 a 5
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
# Enquanto contador for menor ou igual a 5, imprime o valor e soma 1.
# Exemplo 2: Loop infinito (cuidado!)
while False:
    print("Isso nunca para! Use Ctrl+C para interromper.")
# O loop nunca termina porque a condição é sempre verdadeira.
# Dica: Sempre garanta que a condição do while possa se tornar falsa em algum momento, para evitar loops infinitos indesejados.

# Exemplo 3: Usando break para sair do loop
while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta == 'sair':
        break
# O loop só termina quando o usuário digita "sair".

#Exemplo 3
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair\n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrado...")
