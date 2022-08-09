# PROGRAMA QUE GERA NOME DOS USUARIOS DO SISTEMA

fullNameUser = str(input('Digite o nome completo titular: ')).strip()
nome = fullNameUser.split()
print(nome)
print("{}".format(nome[0]) + "." + "{}".format(nome[-1]))
print("{}".format(nome[0].title()))
