conta_noraml = False
conta_universitaria = False
conta_especia =  True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_noraml:
  if saldo >= saque:
    print("saque realizado com sucessao")
  elif saque <= (saldo + cheque_especial):
    print("Saque realizado com uso do cheque especial")
  else: 
    print("nao foi possivel realizar o saque! ")
elif conta_universitaria:
  if saldo >= saque:
     print("Saque realizado com sucesso")
  else: 
    print("Saldo insuficiente")
elif conta_especia:
  print("conta especial selecionada")
else: 
  print("Sistema nao reconheceu seu timpo de conta, Entre em contato com o gerente")