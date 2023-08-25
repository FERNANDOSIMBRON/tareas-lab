import random
import string

def generate_random_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    character_pool = ''

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("Debe seleccionar al menos un tipo de caracter para generar la contraseña.")

    try:
        password = ''.join(random.choice(character_pool) for _ in range(length))
        return password

    except Exception as e:
        raise Exception("Error al generar la contraseña: " + str(e))

def main():
    try:
        length = int(input("Ingrese la longitud de la contraseña: "))
        use_uppercase = input("Incluir letras mayúsculas (S/N): ").upper() == "S"
        use_lowercase = input("Incluir letras minúsculas (S/N): ").upper() == "S"
        use_numbers = input("Incluir números (S/N): ").upper() == "S"
        use_special_chars = input("Incluir caracteres especiales (S/N): ").upper() == "S"

        password = generate_random_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
        print("Contraseña generada:", password)

    except ValueError:
        print("Error: Ingrese una longitud válida para la contraseña.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
    main()


