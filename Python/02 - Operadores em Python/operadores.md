# Operadores em Python

Operadores são símbolos especiais usados para realizar operações em variáveis e valores. Veja os principais tipos:

## 1. Operadores Aritméticos

| Operador | Descrição      | Exemplo         | Resultado |
|----------|----------------|-----------------|-----------|
| `+`      | Adição         | `2 + 3`         | `5`       |
| `-`      | Subtração      | `5 - 2`         | `3`       |
| `*`      | Multiplicação  | `4 * 3`         | `12`      |
| `/`      | Divisão        | `10 / 2`        | `5.0`     |
| `//`     | Divisão inteira| `7 // 2`        | `3`       |
| `%`      | Módulo         | `7 % 2`         | `1`       |
| `**`     | Exponenciação  | `2 ** 3`        | `8`       |

## 2. Operadores de Comparação

| Operador | Descrição         | Exemplo      | Resultado |
|----------|-------------------|--------------|-----------|
| `==`     | Igual a           | `3 == 3`     | `True`    |
| `!=`     | Diferente de      | `3 != 4`     | `True`    |
| `>`      | Maior que         | `5 > 2`      | `True`    |
| `<`      | Menor que         | `2 < 5`      | `True`    |
| `>=`     | Maior ou igual    | `3 >= 3`     | `True`    |
| `<=`     | Menor ou igual    | `2 <= 3`     | `True`    |

## 3. Operadores Lógicos

| Operador | Descrição | Exemplo             | Resultado |
|----------|-----------|---------------------|-----------|
| `and`    | E         | `True and False`    | `False`   |
| `or`     | Ou        | `True or False`     | `True`    |
| `not`    | Não       | `not True`          | `False`   |

## 4. Operadores de Atribuição

| Operador | Exemplo   | Equivalente a |
|----------|-----------|---------------|
| `=`      | `x = 5`   | `x = 5`       |
| `+=`     | `x += 2`  | `x = x + 2`   |
| `-=`     | `x -= 1`  | `x = x - 1`   |
| `*=`     | `x *= 3`  | `x = x * 3`   |
| `/=`     | `x /= 2`  | `x = x / 2`   |

## 5. Operadores de Pertinência

```python
lista = [1, 2, 3]
print(2 in lista)    # True
print(4 not in lista) # True
```

## 6. Operadores de Identidade

```python
a = [1, 2]
b = a
print(a is b)      # True
print(a is not b)  # False
```

---

Esses são os principais operadores em Python. Use-os para manipular dados e controlar o fluxo dos seus programas!