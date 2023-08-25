def invertir_palabras_en_frase(frase):
    palabras = frase.split()

    palabras_invertidas = palabras[::-1]

    # Paso 3: Unir las palabras para formar la nueva frase invertida
    frase_invertida = " ".join(palabras_invertidas)

    return frase_invertida

frase_original = "Aprendiendo Python con Edem"
frase_invertida = invertir_palabras_en_frase(frase_original)
print("Frase original:", frase_original)
print("Frase invertida:", frase_invertida)