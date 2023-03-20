# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 11:42:36 2023

@author: Raimundo
"""

from Funciones import Equipo, Grupo, Bombo, actualizar_grupos_posibles, sorteo_a_listas

def sortear_libertadores(id_sorteo):
    grupos_posibles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    FLA = Equipo('Flamengo', 'Brasil', '', ['A'], 1)
    RIV = Equipo('River Plate', 'Argentina', '', grupos_posibles, 1)
    PAL = Equipo('Palmeiras', 'Brasil', '', grupos_posibles, 1)    
    BOC = Equipo('Boca Juniors', 'Argentina', '', grupos_posibles, 1)
    PAR = Equipo('Athletico Paranaense', 'Brasil', '', grupos_posibles, 1)
    NAC = Equipo('Nacional', 'Uruguay', '', grupos_posibles, 1)   
    IDV = Equipo('Independiente del Valle', 'Ecuador', '', grupos_posibles, 1) 
    OL = Equipo('Olimpia', 'Paraguay', '', grupos_posibles, 1)
    LIB = Equipo('Libertad', 'Paraguay', '', grupos_posibles, 2)
    AN = Equipo('Atlético Nacional', 'Colombia', '', grupos_posibles, 2)
    INT = Equipo('Internacional', 'Brasil', '', grupos_posibles, 2)
    BAR = Equipo('Barcelona', 'Ecuador', '', grupos_posibles, 2)
    RAC = Equipo('Racing', 'Argentina', '', grupos_posibles, 2)
    COR = Equipo('Corinthians', 'Brasil', '', grupos_posibles, 2)
    CC = Equipo('Colo Colo', 'Chile', '', grupos_posibles, 2)
    FLU = Equipo('Fluminense', 'Brasil', '', grupos_posibles, 2)
    BOL = Equipo('Bolívar', 'Bolivia', '', grupos_posibles, 3)
    STR = Equipo('The Strongest', 'Bolivia', '', grupos_posibles, 3)
    MEL = Equipo('Melgar', 'Perú', '', grupos_posibles, 3)
    AL = Equipo('Alianza Lima', 'Perú', '', grupos_posibles, 3)
    ARG = Equipo('Argentinos Juniors', 'Argentina', '', grupos_posibles, 3)
    MET = Equipo('Metropolitanos', 'Venezuela', '', grupos_posibles, 3)
    AUC = Equipo('Aucas', 'Ecuador', '', grupos_posibles, 3)
    MON = Equipo('Monagas', 'Venezuela', '', grupos_posibles, 3)
    LIV = Equipo('Liverpool', 'Uruguay', '', grupos_posibles, 4)
    DP = Equipo('Deportivo Pereira', 'Colombia', '', grupos_posibles, 4)
    NUB = Equipo('Ñublense', 'Chile', '', grupos_posibles, 4)
    PAT = Equipo('Patronato', 'Argentina', '', grupos_posibles, 4)
    G1 = Equipo('Atlético Mineiro', 'Brasil (Fase previa)', '', grupos_posibles, 4)
    G2 = Equipo('Sporting Cristal', 'Perú (Fase previa)', '', grupos_posibles, 4)
    G3 = Equipo('Cerro Porteño', 'Paraguay (Fase previa)', '', grupos_posibles, 4)
    G4 = Equipo('Independiente Medellín', 'Colombia (Fase previa)', '', grupos_posibles, 4)
    
    equipos = [FLA, RIV, PAL, BOC, PAR, NAC, IDV, OL, LIB, AN, INT, BAR, RAC, COR, CC, FLU,
               BOL, STR, MEL, AL, ARG, MET, AUC, MON, LIV, DP, NUB, PAT, G1, G2, G3, G4]
    # Quizás bombos deberían ser sólo listas
    B1 = Bombo(1, [equipo for equipo in equipos if equipo.bombo == 1])
    B2 = Bombo(2, [equipo for equipo in equipos if equipo.bombo == 2])
    B3 = Bombo(3, [equipo for equipo in equipos if equipo.bombo == 3])
    B4 = Bombo(4, [equipo for equipo in equipos if equipo.bombo == 4])
    bombos = [B1, B2, B3, B4]
    
    A = Grupo('A', [])
    B = Grupo('B', [])
    C = Grupo('C', [])
    D = Grupo('D', [])
    E = Grupo('E', [])
    F = Grupo('F', [])
    G = Grupo('G', [])
    H = Grupo('H', [])
    
    grupos = [A, B, C, D, E, F, G, H]
    
    A.incluir_equipo(FLA, B1)
    [bombo.sortear(equipos, grupos) for bombo in bombos]
    return sorteo_a_listas(id_sorteo, grupos)