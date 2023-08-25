import re
def es_palindromo(frase):
    frase = re.sub(r'[^\w]', '', frase).lower()
    return frase == frase[::-1]
frase = "Anita, lava la tina."
if es_palindromo(frase):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")
print(frase)
frase1 = re.sub(r'[^\w]', '', frase).lower()
# frase2 = re.sub(r'[^\w]', '', frase).lower()
inversa = frase1[::-1]
# print(frase2)
print(inversa)