import os
from Environment import *

iniciado = 0
actual_cycle = 0
actual_environment=Environment(25,100)

def copyright():
    os.system("cls")
    print("\n\n")
    print("\t******************************************************************")
    print("\t***                                                            ***")
    print("\t***                  Propiedad intelectual de:                 ***")
    print("\t***                Jorge Labraña, Juan Pablo Grez,             ***")
    print("\t***             Fernando Monsalves y Romina Álvarez            ***")
    print("\t***                    Licencia GNU GPL v3.0                   ***")
    print("\t***                                                            ***")
    print("\t***      El detalle del proyecto puede ser encontrado en:      ***")
    print("\t***           https://github.com/ThilahT/UAutonoma             ***")
    print("\t***                                                            ***")
    print("\t******************************************************************")
    print("\n\n")
    os.system("pause")
    start()

def banner():
    os.system("cls")
    print("\n")
    print("\t****************************************************************************")
    print("\t*****                         Proyecto Número 1                       ******")
    print("\t*****                            Programación                         ******")
    print("\t****************************************************************************")
    print("\n")

def start():
    os.system("cls")
    print("\n")
    print("\t****************************************************************************")
    print("\t*****                         Programa iniciado                       ******")
    print("\t****************************************************************************")
    print("\n")
    game()

def game():
    banner()
    print("Ingresar 0 para obtener un reporte completo, -1 para reiniciar y -2 para terminar el juego!")
    print("Ingrese cantidad de rondas a ejecutar:")
    cycles = input()
    if cycles:
        if cycles.isdigit:
            cycles = int(cycles)
            if cycles == 0:
                banner()
                actual_environment.print_environment()
                os.system("pause")
                game()
            if cycles == -1:
                temp = True
                while temp:
                    print("Por favor ingresa un tamaño para el mapa (ingresa solo integros, se convertirán a m2)")
                    map_size = input("Ingresa un tamaño:")
                    if map_size:
                        if map_size.isdigit():
                            map_size = int(map_size)
                            temp = False
                        else:
                            print("Por favor ingresa solo integros")
                    else:
                        map_size = 100
                        print("Se aplicará valor por defecto de 100.")
                        temp = False
                temp = True
                while temp:
                    print("Por favor ingresa una cantidad de entidades a generar. Esta no puede ser mayor que: ",int(map_size*map_size))
                    initial_entitys = input("Ingresa una cantidad:")
                    if initial_entitys:
                        if initial_entitys.isdigit():
                            initial_entitys = int(initial_entitys)
                            if initial_entitys < (map_size*map_size):
                                temp = False
                            else:
                                initial_entitys = 50
                                print("Valor  muy alto, se aplicará valor por defecto de 50.")
                                temp = False
                        else:
                            print("Por favor ingresa solo integros")
                    else:
                        initial_entitys = 50
                        print("Se aplicará valor por defecto de 50.")
                        temp = False
                actual_environment.reset(initial_entitys,map_size)
                game()
            elif cycles == -2:
                close()
            elif cycles < -2:
                print("Error, no ingresar rondas negativas!")
                game()
            else:
                actual_environment.new_cycle(cycles)
                global actual_cycle
                actual_cycle = actual_cycle + cycles
                game()
        else:
            print("Favor solo ingresar integros.")
            game()
    else:
        print("Favor ingresar el valor de forma correcta.")
        game()
        
def close():
    banner()
    print("Esta ventana se cerrará.")
    os.system("pause")



copyright()


