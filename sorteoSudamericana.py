# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:27:32 2023

@author: Raimundo
"""

import random
from collections import defaultdict, namedtuple
import pandas as pd
from constraint import Problem, AllDifferentConstraint


Equipo = namedtuple('Equipo', ['nombre', 'pais', 'bombo'])
equipos = [
    Equipo('Peñarol', 'Uruguay',   1),
    Equipo('Sao Paulo', 'Brasil',   1),
    Equipo('Santos', 'Brasil',   1),
    Equipo('Liga de Quito', 'Ecuador',   1),
    Equipo('Estudiantes de La Plata', 'Argentina',   1),
    Equipo('Emelec', 'Ecuador',   1),
    Equipo('San Lorenzo', 'Argentina',   1),
    Equipo('Independiente Santa Fe', 'Colombia',   1),
    Equipo('Defensa y Justicia', 'Argentina',   2),
    Equipo('Guaraní', 'Paraguay',   2),
    Equipo('Bragantino', 'Brasil',   2),
    Equipo('Universitario', 'Perú',   2),
    Equipo('Deportes Tolima', 'Colombia',   2),
    Equipo("Newell's", 'Argentina',   2),
    Equipo('Botafogo', 'Brasil',   2),
    Equipo('Palestino', 'Chile',   2),
    Equipo('Oriente Petrolero', 'Bolivia',   3),
    Equipo('Estudiantes de Mérida', 'Venezuela',   3),
    Equipo('Danubio', 'Uruguay',   3),
    Equipo('Tigre', 'Argentina',   3),
    Equipo('América MG', 'Brasil',   3),
    Equipo('Blooming', 'Bolivia',   3),
    Equipo('Goiás', 'Brasil',   3),
    Equipo('Universidad César Vallejo', 'Perú',   3),
    Equipo('Audax Italiano', 'Chile',   4),
    Equipo('Gimnasia de La Plata', 'Argentina',   4),
    Equipo('Puerto Cabello', 'Venezuela',   4),
    Equipo('Tacuary', 'Paraguay',   4),
    Equipo('Millonarios', 'Colombia',   4),
    Equipo('Huracán', 'Argentina',   4),
    Equipo('Fortaleza', 'Brasil',   4),
    Equipo('Magallanes', 'Chile',   4)
]


mapeo_bombo_equipo= defaultdict(list)  # dict[pot, list[club]]
mapeo_equipo_bombo = {}  # dict[club, pot]

mapeo_pais_equipo = defaultdict(list)  # dict[country, list[club]]
mapeo_equipo_pais = {}  # dict[club, country]

for equipo in equipos:
    mapeo_bombo_equipo[equipo.bombo].append(equipo.nombre)
    mapeo_equipo_bombo[equipo.nombre] = equipo.bombo

    mapeo_pais_equipo[equipo.pais].append(equipo.nombre)
    mapeo_equipo_pais[equipo.nombre] = equipo.pais
    
nombres_equipos = list(mapeo_equipo_pais.keys())
n_equipos = len(equipos)
grupos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
bombos = [1, 2, 3, 4]

def sorteo_posible(assignment = None):
    if not assignment:
        assignment = {}
    
    problema = Problem()
    #Asigna grupos posibles a cada equipo
    for nombre in nombres_equipos:
            if nombre in assignment:
                problema.addVariable(nombre, assignment.get(nombre))
            else:
                problema.addVariable(nombre, grupos)
        
    # Equipos del mismo bombo no pueden estar en mismo grupo
    for _, equipos_del_bombo in mapeo_bombo_equipo.items():
        problema.addConstraint(AllDifferentConstraint(), equipos_del_bombo)
        
    # Equipos del mismo país no pueden estar en mismo grupo
    for pais, equipos_del_pais in mapeo_pais_equipo.items():
        problema.addConstraint(AllDifferentConstraint(), equipos_del_pais)
        
    return problema.getSolution()

valid_assignment_hashes = set()

def simular(sorteo_parcial=None):
    """Simulate the draw procedure to produce a draw that satisfies the constraints."""
    
    sorteo = {}
    if sorteo_parcial:
        sorteo.update(sorteo_parcial)
    
    for bombo, equipos_del_bombo in mapeo_bombo_equipo.items():
        grupos_del_bombo = grupos.copy()

        # The pot_clubs list could be randomly shuffled to mimic the actual draw procedure.
        # However, a random shuffle should not affect the resulting probabilities.
        random.shuffle(equipos_del_bombo)
        for equipo in equipos_del_bombo:
            if equipo in sorteo:
                continue
            grupos_posibles = []

            for grupo in grupos_del_bombo:
                assignment = sorteo.copy()
                assignment[equipo] = grupo

                assignment_hash = hash(frozenset(assignment.items()))
                if assignment_hash in valid_assignment_hashes:
                    grupos_posibles.append(grupo)
                else:
                    sorteo_factible = sorteo_posible(assignment)
                    if sorteo_factible:
                        grupos_posibles.append(grupo)
                        valid_assignment_hashes.add(assignment_hash)

            grupo_seleccionado = grupos_posibles[0]
            sorteo[equipo] = grupo_seleccionado
            grupos_del_bombo.remove(grupo_seleccionado)

    return sorteo

def sorteo_a_dataframe(sorteo):
    equipos = sorteo.keys()
    grupos = sorteo.values()
    paises = [mapeo_equipo_pais[equipo] for equipo in equipos]
    bombos = [mapeo_equipo_bombo[equipo] for equipo in equipos]
    df = pd.DataFrame({'Grupo': grupos, 'Equipo': equipos, 'País': paises,
                       'Bombo': bombos})
    df.sort_values(by = ['Grupo', 'Bombo'], inplace = True)
    df = df.pivot(index ='Bombo', columns='Grupo', values='Equipo')
    return df

