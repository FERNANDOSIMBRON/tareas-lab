def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese un número: "))
print(f"Los números primos menores que {n} son:")

for num in range(2, n):
    if es_primo(num):
        print(num, )
        

