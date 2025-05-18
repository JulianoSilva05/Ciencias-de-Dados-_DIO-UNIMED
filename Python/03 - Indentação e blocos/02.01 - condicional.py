#Programa que verifica se usuario pode "tirar" a CNH
MAIOR_DE_IDADE = 18

idade = int(input("Qual a sua idade: \n"))

if idade >= MAIOR_DE_IDADE:
    print("Pode tirar a habilitação")
else:
    print("Ainda não pode tirar a habilitação")
    print(f"Espere mais {MAIOR_DE_IDADE - idade} ano(s)")