import time,os

def titulo_persistente():
    os.system('cls')
    print("\t**********************************************")
    print("\t***              Jorge Labraña             ***")
    print("\t**********************************************")
    print("\n\n")
    print("Contador de segundos!")
    print("\n\n")

def printrepetitivo(var1,var2):
    if(var1 <= var2):
        print("Contador es igual a",var1)
        global contador
        contador=var1
        contador=contador+1
        time.sleep(1)
        printrepetitivo(contador,numero)
    else:
        print("El contador ha terminado!")
        print("El programa se cerrara en 5s!")
        time.sleep(5)
titulo_persistente()
numero=int(input("Ingresa una cantidad de segundos a contar"))

printrepetitivo(0,numero)
