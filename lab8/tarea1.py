from Countries_data import countries
#a) Crea una función llamada los idiomas más hablados en el mundo. 
# Debería devolver los 10 o 20 idiomas más hablados en el mundo en orden descendente.
from collections import Counter

def paises_mas_poblados(num_paises):
    paises_mas_poblados_mundo = sorted(countries, key=lambda x: x['population'], reverse=True)[:20]
    return paises_mas_poblados_mundo

def idiomas_mas_hablados_mundo(num_idiomas):
    contador_leguajes = Counter()
    
    for country in countries:
        lenguajes = country['languages']
        contador_leguajes.update(lenguajes)
    lenguajes_mas_top = contador_leguajes.most_common(num_idiomas) #en aqui se uso most_common para obtener los elemtos mas comunes o los que tienen los mayores valores
    return lenguajes_mas_top
#b) Crea una función llamada los países más poblados. Debería devolver
#  los 10 o 20 países más poblados en orden descendente.
top_idiomas = idiomas_mas_hablados_mundo(20)
print("Los 20 idiomas más hablados del mundo segun los datos son:")
for language, count in top_idiomas:
    print(f"{language}: {count} países")
paises_mas_poblados_ = paises_mas_poblados(20)
for index, country in enumerate(paises_mas_poblados_, start=1):
    print(f"{index}. {country['name']}: {country['population']}")