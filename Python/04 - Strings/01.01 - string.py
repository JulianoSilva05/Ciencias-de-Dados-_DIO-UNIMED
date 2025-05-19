nome = "JulIAno"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá Mundo!    "
print(texto +".")
print(texto.strip() +".")
print(texto.rstrip() +".")
print(texto.lstrip() +".")


menu = "Python"
print(menu.center(14,"#"))

print("P-y-t-h-o-n")

for i, letra in enumerate(menu):
    if i == len(menu) - 1:
        print(letra)
    else:
        print(letra, end="-")