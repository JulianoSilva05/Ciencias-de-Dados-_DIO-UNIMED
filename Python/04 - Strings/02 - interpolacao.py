print("- Metotodo old Style -".center(40,"#"))
nome = "Juliano"
print("Olá, %s!" % nome)

idade = 21
profissao = "Professor"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))

print("- Métotodo format -".center(40,"#"))
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))

print(" OU ".center(20,"-"))#Com indices
print("Olá, me chamo {3}. Eu tenho {0} anos de idade, trabalho como {1} e estou matriculado no curso de {2}." .format(idade,  profissao, linguagem, nome))

print(" OU ".center(20,"-"))#Com indices
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {curso}." .format(idade=idade,  profissao=profissao, curso=linguagem, nome=nome))

print("- Métotodo f-string -".center(40,"#"))
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}")