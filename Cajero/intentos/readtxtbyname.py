import time
import os

def definir_valores_cajero():
    opentxt = open("cajero.txt", "r")
    resultado = opentxt.read().split("-")
    print (resultado)
    print (len(resultado))
    opentxt.close()
    global datauser
    datauser = []
    global gaveta
    gaveta=int(resultado[0])
    global sesion
    sesion= int(resultado[1])
    global listasi
    listasi = resultado[2]
    print (listasi)
    print("Valores cargados correctamente!")
    print(datauser,gaveta,sesion,listasi)

def guardar_valores_cajero():
    listaescribir = [gaveta,sesion,listasi]
    escribir = '-'.join(str(i) for i in listaescribir)
    print (escribir)
    with open("cajero.txt", "w") as output:
      output.write(str(escribir))

def definir_valores_usuario(cuenta):
    #leemos archivo
    strtxt = ".txt"
    nombretxt = str(cuenta)+str(strtxt)
    opentxt = open(nombretxt, "r")
    resultado = opentxt.read().split(",")
    print (resultado)
    print (len(resultado))
    opentxt.close()
    #definimos variables del usuario
    global usuario
    usuario = resultado[0]
    global nombreusuario
    nombreusuario = resultado[1]
    global pin
    pin = resultado[2]
    global intentos
    intentos= int(resultado[3])
    global bloqueado
    bloqueado= int(resultado[4])
    global admin
    admin = int(resultado[5])
    global saldo
    saldo = int(resultado[6])
    global nombretipocta
    nombretipocta = resultado[7]
    global tipocta
    tipocta = resultado[8]
    global cobrogiro
    cobrogiro = int(resultado[9])
    global cobrosaldo
    cobrosaldo = int(resultado[10])
    print("Valores cargados correctamente!")
    print(usuario,nombreusuario,pin,intentos,bloqueado,admin,saldo,nombretipocta,tipocta,cobrogiro,cobrosaldo)
    
def guardar_valores_usuario(cuenta):
    strtxt = ".txt"
    nombretxt = str(cuenta)+str(strtxt)
    listaescribir = [usuario,nombreusuario,pin,intentos,bloqueado,admin,saldo,nombretipocta,tipocta,cobrogiro,cobrosaldo]
    escribir = ','.join(str(i) for i in listaescribir)
    print (escribir)
    with open(nombretxt, "w") as output:
      output.write(str(escribir))

definir_valores_cajero()
guardar_valores_cajero()
