from Countries_data import countries
#a
NUm_leng = set()
for country in countries:
    lenguajes = country['languages']
    NUm_leng.update(lenguajes)
total_lenguajes = len(NUm_leng)
print("Número total de idiomas:", total_lenguajes)

#b Encuentra los diez idiomas más hablados a partir de los datos.

contar_idiomas = {}
for country in countries:
    lenguajes = country['languages']
    for lenguaje in lenguajes:
        if lenguaje in contar_idiomas:
            contar_idiomas[lenguaje]+=1
        else:
            contar_idiomas[lenguaje] =1
leng_mas_habl = sorted(contar_idiomas.items(), key=lambda x: x[1], reverse=True)[:10] #en aqui solo se toman 10 items que es tomado por su valores y ordenados de forma asendente
print("Los 10 idiomas mas hablados apartir de los datos son")
for lenguaje, count in leng_mas_habl:
    print(f"{lenguaje}: {count} paises")
    
#c) Encuentra los 10 países más poblados del mundo.

paises_mas_poblados_mundo = sorted(countries, key=lambda x: x['population'], reverse=True)[:10]
print("Los diez países más poblados:")
for index, country in enumerate(paises_mas_poblados_mundo, start=1):
    print(f"{index}. {country['name']}: {country['population']}")