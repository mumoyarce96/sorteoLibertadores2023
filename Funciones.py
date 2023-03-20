# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:06:35 2023

@author: Raimundo
"""
import random
from collections import Counter

class Bombo:
    def __init__(self, numero, equipos):
        self.numero = numero
        self.equipos = equipos
        
    def obtener_equipo(self):
        equipo_seleccionado = random.choice(self.equipos)
        return(equipo_seleccionado)
    
    def mostrar_equipos(self):
        [equipo.mostrar_grupos_posibles() for equipo in self.equipos]
    
    def sortear(self, equipos, grupos): 
            actualizar_grupos_posibles(equipos, grupos, self)
            grupos_disponibles = [grupo.letra for grupo in grupos]
            while len(self.equipos) > 0: 
                equipo_sorteado = self.obtener_equipo()
                for grupo in grupos:
                    if grupo.letra == equipo_sorteado.grupos_posibles[0] and len(grupo.equipos) < self.numero:
                        grupo.incluir_equipo(equipo_sorteado, self)
                        grupos_disponibles.remove(grupo.letra)
                        actualizar_grupos_posibles(equipos, grupos, self)
            return
        
class Equipo:
    def __init__(self, nombre, pais, grupo, grupos_posibles, bombo):
        self.nombre = nombre
        self.pais = pais
        self.grupo = grupo
        self.grupos_posibles = grupos_posibles
        self.bombo = bombo
            
    def actualizar_grupos_posibles(self, grupos):
        self.grupos_posibles = [grupo.letra for grupo in grupos if self.pais not in grupo.paises_en_grupo and len(grupo.equipos) < self.bombo]

    def mostrar_grupos_posibles(self):
        print(f'{self.nombre} - {self.grupos_posibles}')
        
class Grupo:
    def __init__(self, letra, equipos):
        self.letra = letra
        self.equipos = equipos
        self.paises_en_grupo =  [equipo.pais for equipo in self.equipos]

    def actualizar_paises(self):
        self.paises_en_grupo = [equipo.pais for equipo in self.equipos]
    
    def incluir_equipo(self, equipo, bombo):
        self.equipos += [equipo]
        equipo.grupo = self.letra
        self.actualizar_paises()
        bombo.equipos.remove(equipo)
    
    def mostrar_equipos(self):
        print(f'Grupo {self.letra}:')
        [print(equipo.nombre) for equipo in self.equipos]
        
def lista_mas_repetida(listas):
        min_len = len(min(listas, key = (len)))
        mas_cortos = [lista for lista in listas if len(lista) == min_len]
        counter = Counter(tuple(sub_list) for sub_list in mas_cortos)
        info_mas_comun = counter.most_common()
        lista_mas_comun = list(info_mas_comun[0][0])
        n_repeticiones = info_mas_comun[0][1]
        set_mas_comun = set(lista_mas_comun)
        return set_mas_comun, n_repeticiones

  
def actualizar_grupos_posibles(equipos, grupos, bombo):
    [equipo.actualizar_grupos_posibles(grupos) for equipo in bombo.equipos]  
    for equipo in bombo.equipos:
        if len(equipo.grupos_posibles) == 1:
            grupo_obligado = equipo.grupos_posibles[0]
            for grupo in grupos:
                if grupo.letra == grupo_obligado:
                    grupo.incluir_equipo(equipo, bombo)
                    actualizar_grupos_posibles(equipos, grupos, bombo)
                    return
    grupos_posibles = [equipo.grupos_posibles for equipo in bombo.equipos]
    if len(grupos_posibles) > 0:
        set_mas_comun, n_repeticiones = lista_mas_repetida(grupos_posibles)
        if n_repeticiones == len(set_mas_comun):
            for i, lista_equipo in enumerate(grupos_posibles):
               set_equipo = set(lista_equipo)
               if set_equipo != set_mas_comun:
                   equipo = bombo.equipos[i]
                   equipo.grupos_posibles = list(set_equipo.difference(set_mas_comun)) 
             
    for i, lista_equipo_1 in enumerate(grupos_posibles):
        for letra in lista_equipo_1: 
            unique = True
            for lista_equipo_2 in grupos_posibles:
                if lista_equipo_2 is not lista_equipo_1 and letra in lista_equipo_2:
                    unique = False
                    break
            if unique:
                for grupo in grupos:
                    if grupo.letra == letra:
                        equipo = bombo.equipos[i]
                        grupo.incluir_equipo(equipo, bombo)
                        actualizar_grupos_posibles(equipos, grupos, bombo)
                        return
                             
def sorteo_a_listas(id_sorteo, grupos):
    lista = []
    for grupo in grupos:
        for equipo in grupo.equipos:
            lista.append([id_sorteo, grupo.letra, equipo.nombre, equipo.pais, equipo.bombo])
    return lista