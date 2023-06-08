def obtener_states(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()

    inicio_bloque = 'states'
    fin_bloque = 'endstates'

    inicio = contenido.find(inicio_bloque)
    fin = contenido.find(fin_bloque)

    if inicio == -1 or fin == -1:
        return []  # Si no se encuentra uno de los bloques, retorna un arreglo vacío

    inicio += len(inicio_bloque)
    contenido_bloque = contenido[inicio:fin].strip()
    arreglo_contenido = contenido_bloque.split(',')

    return [s.strip() for s in arreglo_contenido]


def obtener_action(archivo, direction):
    with open(archivo, 'r') as f:
        contenido = f.read()

    inicio_bloque = 'action move-' + direction
    fin_bloque = 'endaction'

    inicio = contenido.find(inicio_bloque)
    fin = contenido.find(fin_bloque)

    if inicio == -1 or fin == -1:
        return []  # Si no se encuentra uno de los bloques, retorna un arreglo vacío

    inicio += len(inicio_bloque)
    contenido_bloque = contenido[inicio:fin].strip()
    lineas = contenido_bloque.split('\n')

    arreglo_contenido = []
    for linea in lineas:
        elementos = linea.split()
        arreglo_contenido.append(elementos)

    return arreglo_contenido


def obtener_cost(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()

    inicio_bloque = 'cost'
    fin_bloque = 'endcost'

    inicio = contenido.find(inicio_bloque)
    fin = contenido.find(fin_bloque)

    if inicio == -1 or fin == -1:
        return []  # Si no se encuentra uno de los bloques, retorna un arreglo vacío

    inicio += len(inicio_bloque)
    contenido_bloque = contenido[inicio:fin].strip()
    lineas = contenido_bloque.split('\n')

    arreglo_contenido = []
    for linea in lineas:
        elementos = linea.split()
        arreglo_contenido.append(elementos)

    return arreglo_contenido


# Leer el archivo
archivo = './PruebasGrid/FixedGoalInitialState/navigation_1.net'
states = obtener_states(archivo)
actions_south = obtener_action(archivo, 'south')
actions_north = obtener_action(archivo, 'north')
actions_west = obtener_action(archivo, 'west')
actions_east = obtener_action(archivo, 'east')
cost = obtener_cost(archivo)
print(cost)