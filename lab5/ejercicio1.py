# punto 1
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edades_ordenadas = sorted(edades)
edad_minima = edades_ordenadas[0]
edad_maxima = edades_ordenadas[-1]

print("Las edades orenandas es:",edades_ordenadas)
print("La edad minima es:", edad_minima)
print("La edad maxima es:",edad_maxima)
print(" ")
#punto 2
edades.extend([edad_minima, edad_maxima])
print("La nueva lista con edades añadidas es:",edades)
print(" ")
#punto 3
edades_ordenadas = sorted(edades)
n = len(edades_ordenadas)

if n % 2 == 0:
    mediana = (edades_ordenadas[n // 2 - 1 ] + edades_ordenadas[n // 2]) / 2
else: 
    mediana = edades_ordenadas[n // 2]
    print("La edad mediana es:", mediana)
print(" ")
#punto 4
promedio = sum(edades) / len(edades)
print("El promedio de edades es:", promedio)
print("")
#punto 5
rango_edades = edad_maxima - edad_minima
print("El rango de edades es:",rango_edades)
print(" ")
#punto 6 
diferencia_minimo = abs(edad_minima - promedio)
diferencia_maximo = abs(edad_maxima - promedio)
print("Diferencia entre minimo y promedio es: ",diferencia_minimo)
print("Diferencia entre maximo y promedio es:", diferencia_maximo)
