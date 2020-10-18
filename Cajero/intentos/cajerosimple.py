import time
import os

def definir_valores():
  global usuario
  usuario = "20188471-3"
  global pin
  pin = int(1111)
  global intentos
  intentos= int(0)
  global bloqueado
  bloqueado= int(0)
  global admin
  admin= int(1)
  global saldo
  saldo= int(658320)
  global gaveta
  gaveta=int(50000000)
  global cobro_giro
  cobro_giro= int(480)
  global cobro_saldo
  cobro_saldo= int(300)
  global sesion
  sesion= int(0)
  global listasi
  listasi = ["Si","SI","si","sI","s","S"]
  print("Valores cargados correctamente!")
  print(usuario,pin,intentos,bloqueado,admin,saldo,gaveta,cobro_giro,cobro_saldo)

def titulo_persistente():
  os.system("cls")
  print("\n\n")
  print("\t********************************************************************************************")
  print("\t*****                      Primer banco del Principado de Sealand                     ******")
  print("\t*****                                Cajero Automatico                                ******")
  print("\t********************************************************************************************")
  print("\n\n")

def print_menu():
  if admin!=1:
    titulo_persistente()
    print("                    Ingresa el numero correspondiente a la opcion requerida                   \n\n")
    print("\t********************************************************************************************")
    print("")
    print("1- GIRO RAPIDO POR $10.000                                                 CONSULTA DE SALDO-6")
    print("")
    print("2- GIRO RAPIDO POR $20.000                                                 DEPOSITO A CUENTA-7")
    print("")
    print("3- GIRO RAPIDO POR $50.000                                                   CAMBIO DE CLAVE-8")
    print("")
    print("4- GIRO RAPIDO POR $100.000")
    print("")
    print("5- GIRO POR OTRO MONTO                                                                 SALIR-0")
    print("")
    print("\t********************************************************************************************")
  else:
    titulo_persistente()
    print("                    Ingresa el numero correspondiente a la opcion requerida                   \n\n")
    print("\t********************************************************************************************")
    print("")
    print("1- GIRO RAPIDO POR $10.000                                                 CONSULTA DE SALDO-6")
    print("")
    print("2- GIRO RAPIDO POR $20.000                                                 DEPOSITO A CUENTA-7")
    print("")
    print("3- GIRO RAPIDO POR $50.000                                                   CAMBIO DE CLAVE-8")
    print("")
    print("4- GIRO RAPIDO POR $100.000                                              MENU ADMINISTRATIVO-9")
    print("")
    print("5- GIRO POR OTRO MONTO                                                                 SALIR-0")
    print("")
    print("\t********************************************************************************************")

def desea_operacion():
  time.sleep(3)
  titulo_persistente()
  print("\n\nDesea otra operacion?\n\n")
  print("Escribe 'Si' o 'S' para volver al menu. Cualquier otra palabra para salir.")
  confirma = input("\n\nPor favor responde:")
  if confirma in listasi:
    menu()
  else:
    salir()

def inicio():
  titulo_persistente()
  definir_valores()
  print("\n\nBienvenido!\n\n")
  print("Verificando sesiones abiertas!")
  time.sleep(3)
  if sesion!=1:
    login()
  else:
    menu()

def login():
  titulo_persistente()
  nrocta = input("\n\nIngresa el numero de tu cuenta (RUT sin puntos, con guion y digito verificador):")
  if nrocta==usuario:
    if bloqueado!=1:
      verificar_pin()
    else:
      print("\n\nCuenta bloquedada!\n\n")
      time.sleep(5)
      login()
  else:
    titulo_persistente()
    print("\n\nUsuario Incorrecto! Por favor ingresa un número de cuenta válido.\n\n")
    time.sleep(3)
    login()

def verificar_pin():
  global intentos
  global sesion
  pinctastr = input("\n\nIngresa tu PIN:\n\n")
  pincta = int(pinctastr)
  print("Verificando tus datos, espera un momento por favor...")
  time.sleep(2)
  if pincta==pin:
    sesion=1
    titulo_persistente()
    print("\n\nAcceso correcto, bienvenido!\n\n")
    intentos=0
    time.sleep(3)
    menu()
  else:
    sesion=0
    titulo_persistente()
    if intentos<3:
      print("\n\nPIN o Clave Incorrecta, intentalo nuevamente!\n\n")
      print("Te recordamos que tu cuenta sera bloqueada tras 3 intentos fallidos!\n\n")
      intentos=intentos+1
      time.sleep(5)
      login()
    else:
      print("\n\nPIN o Clave Incorrecta!\n\n")
      print("Cuenta bloqueada!\n\n")
      bloqueado=1
      time.sleep(8)
      login()

def giro(dgiro):
  global saldo
  global gaveta
  if dgiro!=0:
    titulo_persistente()
    giro = int(dgiro)
    print("Realizaremos un Giro por",dgiro,", confirmas esta operacion?")
    print("Te recordamos que esta operacion tiene un costo de $480.")
    print("Escribe 'Si' o 'S' para confirmar. Cualquier otra palabra para anular.")
    confirma = input("\n\nPor favor confirma tu operacion: ")
    if confirma in listasi:
      titulo_persistente()
      print("Estamos realizando un giro por $",dgiro,". Por favor espere un momento.")
      time.sleep(2)
      if giro+cobro_giro <= saldo:
        if giro <= gaveta:
          saldo = saldo-giro
          saldo = saldo-cobro_giro
          time.sleep(1)
          print("Su nuevo saldo es $", saldo ," su operacion fue realizada exitosamente!")
          time.sleep(2)
          salida_billetes(giro)
        else:
          print("Temporalmente no podemos realizar esta operacion.")
          time.sleep(4)
          desea_operacion()
      else:
        print("Tu cuenta no tiene el saldo suficiente para realizar esta operacion.")
        time.sleep(4)
        desea_operacion()
    else:
      print("Anulaste la operacion.")
      time.sleep(3)
      desea_operacion()
  else:
    titulo_persistente()
    dgiro = input("\n\nPor favor ingresa el monto a girar: ")
    if dgiro.isdigit():
        giro = int(dgiro)
        print("Realizaremos un Giro por", dgiro ,", confirmas esta operacion?")
        print("Te recordamos que esta operacion tiene un costo de $480.")
        print("Escribe 'Si' o 'S' para confirmar. Cualquier otra palabra para anular.")
        confirma = input("\n\nPor favor confirma tu operacion: ")
        if confirma in listasi:
          titulo_persistente()
          print("Estamos realizando un giro por $", dgiro ,". Por favor espere un momento.")
          time.sleep(2)
          if (giro+cobro_giro<=saldo):
            if (giro<=gaveta):
              saldo = saldo-giro
              saldo = saldo-cobro_giro
              time.sleep(1)
              print("Su nuevo saldo es $", saldo ,"su operacion fue realizada exitosamente!")
              time.sleep(4)
              salida_billetes(giro)
            else:
              print("Temporalmente no podemos realizar esta operacion.")
              time.sleep(4)
              desea_operacion()
          else:
            print("Tu cuenta no tiene el saldo suficiente para realizar esta operacion.")
            time.sleep(4)
            desea_operacion()
        else:
          print("Anulaste la operacion.")
          time.sleep(2)
          desea_operacion()
    else:
        print("Ingresaste un monto invalido. Por favor intentalo nuevamente.")
        time.sleep(4)
        desea_operacion()

def consultasaldo():
  global saldo
  print("Realizaremos una consulta de saldo a la cuenta", usuario ,", confirmas esta operacion?")
  print("Te recordamos que esta operacion tiene un costo de $300.")
  print("Escribe 'Si' o 'S' para confirmar. Cualquier otra palabra para anular.")
  confirma = input("\n\nPor favor confirma tu operacion: ")
  if confirma in listasi:
      if saldo>=cobro_saldo:
        saldo=saldo-cobro_saldo
        time.sleep(2)
        print("Se ha generado un cobro por $300 por consulta de saldo.")
        print("Tu saldo actual es: $", saldo ,".")
        desea_operacion()
      else:
        print("Saldo insuficiente para esta operacion!")
        time.sleep(2)
        desea_operacion()
  else:
    print("Anulaste la operacion.")
    time.sleep(4)
    desea_operacion()

def deposito():
  global saldo
  global gaveta
  print("Estas haciendo un deposito a la cuenta", usuario ,".\n")
  print("Cual es el monto a depositar?")
  montodepositostr = input("\n\nMonto a depositar: ")
  if montodepositostr.isdigit():
      montodeposito = int(montodepositostr)
      print("\n\nRealizaremos un deposito de $", montodeposito ," a la cuenta", usuario ,", confirmas esta operacion?")
      print("\nEscribe 'Si' o 'S' para confirmar. Cualquier otra palabra para anular.")
      confirma = input("\n\nPor favor confirma tu operacion: ")
      if confirma in listasi:
        gaveta= gaveta+montodeposito
        saldo= saldo+montodeposito
        time.sleep(2)
        print("Su nuevo saldo es $", saldo ,"su operacion fue realizada exitosamente!")
        time.sleep(3)
        desea_operacion()
      else:
        print("Anulaste la operacion.")
        time.sleep(2)
        desea_operacion()
    else:
        print("Ingresaste un monto invalido. Por favor intentalo nuevamente.")
        time.sleep(4)
        desea_operacion()
              
def cambiopin():
  global pin
  print("Estas cambiando el PIN de la cuenta", usuario ,".\n")
  pinactualstr = input("\nPor favor ingresa tu PIN actual: ")
  pinactual=int(pinactualstr)
  pinnuevostr = input("\nPor favor ingresa tu nuevo PIN: ")
  if pinnuevostr.isdigit():
      pinnuevo=int(pinnuevostr)
      if pinactual==pin:
        if pinactual!=pinnuevo:
          print("\n\nRealizaremos el cambio de PIN de la cuenta", usuario ,", confirmas esta operacion?")
          print("\nEscribe 'Si' o 'S' para confirmar. Cualquier otra palabra para anular.")
          confirma = input("\n\nPor favor confirma tu operacion: ")
          if confirma in listasi:
            pin = pinnuevo
            time.sleep(2)
            print("El cambio de PIN fue realizado correctamente. Por favor ingresa con tu nueva clave.")
            time.sleep(2)
            salir()
          else:
            print("Anulaste la operacion.")
            time.sleep(2)
            desea_operacion()
        else:
          print("El nuevo PIN no puede ser igual al anterior!")
          time.sleep(2)
          desea_operacion()
      else:
        print("Tu PIN actual es INCORRECTA, por favor intentalo nuevamente.")
        time.sleep(4)
        desea_operacion()
  else:
    print("El PIN solo acepta Digitos! Intentalo nuevamente.")
    time.sleep(4)
    desea_operacion()

def menuadmin():
  global usuario
  global pin
  global saldo
  global gaveta
  global admin
  print("1 para cambio de usuario, 2 para cambio de PIN, 3 para quitar admin, 4 para modificar saldo, 5 para cargar gaveta, 0 para salir al menu.")
  opcionstr = input("\n\nPor favor elige una opcion: ")
  opcion = int(opcionstr)
  if opcion==1:
    newusuario = input("\n\nPor favor ingresa un nuevo RUT para el usuario: ")
    usuario = newusuario
    print("Cambiado correctamente, el nuevo usuario es:", usuario ,".")
    time.sleep(2)
    menuadmin()
  elif opcion==2:
    newpin = input("\n\nPor favor ingresa un nuevo PIN para el usuario: ")
    pin = newpin
    print("Cambiado correctamente, el nuevo PIN es:", pin ,".")
    time.sleep(2)
    menuadmin()
  elif opcion==3:
    confirma = input("\n\nPor favor confirma el RUT del usuario: ")
    if confirma==usuario:
      admin = 0
      print("Cambiado correctamente, el usuario", usuario ," ya no es admin.")
      time.sleep(2)
      menuadmin()
    else:
      print("Usuario Incorrecto, intenta nuevamente!")
      menuadmin()
  elif opcion==4:
    newsaldo = input("\n\nPor favor ingresa un nuevo SALDO para el usuario: ")
    saldo = newsaldo
    print("Cambiado correctamente, el nuevo SALDO es: $", saldo ,".")
    time.sleep(2)
    menuadmin()
  elif opcion==5:
    gaveta = gaveta+10000000
    print("Se han agregado $10.000.000 a la gaveta. El nuevo monto en gaveta es: $", gaveta ,".")
    time.sleep(2)
    menuadmin()
  elif opcion==0:
    print("Volviendo al menu principal!")
    time.sleep(2)
    menu()
  else:
    print("\n\nOpcion incorrecta, intentalo nuevamente!\n\n")
    time.sleep(2)
    menuadmin()
              
def salir():
  print("Muchas gracias por preferir nuestros servicios, hasta luego!")
  print("No olvides retirar todas tus posesiones del cajero!")
  time.sleep(5)
  sesion=0
  login()

def salida_billetes(cantidad):
  titulo_persistente()
  print("**ruidito de billetes**")
  time.sleep(3)
  print("___________________________________")
  print("|#######====================#######|")
  print("|#(1)*    SEALAND DOLLAR      *(1)#|")
  print("|#**          /===\   ********  **#|")
  print("|*# {G}      | (') |             #*|")
  print("|#*  ******  | /v\ |    O N E    *#|")
  print("|#(1)         \===/            (1)#|")
  print("|##======ONE SEALAND DOLLAR======##|")
  print("------------------------------------")
  time.sleep(3)
  print("Retira tus ", cantidad ,"dolares de SEALAND. Son ", cantidad ,"billetes de 1 dolar.")
  time.sleep(6)
  desea_operacion()
    
    
def menu():
  if sesion==1:
    print_menu()
    opcionstr = input("\n\nPor favor elige una opcion: ")
    opcion = int(opcionstr)
    if opcion==1:
      giro(10000)
    elif opcion==2:
      giro(20000)
    elif opcion==3:
      giro(50000)
    elif opcion==4:
      giro(100000)
    elif opcion==5:
      giro(0)
    elif opcion==6:
      consultasaldo()
    elif opcion==7:
      deposito()
    elif opcion==8:
      cambiopin()
    elif opcion==9:
      menuadmin()
    elif opcion==0:
      salir()
    else:
      titulo_persistente()
      print("\n\nOpcion incorrecta, intentalo nuevamente!\n\n")
      time.sleep(3)
      menu()
  else:
    print("No logeado! Fuera de aqui!!!!! **patada de espartano**")
    login()

inicio()
