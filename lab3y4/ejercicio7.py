def contar_palabras_caracteres(frase):
    # Contar palabras
    palabras = frase.split()
    num_palabras = len(palabras)

    # Contar caracteres
    num_caracteres = len(frase)

    return num_palabras, num_caracteres

frase = "Estoy aprendiendo Python y me está gustando mucho. ¡Es genial!"
num_palabras, num_caracteres = contar_palabras_caracteres(frase)

print("Número de palabras:", num_palabras)
print("Número de caracteres:", num_caracteres)