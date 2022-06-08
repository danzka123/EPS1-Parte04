
"""
Created on Wed Jun  8 09:45:57 2022

@author: alumno
"""

import metodo as m

def menu():
    print("\n*********MENU PRINCIPAL***********")
    print("1. Listar persona")
    print("2. Agregar persona")
    print("3. Salir")
    
    
contador = 1
def validar(a):
    
    usuario = m.leer_archivo('login.txt')
    contraseña = m.leer_archivo('clave.txt')
    numero = a
    
    print("\n\n*********LOGIN***********")
        
    dato1 = input('\nIngrese usuario: ')
    dato2 = input('Ingrese la clave: ')
    
    if numero <= 2:
        if usuario == dato1 and contraseña == dato2:
             print("\n¡BIENVENIDO AL PROGRAMA!\n")
             
             opcion = 1
             while opcion <= 3:
                 menu()
                 opcion = int(input("Seleccione una opción [1-3]: "))
                 if opcion == 1:
                     m.listar_persona()
                 elif opcion == 2:
                     m.agregar_persona()
                 elif opcion == 3:
                     m.salir()
                 else:
                     m.error()
        else:            
            print("\n*Usuario y/o clave incorrectos...*\n")               
            contador = numero+1                
            validar(contador)
         
    else:
          print("\n***Ha sobrepasado el número de intentos. BYE :D...***\n")
          m.salir()
        
validar(1)

