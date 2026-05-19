# Matriz con nombre y horas trabajadas
recursos = [
    ["Carlos", 8, 9, 8, 9, 8],
    ["Ana", 7, 8, 8, 7, 8],
    ["Luis", 10, 9, 10, 9, 9],
    ["María", 8, 8, 8, 8, 8]
]

# Función para calcular total y clasificación
def calcular_horas(recurso):
    nombre = recurso[0]
    horas = recurso[1:]

    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total, clasificacion

# Mostrar resultados
print("REPORTE SEMANAL DE HORAS\n")

for recurso in recursos:
    nombre, total, clasificacion = calcular_horas(recurso)

    print(f"Recurso: {nombre}")
    print(f"Total Horas: {total}")
    print(f"Clasificación: {clasificacion}")
    print("-----------------------------")