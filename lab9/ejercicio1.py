def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    try:
        temperatura = float(input("Ingrese la temperatura: "))
        unidad = input("Ingrese la unidad de temperatura (C o F): ").upper()

        if unidad == "C":
            fahrenheit = celsius_to_fahrenheit(temperatura)
            print(f"{temperatura} grados Celsius equivale a {fahrenheit:.2f} grados Fahrenheit.")
        elif unidad == "F":
            celsius = fahrenheit_to_celsius(temperatura)
            print(f"{temperatura} grados Fahrenheit equivale a {celsius:.2f} grados Celsius.")
        else:
            print("Unidad de temperatura no reconocida. Por favor, ingrese 'C' o 'F'.")

    except ValueError:
        print("Error: Ingrese una temperatura válida.")

if __name__ == "__main__":
    main()
