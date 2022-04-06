from os import system
from animal import *
# VARIABLES

animales = []

# FUNCIONES

def agregarAnimal(dato, nombre, edad):
    if dato == 1:
        newAnimal = Perro(nombre, edad)
        animales.append(newAnimal)
    elif dato == 2:
        newAnimal = Guacamaya(nombre, edad)
        animales.append(newAnimal)
    elif dato == 3:
        newAnimal = Cerdo(nombre, edad)
        animales.append(newAnimal)     
    elif dato == 4:
        newAnimal = Puma(nombre, edad)
        animales.append(newAnimal)   

def verAnimales():
    print("******************")
    for i in animales:
        print("Animal")
        print("Nombre: ", i.nombre, "\nEdad: ", i.edad)
        i.tipoAnimal()
        i.sonidoAnimal()
        print("\n")
    print("******************")

# MAIN
while True:
    print("********* CORRAL DE ANIMALES **********")
    print("     1) Agregar animal")
    print("     2) Ver animales")
    print("     0) Salir")
    print("***************************************")

    op = int(input("Ingrese una opción:"))

    if op > 3 or op < 0:
        print("¡Debe ingresar un numero mayor que 0 y menor que 3!")

    elif op == 0:
        break

    elif op == 1:
        system("clear")
        print("¿Qué animal desea agregar?")
        print("1) Perro")
        print("2) Guacamaya")
        print("3) Cerdo")
        print("4) Puma")
        op2 = int(input())

        if op2 > 0 and op2 < 5:
            system("clear")
            nom = input("Ingrese el nombre del animal: ")
            ed = input ("Ingrese edad del animal: ")
            agregarAnimal(op2, nom, ed)
            system("clear")

        else:
            system("clear")
            print("¡Debe ingresar un numero mayor que 0 y menor que 5!")
    
    while op == 2:
        system("clear")
        verAnimales()
        out = input("Escriba 'q' para salir")
        if out == "q":
            system("clear")
            break