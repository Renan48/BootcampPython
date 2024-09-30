MAIOR_IDADE = 18 

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
   print("maior de idade, pode tirar a cnh. ")

if idade < MAIOR_IDADE:
   print("Ainda nao pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("maior de idade, pode tirar a cnh. ")
elif idade == IDADE_ESPECIAL:
   print("Pode Fazer aulas teoricas, mas nao pode fazer aulas praticas")
else:
   print("ainda nao pode tirar a cnh")

