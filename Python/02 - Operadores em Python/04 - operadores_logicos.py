# Exemplo de uso do operador and
# Operadores lógicos em Python são usados para combinar expressões booleanas (True ou False). Os principais operadores lógicos são: and, or e not.

# 1. and (E lógico)
# Retorna True se ambas as expressões forem verdadeiras.
# Exemplo de uso do operador and
a = True
b = False
resultado = a and b  # resultado será False, pois b é False
print(resultado)     # Saída: False

# Outro exemplo
idade = 20
tem_carteira = True
pode_dirigir = idade >= 18 and tem_carteira
print(pode_dirigir)  # Saída: True

# 2. or (OU lógico)
# Retorna True se pelo menos uma das expressões for verdadeira.
# Exemplo de uso do operador or
a = False
b = True
resultado = a or b   # resultado será True, pois b é True
print(resultado)     # Saída: True

# Outro exemplo
tem_passaporte = False
tem_rg = True
pode_viajar = tem_passaporte or tem_rg
print(pode_viajar)   # Saída: True

# 3. not (NÃO lógico)
# Inverte o valor lógico da expressão.
# Exemplo de uso do operador not
a = True
resultado = not a    # resultado será False
print(resultado)     # Saída: False

# Outro exemplo
chovendo = False
vou_sair = not chovendo
print(vou_sair)      # Saída: True
# Resumo
# and: True se ambos forem True.
# or: True se pelo menos um for True.
# not: Inverte o valor lógico.
# Esses operadores são muito usados em estruturas condicionais (if, while, etc.) para tomar decisões baseadas em múltiplas condições.

print("EXERCÍCIOS")
# Exercício 1: Verifique se uma pessoa pode votar (idade >= 16 e tem título de eleitor)


# Exercício 2: Verifique se um aluno foi aprovado (nota >= 7 ou fez trabalho extra)


# Exercício 3: Verifique se um produto NÃO está disponível (estoque == 0)
