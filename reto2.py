def palindroma(palabra):
    palabra = palabra.replace(" ", "").lower()
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - i - 1]:
            return False
    return True

palabra = input("Ingresa una palabra: ")
if palindroma(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
