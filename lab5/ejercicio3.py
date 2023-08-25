lista1 = list(range(1,10))
lista2 = list(range(5,16))
lista3 = list(range(10,21))

conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

print("el primer conjunto: ",conjunto1)
print("el segundo conjunto: ",conjunto2)
print("el tercer conjunto: ",conjunto3)
#b
interseccion = conjunto1.intersection(conjunto2, conjunto3)
print("los numero presentes en las tres listas es:", interseccion)

#c
union = conjunto1.union(conjunto2, conjunto3)
print("El conjunto union es:", union)

#d
diferencia = conjunto1.difference(conjunto3)
print("la diferencia entre el primer conjunto y el ultimo es:", diferencia)

#e
tupla1 = tuple(interseccion)
tupla2 = tuple(union)
tupla3 = tuple(diferencia)
print(tupla3)
#sumar
prim_ult_interseccion = tupla1[0] + tupla1[-1]
prim_ult_union = tupla2[0] + tupla2[-1]
prim_ult_diferencia = tupla3 + tupla3

print("La suma de su primer elemento de la primer tupla:", prim_ult_interseccion,"\n de la segunda:", prim_ult_union,
      "\n de la tercera:", prim_ult_diferencia)

