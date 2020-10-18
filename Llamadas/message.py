import os, time

def titulo_persistente():
    os.system('cls')
    print("\t**********************************************")
    print("\t***              Jorge Labraña             ***")
    print("\t**********************************************")
    print("\n\n")
    print("Calculadora de precios!")
    print("\n\n")

def error():
    titulo_persistente()
    print("Por favor, ingresa correctamente los datos!")
    print("\n")
    print("El script se reiniciará en 5 segundos!")
    time.sleep(5)
    start()
    
def minutos():
    titulo_persistente()
    print("Ingresa los datos correspondientes cuando se te soliciten...")
    print("\n\n")
    print("Ingrese el numero de minutos de su llamada")
    global minutos
    minutosstring=input("Minutos:")
    try:
        val = int(minutosstring)
        minutos = int(minutosstring)  
    except ValueError:
        error()
    diasemana()
    
def diasemana():
    titulo_persistente()
    print("Ingresa los datos correspondientes cuando se te soliciten...")
    print("\n\n")
    print("Ingresa la inicial del día en que hiciste tu llamada... (Lunes=L, Martes=M, etc...)")
    global dia
    dia=input('Dia:')
    preguntahorario()
    
def preguntahorario():
    titulo_persistente()
    print("Ingresa los datos correspondientes cuando se te soliciten...")
    print("\n\n")
    print("Ingresa la hora en que hiciste tu llamada (EJ: 1, 2, 3, 12, 15, 19, 21)")
    global turno
    turno=input('Hora: ')
    verificacion()
    
def calculo(var1,var2,var3):
    habil = ["L", "M", "J", "V"]
    if  dia == "D" or dia == "S":
        global llamadamasiva
        llamadamasiva = llamada + var1
        print("Total (llamada + cobros de servicio): ",llamadamasiva," ")
        print("\n\n")
        print("El total de su llamada fue de ",llamadamasiva," ")
        print("\n\n")
        print("este script se cerrara en 15 segundos...")
        time.sleep(15)
    
    elif  dia in habil:
        horahabil = ["8","9","10","11","12","13","14","15","16","17","18","19"]
        horanohabil = ["1","2","3","4","5","6","7","20","21","22","23","24","0"]
        if turno in horahabil :
            llamadamasiva = llamada + var2
            print("Total (llamada + cobros de servicio): ",llamadamasiva," ")
            print("\n\n")
            print("El total de su llamada fue de ",llamadamasiva," ")
            print("\n\n")
            print("este script se cerrara en 15 segundos...")
            time.sleep(15)
        elif turno in horanohabil :
            llamadamasiva = llamada + var3
            print("Total (llamada + cobros de servicio): ",llamadamasiva," ")
            print("\n\n")
            print("El total de su llamada fue de ",llamadamasiva," ")
            print("\n\n")
            print("este script se cerrara en 15 segundos...")
            time.sleep(15)
        else :
            error()
    else :
            error()
            
            
def inicio():
    titulo_persistente()
    print("Bienvenido a la calculadora de precios de llamadas!")
    time.sleep(3)
    minutos()
            
def verificacion():
    global llamada
    if minutos <= 5 :
            llamada = minutos * 1.00
            print(f"El cobro por minuto de su llamada es: ",llamada," ")
            calculo(0.03,0.15,0.10)

    elif minutos >= 6 and minutos <= 8 :
            llamada = minutos * 1.00
            print(f"El cobro por minuto de su llamada es: ",llamada," ")
            calculo(0.03,0.15,0.10)

    elif minutos >= 9 and minutos <= 10 :
            llamada = 0.7 * (minutos - 8) +  7.4
            print(f"El cobro por minuto de su llamada es: ",llamada," ")
            calculo(0.03,0.15,0.10)

    elif minutos >= 11 :
            llamada =  0.5 * (minutos - 10) +  8.80
            print(f"El cobro por minuto de su llamada es: ",llamada," ")
            calculo(0.03,0.15,0.10)

inicio()
