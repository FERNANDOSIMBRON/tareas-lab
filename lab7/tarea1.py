persona = {
'first_name': 'Edem',
'last_name': 'Terraza',
'age': 31,
'country': 'Peru',
'is_married': True, #
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}
#a
if 'skills' in persona:
    skill = persona['skills']
    if len(skill) >= 3:
        habilidad_medio = skill[len(skill) // 2]
        print("Habilidad del medio es:", habilidad_medio)
    else:
        print("No hay suficientes habilidades para determinar la habilidad del medio.")
else:
    print("La persona no tiene la clave 'skills' en su diccionario.")
#b
if 'skills' in persona:
    skill = persona['skills']
    if 'Python' in skill:
        print(f"La persona tiene la habilidad {'Python'}.")
    else:
        print("La persona no tiene la habilidad 'Python'.")
else:
    print("La persona no tiene la clave 'skills' en su diccionario.")
#c
if 'skills' in persona:
    skills = persona['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("Él es un desarrollador frontend.")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("Él es un desarrollador backend.")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("Él es un desarrollador fullstack.")
    else:
        print("Título desconocido.")
else:
    print("La persona no tiene la clave 'skills' en su diccionario.")