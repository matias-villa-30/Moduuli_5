lista = []
while True:

    numeros = input("Kirjoita numerot, paina enter lopetamaan: ")
    if numeros != "":
        lista.append(numeros)
    elif numeros == "":
        sortd_lista = sorted(lista, key=int, reverse=True)
        print(sortd_lista[0:5])
        break




