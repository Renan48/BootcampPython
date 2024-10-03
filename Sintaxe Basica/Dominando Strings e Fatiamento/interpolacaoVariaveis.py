nome = "Renan Pereira"
idade = 31
profissao = "Progamador"
linguagem = "Python"

dados ={"nome": "Renan Pereira", 
        "idade": 31,
       "profissao": "Progamador",
       "linguagem": "Python"}

# print("nome: %s. idade: %d Profissão %s Curso: %s. " % (nome, idade, profissao, linguagem))
# print("nome: {}. idade: {} Profissão {} Curso: {}.".format(nome, idade, profissao, linguagem))
# print("nome: {3}. idade: {2} Profissão {1} Curso: {0}.".format(linguagem, profissao, idade, nome))
# print("nome: {nome}. idade: {idade} Profissão {profissao} Curso: {linguagem}.".format(linguagem = linguagem, profissao = profissao, idade = idade, nome = nome))
# print("nome: {nome}. idade: {idade} Profissão {profissao} Curso: {linguagem}.".format(**dados))
# print(f"nome: {nome}. idade: {idade} Profissão {profissao} Curso: {linguagem}.")

saldo = 35.35689

print(f"saldo = {saldo}")
print(f"saldo = {saldo:.2f}")
print(f"saldo = {saldo:5.1f}")