import random

# 3) Ejercicio Complejo: Generador de Contraseñas Seguras
# Descripción: Vamos a crear un generador de contraseñas seguras 
# utilizando los conceptos que hemos aprendido hasta ahora, incluyendo funciones
# módulos y control de flujo. La idea es que el programa genere una 
# contraseña aleatoria con una longitud específica y asegure que cumple
# con ciertos requisitos de seguridad.
# a) Requisitos de seguridad de la contraseña:
# b) La contraseña debe tener al menos 8 caracteres.
# c) Debe incluir al menos una letra mayúscula y una letra minúscula.
# d) Debe contener al menos un número.
# e) Debe contener al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.)

minus = 'abcdefjhijklmnñoprstuvwxyz'
mayus = minus.upper()
nume = '1234567890'
carac_esp = '!@#$%&/'
longitud = 8
totalcarac= minus+mayus+nume+carac_esp
pasword = random.sample(totalcarac,longitud)
contraseña = ''.join(pasword)
print(f"la contraseña creada es: {contraseña}")