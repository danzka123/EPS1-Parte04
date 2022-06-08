# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:46:14 2022

@author: alumno
"""

import os

# MENU PRODUCTO

def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido


def agregar_persona():
    print("\nAGREGAR PERSONA")
    print("---------------------------")
    archivo = 'dni.txt'
    contenido = input("DNI de persona: ")
    agregar_contenido_archivo(archivo, contenido)
    
    archivo1 = 'nombre.txt'
    contenido1 = input("Nombre de persona: ")
    agregar_contenido_archivo(archivo1, contenido1)
    
    archivo2 = 'apellido.txt'
    contenido2 = input("Apellido de persona: ")
    agregar_contenido_archivo(archivo2, contenido2)

def listar_persona():
    print("\nLISTAR PERSONA")
    print("------------------------------------")
    
    listar_dni = leer_archivo('dni.txt')
    listar_nombre = leer_archivo('nombre.txt')
    listar_apellido = leer_archivo('apellido.txt')
   
    dni = listar_dni.split(",")
    nom = listar_nombre.split(",")
    ape = listar_apellido.split(",")
 
    print("CÓDIGO\t\tPRODUCTO\t\tPRECIO")
    print("------------------------------------")
    for i  in range(len(dni)):
        print(f" {dni[i]}\t{nom[i]}\t\t{ape[i]}")

def salir():
    print("\nGracias... Vuelva pronto")  

def error():
    print("Opción incorrecta")


# OPERACIONES ARCHIVO


def agregar_contenido_archivo(nombre_archivo, contenido):
    archivo = open(nombre_archivo,"at")
    archivo.write("," + contenido)
    archivo.close()
   
def agregar_usuario():
    archivo = 'usuario.txt'
    contenido = input("Nuevo usuario:")
    agregar_contenido_archivo(archivo, contenido)
    
def agregar_clave():
    archivo = 'clave.txt'
    contenido = input("Nueva clave:")
    agregar_contenido_archivo(archivo, contenido)
    
def eliminar_archivo(nombre):
    os.remove(nombre)
    
def crea_archivo(nombre, contenido):
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()

def crear_archivo_usuario():
    archivo = 'usuario.txt'
    contenido= input('Nuevo usuario: ')
    crea_archivo(archivo, contenido)

def crear_archivo_clave():
    archivo = 'clave.txt'
    contenido= input('Nueva clave: ')
    crea_archivo(archivo, contenido)





