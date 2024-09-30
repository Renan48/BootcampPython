texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

for letra in texto:
     if letra.upper() in VOGAIS:
          print(letra, end="")
else: 
    print()
    print("executa no final do laço")

#utilizando um iteravel

for numero in range(0,11):
     print(numero, end=" ")
else:
     print()


#utilizando um a funçao built-in range
for numero in range(0, 51, 5):
     print(numero, end=" ")