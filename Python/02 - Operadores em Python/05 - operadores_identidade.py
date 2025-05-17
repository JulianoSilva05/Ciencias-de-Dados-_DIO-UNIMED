# Operadores de identidade em Python são  
# 05 - operadores_identidade.py

# Operadores de identidade em Python são usados para comparar se duas variáveis referenciam exatamente o mesmo objeto na memória. Eles são diferentes dos operadores de igualdade (==), que verificam se os valores dos objetos são iguais.

# Principais operadores de identidade
# is: Retorna True se as variáveis comparadas apontam para o mesmo objeto.
# is not: Retorna True se as variáveis comparadas apontam para objetos diferentes.
# Exemplo prático

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True, pois b é o mesmo objeto que a
print(a is c) # False, pois c é um objeto diferente, mesmo com o mesmo conteúdo
print(a == c) # True, pois os conteúdos são iguais

print(a is not c) # True, pois a e c não são o mesmo objeto

# Exemplos adicionais
x = None
y = None
print(x is y) # True, pois ambos apontam para o mesmo objeto None

d = 256
e = 256
print(d is e) # True, pois inteiros pequenos são otimizados pelo Python

f = 257
g = 257
print(f is g) # Pode ser False, pois inteiros maiores podem não compartilhar referência

s1 = "python"
s2 = "python"
print(s1 is s2) # True, strings curtas podem ser otimizadas

s3 = "".join(["py", "thon"])
print(s1 is s3) # Pode ser False, pois s3 foi criado dinamicamente

# Comparando com None (boa prática)
var = None
if var is None:
    print("var é None")

# Pontos importantes
# Objetos imutáveis pequenos (como inteiros de -5 a 256 e strings curtas) podem ser otimizados pelo Python para compartilhar a mesma referência, mas não conte sempre com isso.
# Use is para comparar com None (ex: if x is None:), pois é garantido que só existe um objeto None em Python.
# Resumindo
# is e is not verificam identidade de objeto (mesmo local na memória).
# == verifica igualdade de valor (mesmo conteúdo).

print("EXERCÍCIOS")
# "1. Crie duas listas diferentes com o mesmo conteúdo e verifique se elas são o mesmo objeto usando 'is' e se possuem o mesmo conteúdo usando '=='."

# "2. Crie duas variáveis inteiras com o valor 1000 e verifique se elas são o mesmo objeto usando 'is'. Explique o resultado.",

# "3. Crie uma variável com valor None e outra com valor 0. Use 'is' para comparar ambas com None e explique a diferença dos resultados."
