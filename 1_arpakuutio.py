import random

arpakuutio_luukumaara = int(input("Anna arpakuutioiden lukumäärän: "))
lista = []

for i in range(0, arpakuutio_luukumaara):
    dado = random.randint(1, 6)
    lista.append(dado)

print(sum(lista))
