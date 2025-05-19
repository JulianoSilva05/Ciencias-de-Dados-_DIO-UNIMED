# String de multiplas linhas, ou String tripla
# String de múltiplas linhas são definidas informando 3 aspas simples ou dupla durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.
nome = "Juliano"

mensagem = f"""Olá, meu nome é {nome}, 
        Estou aprendendo Python
"""
print(mensagem)
print(f"""Bom dia!, meu nome é {nome}, 
        Estou aprendendo Python""")

print(
    """
    ================= MENU =================

    1 - Depositar
    2 - Sacar
    3 - Sair

    ========================================

                                    Bom dia!

"""
)