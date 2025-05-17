# Conversão de Tipos em Python

# Inteiro para float
num_int = 10
num_float = float(num_int)
print(f'Inteiro para float: {num_int} -> {num_float} ({type(num_float)})')

# Float para inteiro
num_float2 = 9.7
num_int2 = int(num_float2)
print(f'Float para inteiro: {num_float2} -> {num_int2} ({type(num_int2)})')

# Inteiro para string
num_str = str(num_int)
print(f'Inteiro para string: {num_int} -> "{num_str}" ({type(num_str)})')

# String para inteiro
str_num = "15"
int_num = int(str_num)
print(f'String para inteiro: "{str_num}" -> {int_num} ({type(int_num)})')

# String para float
str_float = "3.14"
float_num = float(str_float)
print(f'String para float: "{str_float}" -> {float_num} ({type(float_num)})')

# Float para string
float_str = str(num_float2)
print(f'Float para string: {num_float2} -> "{float_str}" ({type(float_str)})')

# Observação: conversão de string para inteiro/float só funciona se a string for um número válido.
# Exemplo de erro:
try:
    erro = int("abc")
except ValueError as e:
    print(f'Erro ao converter "abc" para inteiro: {e}')