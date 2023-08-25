def cifrado_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            codigo_ascii = ord(letra)
            if letra.isupper():
                nueva_letra = chr((codigo_ascii - 65 + desplazamiento) % 26 + 65)
            else:
                nueva_letra = chr((codigo_ascii - 97 + desplazamiento) % 26 + 97)
            mensaje_cifrado += nueva_letra
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

mensaje_original = "Hola Mundo!"
desplazamiento = 1
mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)
