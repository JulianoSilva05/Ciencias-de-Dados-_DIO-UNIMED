nome  = "Juliano"
idade = 21
profissao = "Professor"
linguagem = "Python"

dados = {"nome": nome, "idade": idade, "profissao":profissao, "linguagem": linguagem, "saldo": 10000.45645}

print("NOME: %s IDADE: %d" %(nome,idade))
print("NOME: {} IDADE: {}" .format(nome,idade))
print("NOME: {0} IDADE: {1}" .format(nome,idade))
print("NOME: {0} IDADE: {1} NOME: {0}" .format(nome,idade))
print("NOME: {n} IDADE: {i}" .format(n=nome,i=idade))
print("NOME: {nome} IDADE: {idade} PROFISSÃO: {profissao} SALDO: {saldo:.2f}" .format(**dados))