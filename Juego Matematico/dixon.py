import os
import time
import random
import operator

def titulo_persistente(var1,var2): ##llama al titulo
    os.system('cls')
    print("\t**********************************************")
    print("\t***          Juego Matematico!             ***")
    print("\t**********************************************")
    print("",var1,"-",var2,"-")
    print("\n\n")

def inicio(): ## llama al inicio
    titulo_persistente(6,7)
    print ("Realiza el ejercicio y responde correctamente!")
    print ("los resultados son aproximados por truncamiento")
    print ("\n\n")
    print ("Generando numeros al azar...")
    a=random.randint(0,10)
    b=random.randint(1,10)
    c=random.randint(0,10)
    d=random.randint(1,10)
    print (d,a,b,c)
    print ("\n\n")
    print ("Resuelve: (",a,"*",b,") +",c,"/",d,"= ?")
    parcial1 = a*b
    parcial2 = c/d
    total = int(parcial1 + parcial2)
    respuesta = int(input("Respuesta: "))
    
    if(respuesta == total): ## verifica respueta
        titulo_persistente()
        print("Respuesta correcta!")
        print("\n\n")
        print("te ganaste un pan duro!")
        print("\n\n")
        print("Vuelve a jugar...")
        print("Se actualizará en 5 segundos...!")
        time.sleep(5)
        inicio()
    
    else: ##incorrecta
        titulo_persistente(2,8)
        print("Esa no es la respuesta correcta :'(")
        print("la respuesta correcta era:",total,".")
        print("\n\n")
        print("Vuelve a intentarlo!")
        print("Se actualizará en 5 segundos...!")
        time.sleep(5)
        inicio()
    
inicio()
    
