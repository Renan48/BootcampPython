print(True and True and True)
print(True and False and True)
print(True and False and True)
print(True or True or True)
print(True or False or False)
print(False or False or False)


saldo = 1000
saque = 200
limite = 100
conta_especial = True


x = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(x)
y = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(y)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

resultado= conta_especial_com_saldo_suficiente or conta_normal_com_saldo_suficiente
print(resultado)