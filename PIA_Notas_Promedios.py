import pandas as pd
import random
SEPARADOR = ("~^~" * 27) + "\n"


notas_aleatorias = { \
    "Alcazar":[random.randrange(70, 101) for x in range(7)], \
    "Baez":[random.randrange(70,101) for x in range(7)], \
    "Cepeda":[random.randrange(70,101) for x in range(7)], \
    "Doria":[random.randrange(70,101) for x in range(7)], \
    "Martinez":[random.randrange(70,101) for x in range(7)], \
    "Silguero":[random.randrange(70,101) for x in range(7)], \
    "Zamora":[random.randrange(70,101) for x in range(7)]}
notas = pd.DataFrame(notas_aleatorias)
notas.index = ["Programacion de BD","Liderazgo, Emprendimiento","Macroeconomia","Creatividad", \
               "Estadistica Descriptiva","Contabilidad Administrativa","Estructura de D"]

notas.to_csv (r'Notas.csv',index=True, header=True)
print("¡Guardado!")
print(SEPARADOR)

notas1 = pd.read_csv("Notas.csv", index_col=0)
print(notas1)
print(SEPARADOR)

notas_p = {"Promedios": notas1.mean()}
print(notas_p)
print(SEPARADOR)

def estadistica_notas(notas2):
    notas2 = pd.Series(notas2)
    estadistica = pd.Series([notas_p["Promedios"].min(), notas_p["Promedios"].max(), notas2["Promedios"].mean(), notas2["Promedios"].std()], index=['Min', 'Max', 'Media', 'Desviacion tipica'])
    return estadistica
print(estadistica_notas(notas_p))
print(SEPARADOR)