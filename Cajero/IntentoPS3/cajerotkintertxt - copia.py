
from os import path
import sys
import time
import os
import re
import fileinput
from datetime import datetime
from tkinter import *



def titulo():
    os.system("cls")
    print("\n\n")
    print("\t********************************************************************************************")
    print("\t*****                                                                                 ******")
    print("\t*****                              Cajero Banco de Chile                              ******")
    print("\t*****                                Cajero Automatico                                ******")
    print("\t*****                                                                                 ******")
    print("\t*****                         Jorge Labraña & Juan Pablo Grez                         ******")
    print("\t*****                                                                                 ******")
    print("\t*****                                                                                 ******")
    print("\t*****        Este programa mezcla metodos pack y place, no maximisar ventanas.        ******")
    print("\t********************************************************************************************")
    print("\n\n")



def definir_valores_cajero():
    opentxt = open("cajero.txt", "r")
    resultado = opentxt.read().split("-")
    opentxt.close()
    global datauser
    datauser = []
    global gaveta
    gaveta=int(resultado[0])
    global listasi
    listasi = resultado[2]
    global Lista_Imagenes
    Lista_Imagenes = []



def guardar_valores_cajero():
    listaescribir = [gaveta,sesion,listasi]
    escribir = '-'.join(str(i) for i in listaescribir)
    with open("/cajero.txt", "w") as output:
        output.write(str(escribir))



def definir_valores_usuario(cuenta):
    #leemos archivo
    strtxt = ".txt"
    nombretxt = str(cuenta) + str(strtxt)
    opentxt = open(nombretxt, "r")
    resultado = opentxt.read().split(",")
    opentxt.close()
    #definimos variables del usuario
    global usuario
    usuario = resultado[0]
    global nombreusuario
    nombreusuario = resultado[1]
    global pin
    pin = int(resultado[2])
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



def guardar_valores_usuario(cuenta):
    nombretxt =  str(cuenta) + ".txt"
    listaescribir = [usuario,nombreusuario,pin,intentos,bloqueado,admin,saldo,nombretipocta,tipocta,cobrogiro,cobrosaldo]
    escribir = ','.join(str(i) for i in listaescribir)
    with open(nombretxt, "w") as output:
        output.write(str(escribir))



def inicio():
    global sesion
    global inicio
    titulo()
    inicio = 0
    definir_valores_cajero()
    sesion=int(0)
    horafecha = datetime.now()
    horafechastr = horafecha.strftime("%d-%m-%Y %H:%M:%S")
    strregistro = "Fecha y Hora: " + str(horafechastr) + " Cajero iniciado.\n"
    with open("transacciones.txt", "a") as archivo:
        archivo.write(strregistro)
    menu_login()



def menu_login():
    global inicio
    global windowlogin
    global framelogin2
    global E1
    global E2
    if inicio==0:
        inicio = 1
        #creamos la ventana
        windowlogin = Tk()
        windowlogin.title("ATM BANCO DE CHILE")
        windowlogin.configure(bg="#151d2a")
        windowlogin.geometry("900x600")
        #main framelogin
        framelogin = LabelFrame(windowlogin,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
        framelogin.pack(fill=BOTH,expand=True,padx=150,pady=20)
        #dividimos en multiples framelogins
        framelogin0 = LabelFrame(framelogin,bg="#301fc9",relief=FLAT,bd=0)
        framelogin0.pack(expand=True)
        framelogin1 = LabelFrame(framelogin)
        framelogin1.pack(fill=X,expand=True)
        framelogin2 = LabelFrame(framelogin)
        framelogin2.pack(fill=X,expand=True)
        framelogin3 = LabelFrame(framelogin)
        framelogin3.pack(fill=BOTH,expand=True)
        framelogin4 = LabelFrame(framelogin)
        framelogin4.pack(fill=BOTH,expand=True)
        framelogin5 = LabelFrame(framelogin)
        framelogin5.pack(fill=BOTH,expand=True)
        framelogin6 = LabelFrame(framelogin)
        framelogin6.pack(fill=BOTH,expand=True)
        #empezamos a crear objetos
        canvaslogin = Canvas(framelogin0,width=400,height=200,bg="#301fc9",bd=0,relief=FLAT)      
        canvaslogin.pack(in_=framelogin0)
        imglogologin = PhotoImage(file="logo.png")
        Lista_Imagenes.append(imglogologin)
        canvaslogin.create_image(0,0, anchor=NW, image=imglogologin)
        loginboton1 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton1.place(x=2, y=50)
        loginboton2 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton2.place(x=755, y=50)
        loginboton3 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton3.place(x=2, y=160)
        loginboton4 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton4.place(x=755, y=160)
        loginboton5 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton5.place(x=2, y=270)
        loginboton6 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton6.place(x=755, y=270)
        loginboton7 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton7.place(x=2, y=380)
        loginboton8 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton8.place(x=755, y=380)
        loginboton9 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton9.place(x=2, y=490)
        loginboton0 = Button(windowlogin,bg="#8b93a6",padx=68,pady=25)
        loginboton0.place(x=755, y=490)
        L1=Label(framelogin1,text="Numero de Cuenta: ")
        L1.pack(in_=framelogin1,side=LEFT,fill=BOTH,expand=True)
        E1=Entry(framelogin1)
        E1.pack(in_=framelogin1,side=RIGHT,fill=BOTH,expand=True)
        E1.insert(0,"Ej: 12345678-9")
        L2=Label(framelogin2,text="PIN: ")
        L2.pack(in_=framelogin2,side=LEFT,fill=BOTH,expand=True)
        E2=Entry(framelogin2,show="*")
        E2.pack(in_=framelogin2,side=RIGHT,fill=BOTH,expand=True)
        E2.config(state="readonly")
        BP1=Button(framelogin3,text="1",command=lambda:numero_teclado(1))
        BP1.pack(in_=framelogin3,side=LEFT,fill=BOTH,expand=True)
        BP2=Button(framelogin3,text="2",command=lambda:numero_teclado(2))
        BP2.pack(in_=framelogin3,side=LEFT,fill=BOTH,expand=True)
        BP3=Button(framelogin3,text="3",command=lambda:numero_teclado(3))
        BP3.pack(in_=framelogin3,side=LEFT,fill=BOTH,expand=True)
        BP4=Button(framelogin4,text="4",command=lambda:numero_teclado(4))
        BP4.pack(in_=framelogin4,side=LEFT,fill=BOTH,expand=True)
        BP5=Button(framelogin4,text="5",command=lambda:numero_teclado(5))
        BP5.pack(in_=framelogin4,side=LEFT,fill=BOTH,expand=True)
        BP6=Button(framelogin4,text="6",command=lambda:numero_teclado(6))
        BP6.pack(in_=framelogin4,side=LEFT,fill=BOTH,expand=True)
        BP7=Button(framelogin5,text="7",command=lambda:numero_teclado(7))
        BP7.pack(in_=framelogin5,side=LEFT,fill=BOTH,expand=True)
        BP8=Button(framelogin5,text="8",command=lambda:numero_teclado(8))
        BP8.pack(in_=framelogin5,side=LEFT,fill=BOTH,expand=True)
        BP9=Button(framelogin5,text="9",command=lambda:numero_teclado(9))
        BP9.pack(in_=framelogin5,side=LEFT,fill=BOTH,expand=True)
        BP0=Button(framelogin6,text="0",command=lambda:numero_teclado(0))
        BP0.pack(in_=framelogin6,side=LEFT,fill=BOTH,expand=True)
        BPI=Button(framelogin6, text="Ingresar",command=verificar_pin)
        BPI.pack(in_=framelogin6,side=RIGHT,fill=BOTH,expand=True)
        BPB=Button(framelogin6, text="Borrar",command=lambda:numero_teclado("borrar"))
        BPB.pack(in_=framelogin6,side=LEFT,fill=BOTH,expand=True)
        #iniciamos la ventana
        windowlogin.mainloop()
    else:
        numero_teclado("borrar")
        windowlogin.deiconify()



def numero_teclado(tecla):
    #verificamos si es numero o borrar
    if tecla!="borrar":
        #ingresamos un numero
        E2.config(state="normal")
        E2.insert(END,tecla)
        E2.config(state="readonly")
    else:
        #borramos
        E2.config(state="normal")
        E2.delete(0,END)
        E2.config(state="readonly")



def verificar_pin():
    global nrocta
    global sesion
    if E1.get():
        if E2.get():
            #recibimos el pin como string y lo convertimos a integro
            pintrystr= E2.get()
            pintry=int(pintrystr)
            usuariotry= E1.get()
            nrocta = usuariotry
            file = str(nrocta) + ".txt"
            #verificamos que el usuario sea correcto
            if (path.exists(file)):
                definir_valores_usuario(nrocta)
                #verificamos pin
                if (pintry==pin):
                    #si es correcto, enviamos a menu principal
                    sesion=int(1)
                    horafecha = datetime.now()
                    horafechastr = horafecha.strftime("%d-%m-%Y %H:%M:%S")
                    strregistro = "Fecha y Hora: " + str(horafechastr) + " Inicio de sesion de." + str(nrocta) + "\n"
                    with open("transacciones.txt", "a") as archivo:
                        archivo.write(strregistro)
                    menu_principal()
                else:
                    #si es incorrecto, enviamos error
                    numero_teclado("borrar")
                    ventana_error("pin")
                    horafecha = datetime.now()
                    horafechastr = horafecha.strftime("%d-%m-%Y %H:%M:%S")
                    strregistro = "Fecha y Hora: " + str(horafechastr) + " PIN Incorrecto de " + str(nrocta) + "\n"
                    with open("transacciones.txt", "a") as archivo:
                        archivo.write(strregistro)
            else: 
                ventana_error("usuario")
                horafecha = datetime.now()
                horafechastr = horafecha.strftime("%d-%m-%Y %H:%M:%S")
                strregistro = "Fecha y Hora: " + str(horafechastr) + " Intento de Inicio de sesion cuenta: " + str(nrocta) + "\n"
                with open("transacciones.txt", "a") as archivo:
                    archivo.write(strregistro)
        else:
            ventana_error("data")
            horafecha = datetime.now()
            horafechastr = horafecha.strftime("%d-%m-%Y %H:%M:%S")
            strregistro = "Fecha y Hora: " + str(horafechastr) + " Intento de Inicio de sesion cuenta: " + str(
                nrocta) + "\n"
            with open("transacciones.txt", "a") as archivo:
                archivo.write(strregistro)
    else: 
        ventana_error("data")
        horafecha = datetime.now()
        horafechastr = horafecha.strftime("%d-%m-%Y %H:%M:%S")
        strregistro = "Fecha y Hora: " + str(horafechastr) + " Intento de Inicio de sesion cuenta: " + str(
            nrocta) + "\n"
        with open("transacciones.txt", "a") as archivo:
            archivo.write(strregistro)



def log_out():
    global sesion
    guardar_valores_cajero()
    guardar_valores_usuario(nrocta)
    sesion=int(0)
    menu_login()



def menu_principal():
    global windowlogin
    global windowmenu
    #reducimos ventana login
    windowlogin.withdraw()
    #creamos ventana menu
    windowmenu=Toplevel()
    windowmenu.title("ATM BANCO DE CHILE")
    windowmenu.configure(bg="#151d2a")
    windowmenu.geometry("900x600")
    #main framemenu
    framemenu= LabelFrame(windowmenu,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    framemenu.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples framemenu
    framemenu0 = LabelFrame(framemenu,bg="#301fc9",relief=FLAT,bd=0)
    framemenu0.pack(expand=True)
    framemenu1 = LabelFrame(framemenu,bg="#301fc9",relief=FLAT,bd=0)
    framemenu1.pack(fill=BOTH,expand=True)
    framemenu2 = LabelFrame(framemenu,bg="#301fc9",relief=FLAT,bd=0)
    framemenu2.pack(fill=BOTH,expand=True)
    framemenu3 = LabelFrame(framemenu,bg="#301fc9",relief=FLAT,bd=0)
    framemenu3.pack(fill=BOTH,expand=True)
    framemenu4 = LabelFrame(framemenu,bg="#301fc9",relief=FLAT,bd=0)
    framemenu4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    menuboton1 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_giro(10000))
    menuboton1.place(x=2, y=50)
    menuboton2 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=menu_saldo)
    menuboton2.place(x=755, y=50)
    menuboton3 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_giro(20000))
    menuboton3.place(x=2, y=160)
    menuboton4 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=menu_deposito)
    menuboton4.place(x=755, y=160)
    menuboton5 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_giro(50000))
    menuboton5.place(x=2, y=270)
    menuboton6 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=menu_clave)
    menuboton6.place(x=755, y=270)
    menuboton7 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_giro(100000))
    menuboton7.place(x=2, y=380)
    if admin==1:
        menuboton8 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=menu_admin)
        menuboton8.place(x=755, y=380)
    else:
        menuboton8 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25)
        menuboton8.place(x=755, y=380)
    menuboton9 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_giro(0))
    menuboton9.place(x=2, y=490)
    menuboton0 = Button(windowmenu,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowmenu))
    menuboton0.place(x=755, y=490)
    ML1=Label(framemenu0, text="<--Giro Rapido por $10.000",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=W)
    ML1.pack(in_=framemenu0,side=LEFT,fill=BOTH,expand=True)
    ML2=Label(framemenu0, text="Consulta de Saldo-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
    ML2.pack(in_=framemenu0,side=RIGHT,fill=BOTH,expand=True)
    ML3=Label(framemenu1, text="<--Giro Rapido por $20.000",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=W)
    ML3.pack(in_=framemenu1,side=LEFT,fill=BOTH,expand=True)
    ML4=Label(framemenu1, text="Deposito a Cuenta-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
    ML4.pack(in_=framemenu1,side=RIGHT,fill=BOTH,expand=True)
    ML5=Label(framemenu2, text="<--Giro Rapido por $50.000",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=W)
    ML5.pack(in_=framemenu2,side=LEFT,fill=BOTH,expand=True)
    ML6=Label(framemenu2, text="Cambio de Clave-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
    ML6.pack(in_=framemenu2,side=RIGHT,fill=BOTH,expand=True)
    ML7=Label(framemenu3, text="<--Giro Rapido por $100.000",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=25,anchor=W)
    ML7.pack(in_=framemenu3,side=LEFT,fill=BOTH,expand=True)
    if admin==1:
        ML8=Label(framemenu3, text="Menu Administrativo-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
        ML8.pack(in_=framemenu3,side=RIGHT,fill=BOTH,expand=True)
    else:
        ML8=Label(framemenu3, text="",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
        ML8.pack(in_=framemenu3,side=RIGHT,fill=BOTH,expand=True)
    ML9=Label(framemenu4, text="<--Giro por Otro Monto",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=W)
    ML9.pack(in_=framemenu4,side=LEFT,fill=BOTH,expand=True)
    ML0=Label(framemenu4, text="Salir-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
    ML0.pack(in_=framemenu4,side=RIGHT,fill=BOTH,expand=True)



def menu_giro(cgiro):
    global windowmenu
    global windowgiro
    global ME1
    #reducimos ventana login
    windowmenu.withdraw()
    #creamos ventana giro
    windowgiro=Toplevel()
    windowgiro.title("ATM BANCO DE CHILE")
    windowgiro.configure(bg="#151d2a")
    windowgiro.geometry("900x600")
    #main framegiro
    framegiro= LabelFrame(windowgiro,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    framegiro.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples framegiro
    framegiro0 = LabelFrame(framegiro,bg="#301fc9",relief=FLAT,bd=0)
    framegiro0.pack(expand=True)
    framegiro1 = LabelFrame(framegiro,bg="#301fc9",relief=FLAT,bd=0)
    framegiro1.pack(fill=BOTH,expand=True)
    framegiro2 = LabelFrame(framegiro,bg="#301fc9",relief=FLAT,bd=0)
    framegiro2.pack(fill=BOTH,expand=True)
    framegiro3 = LabelFrame(framegiro,bg="#301fc9",relief=FLAT,bd=0)
    framegiro3.pack(fill=BOTH,expand=True)
    framegiro4 = LabelFrame(framegiro,bg="#301fc9",relief=FLAT,bd=0)
    framegiro4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    giroboton1 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25)
    giroboton1.place(x=2, y=50)
    giroboton2 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25)
    giroboton2.place(x=755, y=50)
    giroboton3 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25)
    giroboton3.place(x=2, y=160)
    giroboton4 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25)
    giroboton4.place(x=755, y=160)
    giroboton5 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25)
    giroboton5.place(x=2, y=270)
    giroboton6 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25)
    giroboton6.place(x=755, y=270)
    giroboton7 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25)
    giroboton7.place(x=2, y=380)
    giroboton9 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25)
    giroboton9.place(x=2, y=490)
    if cgiro!=0:
        strgiro="Estamos realizando un giro por: $"
        strcantidad=str(f"{cgiro:,}")
        strclp=" CLP."
        strtext = strgiro+strcantidad+strclp
        ML1=Label(framegiro0, text=strtext,fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framegiro0,fill=BOTH,expand=True)
        str1="Esta operacion tiene un costo de: $"
        str2=str(cobrogiro)+" CLP."
        strtext2=str1+str2
        ML2=Label(framegiro1, text=strtext2,fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegiro1,fill=BOTH,expand=True)
        ML2=Label(framegiro2, text="Desea realizar esta operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegiro2,fill=BOTH,expand=True)
        ML2=Label(framegiro3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegiro3,fill=BOTH,expand=True)
        ML2=Label(framegiro4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegiro4,fill=BOTH,expand=True)
        giroboton8 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_verifica_giro(cgiro))
        giroboton8.place(x=755, y=380)
        giroboton0 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowgiro))
        giroboton0.place(x=755, y=490)
    else:
        ML1=Label(framegiro0, text="Ingresa el monto a girar:",fg="#f2f5f7",font=("Verdana", 8),bg="#301fc9")
        ML1.pack(in_=framegiro0,side=TOP,fill=BOTH,expand=True)
        ME1=Entry(framegiro0)
        ME1.pack(in_=framegiro0,side=BOTTOM,fill=BOTH,expand=True)
        str1="Esta operacion tiene un costo de: $"
        str2=str(cobrogiro)+" CLP."
        strtext2=str1+str2
        ML2=Label(framegiro1, text=strtext2,fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegiro1,fill=BOTH,expand=True)
        ML2=Label(framegiro2, text="Desea realizar esta operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegiro2,fill=BOTH,expand=True)
        ML2=Label(framegiro3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegiro3,fill=BOTH,expand=True)
        ML2=Label(framegiro4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegiro4,fill=BOTH,expand=True)
        giroboton8 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_verifica_giro(0))
        giroboton8.place(x=755, y=380)
        giroboton0 = Button(windowgiro,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowgiro))
        giroboton0.place(x=755, y=490)



def menu_verifica_giro(cgiro):
    global saldo
    global gaveta
    #verificamos que este definido el giro
    if cgiro!=0:
        #calculamos total a descontar
        giro = cgiro + cobrogiro
        #verifica si gaveta tiene fondos
        if giro<=gaveta:
            #verifica si total a descontar es menor a saldo
            if giro<=saldo:
                #realizamos giro
                saldo = saldo-giro
                gaveta = gaveta - cgiro
                guardar_valores_cajero()
                guardar_valores_usuario(nrocta)
                menu_giro_realizado(cgiro)
            else:
                menu_giro_realizado(0)
        else:
            menu_giro_realizado(-1)
    else:
        strgetgiro = ME1.get()
        if (strgetgiro.isdigit()):
            getgiro=int(strgetgiro)
            #calculamos total a descontar
            giro = getgiro + cobrogiro
            #verifica si gaveta tiene fondos
            if giro<=gaveta:
                #verifica si total a descontar es menor a saldo
                if giro<=saldo:
                    #realizamos giro
                    saldo = saldo-giro
                    gaveta = gaveta + cgiro
                    guardar_valores_cajero()
                    guardar_valores_usuario(nrocta)
                    menu_giro_realizado(getgiro)
                else:
                    menu_giro_realizado(0)
            else:
                menu_giro_realizado(-1)
        else:
            menu_giro_realizado(-2)



def menu_giro_realizado(cgiro):
    global windowgiro
    global windowgirorealizado
    #reducimos ventana login
    windowgiro.withdraw()
    #creamos ventana girorealizado
    windowgirorealizado=Toplevel()
    windowgirorealizado.title("ATM BANCO DE CHILE")
    windowgirorealizado.configure(bg="#151d2a")
    windowgirorealizado.geometry("900x600")
    #main framegirorealizado
    framegirorealizado= LabelFrame(windowgirorealizado,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    framegirorealizado.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples framegirorealizado
    framegirorealizado0 = LabelFrame(framegirorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framegirorealizado0.pack(expand=True)
    framegirorealizado1 = LabelFrame(framegirorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framegirorealizado1.pack(fill=BOTH,expand=True)
    framegirorealizado2 = LabelFrame(framegirorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framegirorealizado2.pack(fill=BOTH,expand=True)
    framegirorealizado3 = LabelFrame(framegirorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framegirorealizado3.pack(fill=BOTH,expand=True)
    framegirorealizado4 = LabelFrame(framegirorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framegirorealizado4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    girorealizadoboton1 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25)
    girorealizadoboton1.place(x=2, y=50)
    girorealizadoboton2 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25)
    girorealizadoboton2.place(x=755, y=50)
    girorealizadoboton3 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25)
    girorealizadoboton3.place(x=2, y=160)
    girorealizadoboton4 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25)
    girorealizadoboton4.place(x=755, y=160)
    girorealizadoboton5 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25)
    girorealizadoboton5.place(x=2, y=270)
    girorealizadoboton6 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25)
    girorealizadoboton6.place(x=755, y=270)
    girorealizadoboton7 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25)
    girorealizadoboton7.place(x=2, y=380)
    girorealizadoboton9 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25)
    girorealizadoboton9.place(x=2, y=490)
    if cgiro > 0:
        strgiro="Realizamos un giro por: $"
        strcantidad=str(f"{cgiro:,}")
        strclp=" CLP."
        strtext = strgiro+strcantidad+strclp
        ML1=Label(framegirorealizado0, text=strtext,fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framegirorealizado0,fill=BOTH,expand=True)
        str1="Tu nuevo saldo es: "
        strcantidad2=str(f"{saldo:,}")
        str2=strcantidad2+" CLP."
        strtext2=str1+str2
        horafecha = datetime.now()
        horafechastr = horafecha.strftime("%d-%m-%Y %H:%M:%S")
        strregistro = "Fecha y Hora: " + str(horafechastr) + " Giro realizado: " + str(
            nrocta) + " Cantidad: " + strcantidad + "\n"
        with open("transacciones.txt", "a") as archivo:
            archivo.write(strregistro)
        ML2=Label(framegirorealizado1, text=strtext2,fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado1,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado2, text="Desea otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado2,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado3,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado4,fill=BOTH,expand=True)
        giroboton8 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowgirorealizado))
        giroboton8.place(x=755, y=380)
        giroboton0 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowgirorealizado))
        giroboton0.place(x=755, y=490)
    elif cgiro==0:
        ML1=Label(framegirorealizado0, text="No se ha realizado el giro.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framegirorealizado0,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado1, text="Saldo insuficiente.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado1,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado2, text="Desea otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado2,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado3,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado4,fill=BOTH,expand=True)
        giroboton8 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowgirorealizado))
        giroboton8.place(x=755, y=380)
        giroboton0 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowgirorealizado))
        giroboton0.place(x=755, y=490)
    elif cgiro==-1:
        ML1=Label(framegirorealizado0, text="No se ha realizado el giro.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framegirorealizado0,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado1, text="Este cajero no puede realizar esta operacion.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado1,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado2, text="Desea otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado2,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado3,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado4,fill=BOTH,expand=True)
        giroboton8 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowgirorealizado))
        giroboton8.place(x=755, y=380)
        giroboton0 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowgirorealizado))
        giroboton0.place(x=755, y=490)
    elif cgiro==-2:
        ML1=Label(framegirorealizado0, text="No se ha realizado el giro.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framegirorealizado0,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado1, text="El monto ingresado es invalido.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado1,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado2, text="Desea otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado2,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado3,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado4,fill=BOTH,expand=True)
        giroboton8 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowgirorealizado))
        giroboton8.place(x=755, y=380)
        giroboton0 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowgirorealizado))
        giroboton0.place(x=755, y=490)
    else:
        ML1=Label(framegirorealizado0, text="No se ha realizado el giro.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framegirorealizado0,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado1, text="Error desconocido.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado1,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado2, text="Desea otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framegirorealizado2,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado3,fill=BOTH,expand=True)
        ML2=Label(framegirorealizado4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framegirorealizado4,fill=BOTH,expand=True)
        giroboton8 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowgirorealizado))
        giroboton8.place(x=755, y=380)
        giroboton0 = Button(windowgirorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowgirorealizado))
        giroboton0.place(x=755, y=490)



def menu_saldo():
    global windowmenu
    global windowsaldo
    global ME1
    #reducimos ventana login
    windowmenu.withdraw()
    #creamos ventana saldo
    windowsaldo=Toplevel()
    windowsaldo.title("ATM BANCO DE CHILE")
    windowsaldo.configure(bg="#151d2a")
    windowsaldo.geometry("900x600")
    #main framesaldo
    framesaldo= LabelFrame(windowsaldo,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    framesaldo.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples framesaldo
    framesaldo0 = LabelFrame(framesaldo,bg="#301fc9",relief=FLAT,bd=0)
    framesaldo0.pack(expand=True)
    framesaldo1 = LabelFrame(framesaldo,bg="#301fc9",relief=FLAT,bd=0)
    framesaldo1.pack(fill=BOTH,expand=True)
    framesaldo2 = LabelFrame(framesaldo,bg="#301fc9",relief=FLAT,bd=0)
    framesaldo2.pack(fill=BOTH,expand=True)
    framesaldo3 = LabelFrame(framesaldo,bg="#301fc9",relief=FLAT,bd=0)
    framesaldo3.pack(fill=BOTH,expand=True)
    framesaldo4 = LabelFrame(framesaldo,bg="#301fc9",relief=FLAT,bd=0)
    framesaldo4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    saldoboton1 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25)
    saldoboton1.place(x=2, y=50)
    saldoboton2 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25)
    saldoboton2.place(x=755, y=50)
    saldoboton3 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25)
    saldoboton3.place(x=2, y=160)
    saldoboton4 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25)
    saldoboton4.place(x=755, y=160)
    saldoboton5 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25)
    saldoboton5.place(x=2, y=270)
    saldoboton6 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25)
    saldoboton6.place(x=755, y=270)
    saldoboton7 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25)
    saldoboton7.place(x=2, y=380)
    saldoboton9 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25)
    saldoboton9.place(x=2, y=490)
    ML1=Label(framesaldo0, text="Consulta de saldo",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML1.pack(in_=framesaldo0,fill=BOTH,expand=True)
    csaldo = cobrosaldo
    str1="Esta operacion tiene un costo de: $"
    str2=str(cobrosaldo)+" CLP."
    strtext2=str1+str2
    ML2=Label(framesaldo1, text=strtext2,fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML2.pack(in_=framesaldo1,fill=BOTH,expand=True)
    ML2=Label(framesaldo2, text="Desea realizar esta operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML2.pack(in_=framesaldo2,fill=BOTH,expand=True)
    ML2=Label(framesaldo3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
    ML2.pack(in_=framesaldo3,fill=BOTH,expand=True)
    ML2=Label(framesaldo4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
    ML2.pack(in_=framesaldo4,fill=BOTH,expand=True)
    saldoboton8 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_verifica_saldo(csaldo))
    saldoboton8.place(x=755, y=380)
    saldoboton0 = Button(windowsaldo,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowsaldo))
    saldoboton0.place(x=755, y=490)

def menu_verifica_saldo(csaldo):
    global saldo
    global windowsaldo
    global windowsaldorealizado
    #reducimos ventana login
    windowsaldo.withdraw()
    #creamos ventana saldorealizado
    windowsaldorealizado=Toplevel()
    windowsaldorealizado.title("ATM BANCO DE CHILE")
    windowsaldorealizado.configure(bg="#151d2a")
    windowsaldorealizado.geometry("900x600")
    #main framesaldorealizado
    framesaldorealizado= LabelFrame(windowsaldorealizado,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    framesaldorealizado.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples framesaldorealizado
    framesaldorealizado0 = LabelFrame(framesaldorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framesaldorealizado0.pack(expand=True)
    framesaldorealizado1 = LabelFrame(framesaldorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framesaldorealizado1.pack(fill=BOTH,expand=True)
    framesaldorealizado2 = LabelFrame(framesaldorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framesaldorealizado2.pack(fill=BOTH,expand=True)
    framesaldorealizado3 = LabelFrame(framesaldorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framesaldorealizado3.pack(fill=BOTH,expand=True)
    framesaldorealizado4 = LabelFrame(framesaldorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framesaldorealizado4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    saldorealizadoboton1 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25)
    saldorealizadoboton1.place(x=2, y=50)
    saldorealizadoboton2 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25)
    saldorealizadoboton2.place(x=755, y=50)
    saldorealizadoboton3 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25)
    saldorealizadoboton3.place(x=2, y=160)
    saldorealizadoboton4 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25)
    saldorealizadoboton4.place(x=755, y=160)
    saldorealizadoboton5 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25)
    saldorealizadoboton5.place(x=2, y=270)
    saldorealizadoboton6 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25)
    saldorealizadoboton6.place(x=755, y=270)
    saldorealizadoboton7 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25)
    saldorealizadoboton7.place(x=2, y=380)
    saldorealizadoboton9 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25)
    saldorealizadoboton9.place(x=2, y=490)
    if saldo >= csaldo:
        saldo = saldo - csaldo
        guardar_valores_cajero()
        guardar_valores_usuario(nrocta)
        ML1=Label(framesaldorealizado0, text="Consulta de saldo",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framesaldorealizado0,fill=BOTH,expand=True)
        str1="Tu saldo actual es:"
        strcantidad=str(f"{saldo:,}")
        str2=str(strcantidad)+" CLP."
        strtext2=str1+str2
        horafecha = datetime.now()
        horafechastr = horafecha.strftime("%d-%m-%Y %H:%M:%S")
        strregistro = "Fecha y Hora: " + str(horafechastr) + " Consulta de Saldo: " + str(
            nrocta) + "\n"
        with open("transacciones.txt", "a") as archivo:
            archivo.write(strregistro)
        ML2=Label(framesaldorealizado1, text=strtext2,fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framesaldorealizado1,fill=BOTH,expand=True)
        ML2=Label(framesaldorealizado2, text="Desea realizar otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framesaldorealizado2,fill=BOTH,expand=True)
        ML2=Label(framesaldorealizado3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framesaldorealizado3,fill=BOTH,expand=True)
        ML2=Label(framesaldorealizado4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framesaldorealizado4,fill=BOTH,expand=True)
        saldoboton8 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowsaldorealizado))
        saldoboton8.place(x=755, y=380)
        saldoboton0 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowsaldorealizado))
        saldoboton0.place(x=755, y=490)
    else:
        ML1=Label(framesaldorealizado0, text="Consulta de saldo",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framesaldorealizado0,fill=BOTH,expand=True)
        ML2=Label(framesaldorealizado1, text="Saldo insuficiente para realizar esta operacion",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framesaldorealizado1,fill=BOTH,expand=True)
        ML2=Label(framesaldorealizado2, text="Desea realizar otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framesaldorealizado2,fill=BOTH,expand=True)
        ML2=Label(framesaldorealizado3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framesaldorealizado3,fill=BOTH,expand=True)
        ML2=Label(framesaldorealizado4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framesaldorealizado4,fill=BOTH,expand=True)
        saldoboton8 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowsaldorealizado))
        saldoboton8.place(x=755, y=380)
        saldoboton0 = Button(windowsaldorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowsaldorealizado))
        saldoboton0.place(x=755, y=490)




def menu_deposito():
    global windowmenu
    global windowdeposito
    global ED1
    global ED2
    #reducimos ventana menu
    windowmenu.withdraw()
    #creamos ventana deposito
    windowdeposito=Toplevel()
    windowdeposito.title("ATM BANCO DE CHILE")
    windowdeposito.configure(bg="#151d2a")
    windowdeposito.geometry("900x600")
    #main framedeposito
    framedeposito= LabelFrame(windowdeposito,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    framedeposito.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples framedeposito
    framedeposito0 = LabelFrame(framedeposito,bg="#301fc9",relief=FLAT,bd=0)
    framedeposito0.pack(expand=True)
    framedeposito1 = LabelFrame(framedeposito,bg="#301fc9",relief=FLAT,bd=0)
    framedeposito1.pack(fill=BOTH,expand=True)
    framedeposito2 = LabelFrame(framedeposito,bg="#301fc9",relief=FLAT,bd=0)
    framedeposito2.pack(fill=BOTH,expand=True)
    framedeposito3 = LabelFrame(framedeposito,bg="#301fc9",relief=FLAT,bd=0)
    framedeposito3.pack(fill=BOTH,expand=True)
    framedeposito4 = LabelFrame(framedeposito,bg="#301fc9",relief=FLAT,bd=0)
    framedeposito4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    depositoboton1 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25)
    depositoboton1.place(x=2, y=50)
    depositoboton2 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25)
    depositoboton2.place(x=755, y=50)
    depositoboton3 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25)
    depositoboton3.place(x=2, y=160)
    depositoboton4 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25)
    depositoboton4.place(x=755, y=160)
    depositoboton5 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25)
    depositoboton5.place(x=2, y=270)
    depositoboton6 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25)
    depositoboton6.place(x=755, y=270)
    depositoboton7 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25)
    depositoboton7.place(x=2, y=380)
    depositoboton9 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25)
    depositoboton9.place(x=2, y=490)
    ML1=Label(framedeposito0, text="Deposito a Cuenta",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML1.pack(in_=framedeposito0,fill=BOTH,expand=True)
    framedeposito11 = LabelFrame(framedeposito1,bg="#301fc9",relief=FLAT,bd=0)
    framedeposito11.pack(fill=BOTH,expand=True)
    framedeposito12 = LabelFrame(framedeposito1,bg="#301fc9",relief=FLAT,bd=0)
    framedeposito12.pack(fill=BOTH,expand=True)
    L1=Label(framedeposito11,text="Numero de Cuenta: ")
    L1.pack(in_=framedeposito11,side=LEFT,fill=BOTH,expand=True)
    ED1=Entry(framedeposito11)
    ED1.pack(in_=framedeposito11,side=RIGHT,fill=BOTH,expand=True)
    ED1.insert(0,"Ej: 12345678-9")
    L2=Label(framedeposito12,text="Monto: ")
    L2.pack(in_=framedeposito12,side=LEFT,fill=BOTH,expand=True)
    ED2=Entry(framedeposito12)
    ED2.pack(in_=framedeposito12,side=RIGHT,fill=BOTH,expand=True)
    ED2.insert(0,"Ej: 123000")
    ML2=Label(framedeposito2, text="Desea realizar esta operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML2.pack(in_=framedeposito2,fill=BOTH,expand=True)
    ML2=Label(framedeposito3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
    ML2.pack(in_=framedeposito3,fill=BOTH,expand=True)
    ML2=Label(framedeposito4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
    ML2.pack(in_=framedeposito4,fill=BOTH,expand=True)
    depositoboton8 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_deposito_confirmar())
    depositoboton8.place(x=755, y=380)
    depositoboton0 = Button(windowdeposito,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowdeposito))
    depositoboton0.place(x=755, y=490)



def menu_deposito_confirmar():
    global windowdeposito
    global windowdepositoconfirmar
    #reducimos ventana login
    windowdeposito.withdraw()
    #creamos ventana depositoconfirmar
    windowdepositoconfirmar=Toplevel()
    windowdepositoconfirmar.title("ATM BANCO DE CHILE")
    windowdepositoconfirmar.configure(bg="#151d2a")
    windowdepositoconfirmar.geometry("900x600")
    #main framedepositoconfirmar
    framedepositoconfirmar= LabelFrame(windowdepositoconfirmar,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    framedepositoconfirmar.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples framedepositoconfirmar
    framedepositoconfirmar0 = LabelFrame(framedepositoconfirmar,bg="#301fc9",relief=FLAT,bd=0)
    framedepositoconfirmar0.pack(expand=True)
    framedepositoconfirmar1 = LabelFrame(framedepositoconfirmar,bg="#301fc9",relief=FLAT,bd=0)
    framedepositoconfirmar1.pack(fill=BOTH,expand=True)
    framedepositoconfirmar2 = LabelFrame(framedepositoconfirmar,bg="#301fc9",relief=FLAT,bd=0)
    framedepositoconfirmar2.pack(fill=BOTH,expand=True)
    framedepositoconfirmar3 = LabelFrame(framedepositoconfirmar,bg="#301fc9",relief=FLAT,bd=0)
    framedepositoconfirmar3.pack(fill=BOTH,expand=True)
    framedepositoconfirmar4 = LabelFrame(framedepositoconfirmar,bg="#301fc9",relief=FLAT,bd=0)
    framedepositoconfirmar4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    depositoconfirmarboton1 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25)
    depositoconfirmarboton1.place(x=2, y=50)
    depositoconfirmarboton2 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25)
    depositoconfirmarboton2.place(x=755, y=50)
    depositoconfirmarboton3 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25)
    depositoconfirmarboton3.place(x=2, y=160)
    depositoconfirmarboton4 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25)
    depositoconfirmarboton4.place(x=755, y=160)
    depositoconfirmarboton5 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25)
    depositoconfirmarboton5.place(x=2, y=270)
    depositoconfirmarboton6 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25)
    depositoconfirmarboton6.place(x=755, y=270)
    depositoconfirmarboton7 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25)
    depositoconfirmarboton7.place(x=2, y=380)
    depositoconfirmarboton9 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25)
    depositoconfirmarboton9.place(x=2, y=490)
    montostr=ED2.get()
    if(montostr.isdigit()):
        cuenta=str(ED1.get())
        monto=int(ED2.get())
        print("1")
        ML1=Label(framedepositoconfirmar0, text="Deposito",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framedepositoconfirmar0,fill=BOTH,expand=True)
        strmonto=str(f"{monto:,}")
        str1="Estas haciendo un deposito de " + str(strmonto) + " CLP a la cuenta numero " + str(cuenta) + "."
        ML2=Label(framedepositoconfirmar1, text=str1,fg="#f2f5f7",font=("Verdana", 9),bg="#301fc9")
        ML2.pack(in_=framedepositoconfirmar1,fill=BOTH,expand=True)
        ML2=Label(framedepositoconfirmar2, text="Desea realizar esta operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framedepositoconfirmar2,fill=BOTH,expand=True)
        ML2=Label(framedepositoconfirmar3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framedepositoconfirmar3,fill=BOTH,expand=True)
        ML2=Label(framedepositoconfirmar4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framedepositoconfirmar4,fill=BOTH,expand=True)
        depositoconfirmarboton8 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_deposito_realizado(cuenta,monto))
        depositoconfirmarboton8.place(x=755, y=380)
        depositoconfirmarboton0 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowdepositoconfirmar))
        depositoconfirmarboton0.place(x=755, y=490)
    else:
        print("2")
        ML1=Label(framedepositoconfirmar0, text="Deposito",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framedepositoconfirmar0,fill=BOTH,expand=True)
        ML2=Label(framedepositoconfirmar1, text="Monto invalido.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framedepositoconfirmar1,fill=BOTH,expand=True)
        ML2=Label(framedepositoconfirmar2, text="Desea otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framedepositoconfirmar2,fill=BOTH,expand=True)
        ML2=Label(framedepositoconfirmar3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framedepositoconfirmar3,fill=BOTH,expand=True)
        ML2=Label(framedepositoconfirmar4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framedepositoconfirmar4,fill=BOTH,expand=True)
        depositoconfirmarboton8 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowdepositoconfirmar))
        depositoconfirmarboton8.place(x=755, y=380)
        depositoconfirmarboton0 = Button(windowdepositoconfirmar,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowdepositoconfirmar))
        depositoconfirmarboton0.place(x=755, y=490)



def menu_deposito_realizado(cuenta,monto):
    global windowdepositoconfirmar
    global windowdepositorealizado
    #reducimos ventana login
    windowdepositoconfirmar.withdraw()
    #creamos ventana depositorealizado
    windowdepositorealizado=Toplevel()
    windowdepositorealizado.title("ATM BANCO DE CHILE")
    windowdepositorealizado.configure(bg="#151d2a")
    windowdepositorealizado.geometry("900x600")
    #main framedepositorealizado
    framedepositorealizado= LabelFrame(windowdepositorealizado,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    framedepositorealizado.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples framedepositorealizado
    framedepositorealizado0 = LabelFrame(framedepositorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framedepositorealizado0.pack(expand=True)
    framedepositorealizado1 = LabelFrame(framedepositorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framedepositorealizado1.pack(fill=BOTH,expand=True)
    framedepositorealizado2 = LabelFrame(framedepositorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framedepositorealizado2.pack(fill=BOTH,expand=True)
    framedepositorealizado3 = LabelFrame(framedepositorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framedepositorealizado3.pack(fill=BOTH,expand=True)
    framedepositorealizado4 = LabelFrame(framedepositorealizado,bg="#301fc9",relief=FLAT,bd=0)
    framedepositorealizado4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    depositorealizadoboton1 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25)
    depositorealizadoboton1.place(x=2, y=50)
    depositorealizadoboton2 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25)
    depositorealizadoboton2.place(x=755, y=50)
    depositorealizadoboton3 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25)
    depositorealizadoboton3.place(x=2, y=160)
    depositorealizadoboton4 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25)
    depositorealizadoboton4.place(x=755, y=160)
    depositorealizadoboton5 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25)
    depositorealizadoboton5.place(x=2, y=270)
    depositorealizadoboton6 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25)
    depositorealizadoboton6.place(x=755, y=270)
    depositorealizadoboton7 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25)
    depositorealizadoboton7.place(x=2, y=380)
    depositorealizadoboton9 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25)
    depositorealizadoboton9.place(x=2, y=490)
    filedeposito = str(cuenta) + ".txt"
    #verificamos que usuario existe
    if(path.exists(filedeposito)):
        #si edita cuenta propia, guardamos valores en txt
        if cuenta==nrocta:
            guardar_valores_usuario(nrocta)
        #abrimos txt y cargamos valores
        opentxtdeposito = open(filedeposito, "r")
        resultadodeposito = opentxtdeposito.read().split(",")
        opentxtdeposito.close()
        usuariodeposito = resultadodeposito[0]
        nombreusuariodeposito = resultadodeposito[1]
        pindeposito = int(resultadodeposito[2])
        intentosdeposito= int(resultadodeposito[3])
        bloqueadodeposito= int(resultadodeposito[4])
        admindeposito = int(resultadodeposito[5])
        saldodeposito = int(resultadodeposito[6])
        nombretipoctadeposito = resultadodeposito[7]
        tipoctadeposito = resultadodeposito[8]
        cobrogirodeposito = int(resultadodeposito[9])
        cobrosaldodeposito = int(resultadodeposito[10])
        #aumentamos el saldo
        saldodeposito=saldodeposito+int(monto)
        listaescribirdeposito = [usuariodeposito,nombreusuariodeposito,pindeposito,intentosdeposito,bloqueadodeposito,admindeposito,saldodeposito,nombretipoctadeposito,tipoctadeposito,cobrogirodeposito,cobrosaldodeposito]
        escribirdeposito = ','.join(str(i) for i in listaescribirdeposito)
        with open(filedeposito, "w") as output:
            output.write(str(escribirdeposito))
        #si edita cuenta propia, recargamos valores desde txt
        if cuenta==nrocta:
            definir_valores_usuario(nrocta)
        ML1=Label(framedepositorealizado0, text="Deposito",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framedepositorealizado0,fill=BOTH,expand=True)
        strmonto=str(f"{monto:,}")
        str1="Has realizado un deposito de " + str(strmonto) + " CLP a la cuenta numero " + str(cuenta) + "."
        horafecha = datetime.now()
        horafechastr = horafecha.strftime("%d-%m-%Y %H:%M:%S")
        strregistro = "Fecha y Hora: " + str(horafechastr) + " Giro realizado: " + str(
            cuenta) + " Cantidad: " + strmonto + "\n"
        with open("transacciones.txt", "a") as archivo:
            archivo.write(strregistro)
        ML2=Label(framedepositorealizado1, text=str1,fg="#f2f5f7",font=("Verdana", 9),bg="#301fc9")
        ML2.pack(in_=framedepositorealizado1,fill=BOTH,expand=True)
        ML2=Label(framedepositorealizado2, text="Desea otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framedepositorealizado2,fill=BOTH,expand=True)
        ML2=Label(framedepositorealizado3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framedepositorealizado3,fill=BOTH,expand=True)
        ML2=Label(framedepositorealizado4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framedepositorealizado4,fill=BOTH,expand=True)
        depositorealizadoboton8 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowdepositorealizado))
        depositorealizadoboton8.place(x=755, y=380)
        depositorealizadoboton0 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowdepositorealizado))
        depositorealizadoboton0.place(x=755, y=490)
    else:
        ML1=Label(framedepositorealizado0, text="Deposito",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML1.pack(in_=framedepositorealizado0,fill=BOTH,expand=True)
        str1="Lo sentimos, la cuenta " + str(cuenta) + " no existe en nuestro banco. No se ha realizado el deposito."
        ML2=Label(framedepositorealizado1, text=str1,fg="#f2f5f7",font=("Verdana", 9),bg="#301fc9")
        ML2.pack(in_=framedepositorealizado1,fill=BOTH,expand=True)
        ML2=Label(framedepositorealizado2, text="Desea otra operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML2.pack(in_=framedepositorealizado2,fill=BOTH,expand=True)
        ML2=Label(framedepositorealizado3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framedepositorealizado3,fill=BOTH,expand=True)
        ML2=Label(framedepositorealizado4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
        ML2.pack(in_=framedepositorealizado4,fill=BOTH,expand=True)
        depositorealizadoboton8 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowdepositorealizado))
        depositorealizadoboton8.place(x=755, y=380)
        depositorealizadoboton0 = Button(windowdepositorealizado,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_salir(windowdepositorealizado))
        depositorealizadoboton0.place(x=755, y=490)

 

def menu_clave():
    global windowmenu
    global windowclave
    global EC1
    global EC2
    #reducimos ventana menu
    windowmenu.withdraw()
    #creamos ventana clave
    windowclave=Toplevel()
    windowclave.title("ATM BANCO DE CHILE")
    windowclave.configure(bg="#151d2a")
    windowclave.geometry("900x600")
    #main frameclave
    frameclave= LabelFrame(windowclave,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    frameclave.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples frameclave
    frameclave0 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave0.pack(expand=True)
    frameclave1 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave1.pack(fill=BOTH,expand=True)
    frameclave2 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave2.pack(fill=BOTH,expand=True)
    frameclave3 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave3.pack(fill=BOTH,expand=True)
    frameclave4 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    claveboton1 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton1.place(x=2, y=50)
    claveboton2 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton2.place(x=755, y=50)
    claveboton3 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton3.place(x=2, y=160)
    claveboton4 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton4.place(x=755, y=160)
    claveboton5 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton5.place(x=2, y=270)
    claveboton6 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton6.place(x=755, y=270)
    claveboton7 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton7.place(x=2, y=380)
    claveboton9 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton9.place(x=2, y=490)
    ML1=Label(frameclave0, text="Cambio de Clave",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML1.pack(in_=frameclave0,fill=BOTH,expand=True)
    frameclave11 = LabelFrame(frameclave1,bg="#301fc9",relief=FLAT,bd=0)
    frameclave11.pack(fill=BOTH,expand=True)
    frameclave12 = LabelFrame(frameclave1,bg="#301fc9",relief=FLAT,bd=0)
    frameclave12.pack(fill=BOTH,expand=True)
    L1=Label(frameclave11,text="Ingrese Clave Actual:")
    L1.pack(in_=frameclave11,side=LEFT,fill=BOTH,expand=True)
    EC1=Entry(frameclave11)
    EC1.pack(in_=frameclave11,side=RIGHT,fill=BOTH,expand=True)
    EC1.insert(0,"Ej: 1234")
    L2=Label(frameclave12,text="Ingrese Clave Nueva: ")
    L2.pack(in_=frameclave12,side=LEFT,fill=BOTH,expand=True)
    EC2=Entry(frameclave12)
    EC2.pack(in_=frameclave12,side=RIGHT,fill=BOTH,expand=True)
    EC2.insert(0,"Ej: 4321")
    ML2=Label(frameclave2, text="Desea realizar esta operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML2.pack(in_=frameclave2,fill=BOTH,expand=True)
    ML2=Label(frameclave3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
    ML2.pack(in_=frameclave3,fill=BOTH,expand=True)
    ML2=Label(frameclave4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
    ML2.pack(in_=frameclave4,fill=BOTH,expand=True)
    claveboton8 = Button(windowclave,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_clave_cambiar())
    claveboton8.place(x=755, y=380)
    claveboton0 = Button(windowclave,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowclave))
    claveboton0.place(x=755, y=490)



def menu_clave_cambiar():
    global windowclave
    global windowclavecambiar
    #reducimos ventana clave
    windowclave.withdraw()
    #creamos ventana clave
    windowclave=Toplevel()
    windowclave.title("ATM BANCO DE CHILE")
    windowclave.configure(bg="#151d2a")
    windowclave.geometry("900x600")
    #main frameclave
    frameclave= LabelFrame(windowclave,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    frameclave.pack(fill=BOTH,expand=True,padx=150,pady=20)
    #dividimos en multiples frameclave
    frameclave0 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave0.pack(expand=True)
    frameclave1 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave1.pack(fill=BOTH,expand=True)
    frameclave2 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave2.pack(fill=BOTH,expand=True)
    frameclave3 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave3.pack(fill=BOTH,expand=True)
    frameclave4 = LabelFrame(frameclave,bg="#301fc9",relief=FLAT,bd=0)
    frameclave4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    claveboton1 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton1.place(x=2, y=50)
    claveboton2 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton2.place(x=755, y=50)
    claveboton3 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton3.place(x=2, y=160)
    claveboton4 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton4.place(x=755, y=160)
    claveboton5 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton5.place(x=2, y=270)
    claveboton6 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton6.place(x=755, y=270)
    claveboton7 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton7.place(x=2, y=380)
    claveboton9 = Button(windowclave,bg="#8b93a6",padx=68,pady=25)
    claveboton9.place(x=2, y=490)
    ML1=Label(frameclave0, text="Cambio de Clave",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML1.pack(in_=frameclave0,fill=BOTH,expand=True)
    frameclave11 = LabelFrame(frameclave1,bg="#301fc9",relief=FLAT,bd=0)
    frameclave11.pack(fill=BOTH,expand=True)
    frameclave12 = LabelFrame(frameclave1,bg="#301fc9",relief=FLAT,bd=0)
    frameclave12.pack(fill=BOTH,expand=True)
    L1=Label(frameclave11,text="Ingrese Clave Actual:")
    L1.pack(in_=frameclave11,side=LEFT,fill=BOTH,expand=True)
    EC1=Entry(frameclave11)
    EC1.pack(in_=frameclave11,side=RIGHT,fill=BOTH,expand=True)
    EC1.insert(0,"Ej: 1234")
    L2=Label(frameclave12,text="Ingrese Clave Nueva: ")
    L2.pack(in_=frameclave12,side=LEFT,fill=BOTH,expand=True)
    EC2=Entry(frameclave12)
    EC2.pack(in_=frameclave12,side=RIGHT,fill=BOTH,expand=True)
    EC2.insert(0,"Ej: 4321")
    ML2=Label(frameclave2, text="Desea realizar esta operacion?",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML2.pack(in_=frameclave2,fill=BOTH,expand=True)
    ML2=Label(frameclave3, text="SI-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
    ML2.pack(in_=frameclave3,fill=BOTH,expand=True)
    ML2=Label(frameclave4, text="NO-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",anchor=E)
    ML2.pack(in_=frameclave4,fill=BOTH,expand=True)
    claveboton8 = Button(windowclave,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_clave_cambiar())
    claveboton8.place(x=755, y=380)
    claveboton0 = Button(windowclave,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowclave))
    claveboton0.place(x=755, y=490)



def menu_admin():
    global windowmenu
    global windowadmin
    if admin==1:
        #reducimos ventana menu
        windowmenu.withdraw()
        #creamos ventana admin
        windowadmin=Toplevel()
        windowadmin.title("ATM BANCO DE CHILE")
        windowadmin.configure(bg="#151d2a")
        windowadmin.geometry("900x600")
        #main frameadmin
        frameadmin= LabelFrame(windowadmin,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
        frameadmin.pack(fill=BOTH,expand=True,padx=150,pady=20)
        #dividimos en multiples frameadmin
        frameadmin0 = LabelFrame(frameadmin,bg="#301fc9",relief=FLAT,bd=0)
        frameadmin0.pack(expand=True)
        frameadmin1 = LabelFrame(frameadmin,bg="#301fc9",relief=FLAT,bd=0)
        frameadmin1.pack(fill=BOTH,expand=True)
        frameadmin2 = LabelFrame(frameadmin,bg="#301fc9",relief=FLAT,bd=0)
        frameadmin2.pack(fill=BOTH,expand=True)
        frameadmin3 = LabelFrame(frameadmin,bg="#301fc9",relief=FLAT,bd=0)
        frameadmin3.pack(fill=BOTH,expand=True)
        frameadmin4 = LabelFrame(frameadmin,bg="#301fc9",relief=FLAT,bd=0)
        frameadmin4.pack(fill=BOTH,expand=True)
        #empezamos a crear objetos
        adminboton1 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:accion_admin(1))
        adminboton1.place(x=2, y=50)
        adminboton2 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:accion_admin(2))
        adminboton2.place(x=755, y=50)
        adminboton3 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:accion_admin(3))
        adminboton3.place(x=2, y=160)
        adminboton4 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:accion_admin(4))
        adminboton4.place(x=755, y=160)
        adminboton5 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:accion_admin(5))
        adminboton5.place(x=2, y=270)
        adminboton6 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:accion_admin(6))
        adminboton6.place(x=755, y=270)
        adminboton7 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:accion_admin(7))
        adminboton7.place(x=2, y=380)
        adminboton8 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:accion_admin(8))
        adminboton8.place(x=755, y=380)
        adminboton9 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:accion_admin(9))
        adminboton9.place(x=2, y=490)
        adminboton0 = Button(windowadmin,bg="#8b93a6",padx=68,pady=25,command=lambda:menu_principal_volver(windowadmin))
        adminboton0.place(x=755, y=490)
        ML1=Label(frameadmin0, text="<--Cambiar Nro. Cta.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=W)
        ML1.pack(in_=frameadmin0,side=LEFT,fill=BOTH,expand=True)
        ML2=Label(frameadmin0, text="Cambiar PIN Cta.-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
        ML2.pack(in_=frameadmin0,side=RIGHT,fill=BOTH,expand=True)
        ML3=Label(frameadmin1, text="<--Dar/Quitar Admin",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=W)
        ML3.pack(in_=frameadmin1,side=LEFT,fill=BOTH,expand=True)
        ML4=Label(frameadmin1, text="Cambiar Saldo Cta.-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
        ML4.pack(in_=frameadmin1,side=RIGHT,fill=BOTH,expand=True)
        ML5=Label(frameadmin2, text="<--Consultar Saldo Cta.",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=W)
        ML5.pack(in_=frameadmin2,side=LEFT,fill=BOTH,expand=True)
        ML6=Label(frameadmin2, text="Consulta de Operaciones-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
        ML6.pack(in_=frameadmin2,side=RIGHT,fill=BOTH,expand=True)
        ML7=Label(frameadmin3, text="<--Cargar Gaveta",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=25,anchor=W)
        ML7.pack(in_=frameadmin3,side=LEFT,fill=BOTH,expand=True)
        ML8=Label(frameadmin3, text="Buscar Usuario-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
        ML8.pack(in_=frameadmin3,side=RIGHT,fill=BOTH,expand=True)
        ML9=Label(frameadmin4, text="<--Eliminar Usuario",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=W)
        ML9.pack(in_=frameadmin4,side=LEFT,fill=BOTH,expand=True)
        ML0=Label(frameadmin4, text="Menu Principal-->",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",width=28,anchor=E)
        ML0.pack(in_=frameadmin4,side=RIGHT,fill=BOTH,expand=True)
    else:
        windowmenu.withdraw()
        windowmenu.deiconify()



def accion_admin(tipo):
    global MAAE1
    global MAAE2
    global MAAE3
    windowaadmin=Toplevel()
    windowaadmin.title("ATM BANCO DE CHILE")
    windowaadmin.configure(bg="#151d2a")
    windowaadmin.geometry("600x600")
    #main frameaadmin
    frameaadmin= LabelFrame(windowaadmin,text="Menu Administrativo",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    frameaadmin.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples frameaadmin
    frameaadmin0 = LabelFrame(frameaadmin,bg="#301fc9",relief=FLAT,bd=0)
    frameaadmin0.pack(expand=True)
    frameaadmin1 = LabelFrame(frameaadmin,bg="#301fc9",relief=FLAT,bd=0)
    frameaadmin1.pack(fill=BOTH,expand=True)
    frameaadmin2 = LabelFrame(frameaadmin,bg="#301fc9",relief=FLAT,bd=0)
    frameaadmin2.pack(fill=BOTH,expand=True)
    frameaadmin3 = LabelFrame(frameaadmin,bg="#301fc9",relief=FLAT,bd=0)
    frameaadmin3.pack(fill=BOTH,expand=True)
    frameaadmin4 = LabelFrame(frameaadmin,bg="#301fc9",relief=FLAT,bd=0)
    frameaadmin4.pack(fill=BOTH,expand=True)
    if tipo==1:
        ML1=Label(frameaadmin0, text="Actualizar Numero de Cta.",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        L1=Label(frameaadmin1,text="Numero de Cuenta actual: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        MAAE1.insert(0,"Ej: 12345678-9")
        L2=Label(frameaadmin2,text="Numero de cuenta nuevo: ")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.insert(0,"Ej: 98765432-1")
        L3=Label(frameaadmin3,text="Respuesta: ")
        L3.pack(in_=frameaadmin3,side=LEFT,fill=BOTH,expand=True)
        MAAE3=Entry(frameaadmin3)
        MAAE3.pack(in_=frameaadmin3,side=RIGHT,fill=BOTH,expand=True)
        MAAE3.config(state="readonly")
    elif tipo==2:
        ML1=Label(frameaadmin0, text="Actualizar PIN de Cta.",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        L1=Label(frameaadmin1,text="Numero de Cuenta: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        MAAE1.insert(0,"Ej: 12345678-9")
        L2=Label(frameaadmin2,text="Nuevo PIN: ")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.insert(0,"Ej: 1234")
        L3=Label(frameaadmin3,text="Respuesta: ")
        L3.pack(in_=frameaadmin3,side=LEFT,fill=BOTH,expand=True)
        MAAE3=Entry(frameaadmin3)
        MAAE3.pack(in_=frameaadmin3,side=RIGHT,fill=BOTH,expand=True)
        MAAE3.config(state="readonly")
    elif tipo==3:
        ML1=Label(frameaadmin0, text="DAR/Quitar privilegio administrativo",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        L1=Label(frameaadmin1,text="Numero de Cuenta: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        MAAE1.insert(0,"Ej: 12345678-9")
        L2=Label(frameaadmin2,text="Admin SI/NO (1/0):")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.insert(0,"Ej: 1")
        L3=Label(frameaadmin3,text="Respuesta: ")
        L3.pack(in_=frameaadmin3,side=LEFT,fill=BOTH,expand=True)
        MAAE3=Entry(frameaadmin3)
        MAAE3.pack(in_=frameaadmin3,side=RIGHT,fill=BOTH,expand=True)
        MAAE3.config(state="readonly")
    elif tipo==4:
        ML1=Label(frameaadmin0, text="Actualizar Saldo de Cta.",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        L1=Label(frameaadmin1,text="Numero de Cuenta: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        MAAE1.insert(0,"Ej: 12345678-9")
        L2=Label(frameaadmin2,text="Nuevo SALDO: ")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.insert(0,"Ej: 123321")
        L3=Label(frameaadmin3,text="Respuesta: ")
        L3.pack(in_=frameaadmin3,side=LEFT,fill=BOTH,expand=True)
        MAAE3=Entry(frameaadmin3)
        MAAE3.pack(in_=frameaadmin3,side=RIGHT,fill=BOTH,expand=True)
        MAAE3.config(state="readonly")
    elif tipo==5:
        ML1=Label(frameaadmin0, text="Consultar Saldo de Cta.",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        L1=Label(frameaadmin1,text="Numero de Cuenta: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        MAAE1.insert(0,"Ej: 12345678-9")
        L2=Label(frameaadmin2,text="Saldo: ")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.config(state="readonly")
        L3=Label(frameaadmin3,text="Nombre Usuario: ")
        L3.pack(in_=frameaadmin3,side=LEFT,fill=BOTH,expand=True)
        MAAE3=Entry(frameaadmin3)
        MAAE3.pack(in_=frameaadmin3,side=RIGHT,fill=BOTH,expand=True)
        MAAE3.config(state="readonly")
    elif tipo==6:
        ML1=Label(frameaadmin0, text="Consulta de Operaciones",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        L1=Label(frameaadmin1,text="Nombre/Cuenta a consultar: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        L2=Label(frameaadmin2,text="Operaciones: ")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.config(state="readonly")
    elif tipo==7:
        ML1=Label(frameaadmin0, text="Agregar Dinero a Gaveta.",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        L1=Label(frameaadmin1,text="Cantidad: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        MAAE1.insert(0,"Ej: 123321123")
        L2=Label(frameaadmin2,text="Monto Anterior: ")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.config(state="readonly")
        L3=Label(frameaadmin3,text="Nuevo Monto: ")
        L3.pack(in_=frameaadmin3,side=LEFT,fill=BOTH,expand=True)
        MAAE3=Entry(frameaadmin3)
        MAAE3.pack(in_=frameaadmin3,side=RIGHT,fill=BOTH,expand=True)
        MAAE3.config(state="readonly")
    elif tipo==8:
        ML1=Label(frameaadmin0, text="Buscar Usuario por Nombre",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        global C1
        C1 = Canvas(frameaadmin0, width=200, height=200, bg="#301fc9", bd=0, relief=FLAT)
        C1.pack(in_=frameaadmin0)
        imgc1 = PhotoImage(file="noexiste.png")
        Lista_Imagenes.append(imgc1)
        C1.create_image(0, 0, anchor=NW, image=imgc1)
        L1=Label(frameaadmin1,text="Nombre de Usuario a buscar: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        MAAE1.insert(0,"Ej: Tulio")
        L2=Label(frameaadmin2,text="Nombre registrado: ")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.insert(0,"Tulio Triviño")
        MAAE2.config(state="readonly")
        L3=Label(frameaadmin3,text="Numero de Cuenta: ")
        L3.pack(in_=frameaadmin3,side=LEFT,fill=BOTH,expand=True)
        MAAE3=Entry(frameaadmin3)
        MAAE3.pack(in_=frameaadmin3,side=RIGHT,fill=BOTH,expand=True)
        MAAE3.insert(0,"123321123-0")
        MAAE3.config(state="readonly")
    elif tipo==9:
        ML1=Label(frameaadmin0, text="Eliminar Usuario",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        L1=Label(frameaadmin1,text="Numero de Cuenta: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        MAAE1.insert(0,"Ej: 12345678-9")
        L2=Label(frameaadmin2,text="Confirma: ")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.insert(0,"Escriba 'SI'")
        L3=Label(frameaadmin3,text="Respuesta: ")
        L3.pack(in_=frameaadmin3,side=LEFT,fill=BOTH,expand=True)
        MAAE3=Entry(frameaadmin3)
        MAAE3.pack(in_=frameaadmin3,side=RIGHT,fill=BOTH,expand=True)
        MAAE3.config(state="readonly")
    else:
        ML1=Label(frameaadmin0, text="ERROR",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
        ML1.pack(in_=frameaadmin0,fill=BOTH,expand=True)
        L1=Label(frameaadmin1,text="ERROR: ")
        L1.pack(in_=frameaadmin1,side=LEFT,fill=BOTH,expand=True)
        MAAE1=Entry(frameaadmin1)
        MAAE1.pack(in_=frameaadmin1,side=RIGHT,fill=BOTH,expand=True)
        MAAE1.insert(0,"Ej: ERROR")
        L2=Label(frameaadmin2,text="ERROR: ")
        L2.pack(in_=frameaadmin2,side=LEFT,fill=BOTH,expand=True)
        MAAE2=Entry(frameaadmin2)
        MAAE2.pack(in_=frameaadmin2,side=RIGHT,fill=BOTH,expand=True)
        MAAE2.insert(0,"Ej: ERROR")
        L3=Label(frameaadmin3,text="ERROR: ")
        L3.pack(in_=frameaadmin3,side=LEFT,fill=BOTH,expand=True)
        MAAE3=Entry(frameaadmin3)
        MAAE3.pack(in_=frameaadmin3,side=RIGHT,fill=BOTH,expand=True)
        MAAE3.insert(0,"Ej: ERROR")
        MAAE3.config(state="readonly")
    if tipo==0:
        MB1=Button(frameaadmin4, text="ERROR")
        MB1.pack(in_=frameaadmin4,fill=BOTH,expand=True)
    else:
        MB1=Button(frameaadmin4, text="EJECUTAR",command=lambda:ejecutar_admin(tipo))
        MB1.pack(in_=frameaadmin4,fill=BOTH,expand=True)
    MB2=Button(frameaadmin4, text="VOLVER",command=lambda: windowaadmin.withdraw())
    MB2.pack(in_=frameaadmin4,fill=BOTH,expand=True)



def ejecutar_admin(tipo):
    global MAAE1
    global MAAE2
    global MAAE3
    global nrocta
    global gaveta
    if tipo==1:
        cuentaactual=MAAE1.get()
        cuentanueva=MAAE2.get()
        if cuentaactual!=cuentanueva:
            fileadmin = str(nrocta) + ".txt"
            #verificamos que usuario existe
            if(path.exists(fileadmin)):
                #si edita cuenta propia, guardamos valores en txt
                if cuentaactual==nrocta:
                    guardar_valores_usuario(nrocta)
                #abrimos txt y cargamos valores
                opentxtadmin = open(fileadmin, "r")
                resultadoadmin = opentxtadmin.read().split(",")
                opentxtadmin.close()
                usuarioadmin = resultadoadmin[0]
                nombreusuarioadmin = resultadoadmin[1]
                pinadmin = int(resultadoadmin[2])
                intentosadmin= int(resultadoadmin[3])
                bloqueadoadmin= int(resultadoadmin[4])
                adminadmin = int(resultadoadmin[5])
                saldoadmin = int(resultadoadmin[6])
                nombretipoctaadmin = resultadoadmin[7]
                tipoctaadmin = resultadoadmin[8]
                cobrogiroadmin = int(resultadoadmin[9])
                cobrosaldoadmin = int(resultadoadmin[10])
                #cambiamos el usuario
                usuarioadmin=cuentanueva
                listaescribiradmin = [usuarioadmin,nombreusuarioadmin,pinadmin,intentosadmin,bloqueadoadmin,adminadmin,saldoadmin,nombretipoctaadmin,tipoctaadmin,cobrogiroadmin,cobrosaldoadmin]
                escribiradmin = ','.join(str(i) for i in listaescribiradmin)
                with open(fileadmin, "w") as output:
                    output.write(str(escribiradmin))
                #renombramos archivo
                os.rename(r""+cuentaactual+".txt",r""+cuentanueva+".txt")
                #si edita cuenta propia, recargamos valores desde txt
                if cuentaactual==nrocta:
                    nrocta = cuentanueva
                    definir_valores_usuario(nrocta)
                MAAE1.delete(0,END)
                MAAE1.insert(0,"Ej: 12345678-9")
                MAAE2.delete(0,END)
                MAAE2.insert(0,"Ej: 98765432-1")
                MAAE3.config(state="normal")
                MAAE3.delete(0,END)
                MAAE3.insert(0,"La cuenta ",cuentaactual," ahora es ",cuentanueva," .")
                MAAE3.config(state="readonly")
            else:
                MAAE1.delete(0,END)
                MAAE1.insert(0,"Ej: 12345678-9")
                MAAE2.delete(0,END)
                MAAE2.insert(0,"Ej: 98765432-1")
                MAAE3.config(state="normal")
                MAAE3.delete(0,END)
                MAAE3.insert(0,"La cuenta ",cuentaactual," no existe.")
                MAAE3.config(state="readonly")
        else:
            MAAE1.delete(0,END)
            MAAE1.insert(0,"Ej: 12345678-9")
            MAAE2.delete(0,END)
            MAAE2.insert(0,"Ej: 98765432-1")
            MAAE3.config(state="normal")
            MAAE3.delete(0,END)
            MAAE3.insert(0,"La cuenta actual no puede ser igual a la cuenta nueva.")
            MAAE3.config(state="readonly")

    elif tipo==2:
        cuentaactual=MAAE1.get()
        pinnueva=MAAE2.get()
        fileadmin = str(cuentaactual) + ".txt"
        #verificamos que usuario existe
        if(path.exists(fileadmin)):
            #si edita cuenta propia, guardamos valores en txt
            if cuentaactual==nrocta:
                guardar_valores_usuario(nrocta)
            #abrimos txt y cargamos valores
            opentxtadmin = open(fileadmin, "r")
            resultadoadmin = opentxtadmin.read().split(",")
            opentxtadmin.close()
            usuarioadmin = resultadoadmin[0]
            nombreusuarioadmin = resultadoadmin[1]
            pinadmin = int(resultadoadmin[2])
            intentosadmin= int(resultadoadmin[3])
            bloqueadoadmin= int(resultadoadmin[4])
            adminadmin = int(resultadoadmin[5])
            saldoadmin = int(resultadoadmin[6])
            nombretipoctaadmin = resultadoadmin[7]
            tipoctaadmin = resultadoadmin[8]
            cobrogiroadmin = int(resultadoadmin[9])
            cobrosaldoadmin = int(resultadoadmin[10])
            #cambiamos el usuario
            pinadmin=int(pinnueva)
            listaescribiradmin = [usuarioadmin,nombreusuarioadmin,pinadmin,intentosadmin,bloqueadoadmin,adminadmin,saldoadmin,nombretipoctaadmin,tipoctaadmin,cobrogiroadmin,cobrosaldoadmin]
            escribiradmin = ','.join(str(i) for i in listaescribiradmin)
            with open(fileadmin, "w") as output:
                output.write(str(escribiradmin))
            #si edita cuenta propia, recargamos valores desde txt
            if cuentaactual==nrocta:
                definir_valores_usuario(nrocta)
            MAAE1.delete(0,END)
            MAAE1.insert(0,"Ej: 12345678-9")
            MAAE2.delete(0,END)
            MAAE2.insert(0,"Ej: 1234")
            MAAE3.config(state="normal")
            MAAE3.delete(0,END)
            MAAE3.insert(0,"El nuevo PIN de la cuenta ",cuentaactual," es ",cuentanueva," .")
            MAAE3.config(state="readonly")
        else:
            MAAE1.delete(0,END)
            MAAE1.insert(0,"Ej: 12345678-9")
            MAAE2.delete(0,END)
            MAAE2.insert(0,"Ej: 98765432-1")
            MAAE3.config(state="normal")
            MAAE3.delete(0,END)
            MAAE3.insert(0,"La cuenta ",cuentaactual," no existe.")
            MAAE3.config(state="readonly")

    elif tipo==3:
        cuentaactual=MAAE1.get()
        adminnueva=MAAE2.get()
        if cuentaactual!=nrocta:
            if int(adminnueva) == 0 or int(adminnueva) == 1:
                fileadmin = str(cuentaactual) + ".txt"
                #verificamos que usuario existe
                if(path.exists(fileadmin)):
                    #abrimos txt y cargamos valores
                    opentxtadmin = open(fileadmin, "r")
                    resultadoadmin = opentxtadmin.read().split(",")
                    opentxtadmin.close()
                    usuarioadmin = resultadoadmin[0]
                    nombreusuarioadmin = resultadoadmin[1]
                    pinadmin = int(resultadoadmin[2])
                    intentosadmin= int(resultadoadmin[3])
                    bloqueadoadmin= int(resultadoadmin[4])
                    adminadmin = int(resultadoadmin[5])
                    saldoadmin = int(resultadoadmin[6])
                    nombretipoctaadmin = resultadoadmin[7]
                    tipoctaadmin = resultadoadmin[8]
                    cobrogiroadmin = int(resultadoadmin[9])
                    cobrosaldoadmin = int(resultadoadmin[10])
                    #cambiamos el usuario
                    adminadmin=int(adminnueva)
                    listaescribiradmin = [usuarioadmin,nombreusuarioadmin,pinadmin,intentosadmin,bloqueadoadmin,adminadmin,saldoadmin,nombretipoctaadmin,tipoctaadmin,cobrogiroadmin,cobrosaldoadmin]
                    escribiradmin = ','.join(str(i) for i in listaescribiradmin)
                    with open(fileadmin, "w") as output:
                        output.write(str(escribiradmin))
                    MAAE1.delete(0,END)
                    MAAE1.insert(0,"Ej: 12345678-9")
                    MAAE2.delete(0,END)
                    MAAE2.insert(0,"Ej: 1")
                    MAAE3.config(state="normal")
                    MAAE3.delete(0,END)
                    MAAE3.insert(0,"El estado admin de la cuenta ",cuentaactual," ahora es ",adminnueva," .")
                    MAAE3.config(state="readonly")
                else:
                    MAAE1.delete(0,END)
                    MAAE1.insert(0,"Ej: 12345678-9")
                    MAAE2.delete(0,END)
                    MAAE2.insert(0,"Ej: 1")
                    MAAE3.config(state="normal")
                    MAAE3.delete(0,END)
                    MAAE3.insert(0,"La cuenta ",cuentaactual," no existe.")
                    MAAE3.config(state="readonly")
            else:
                MAAE1.delete(0,END)
                MAAE1.insert(0,"Ej: 12345678-9")
                MAAE2.delete(0,END)
                MAAE2.insert(0,"Ej: 1")
                MAAE3.config(state="normal")
                MAAE3.delete(0,END)
                MAAE3.insert(0,"El campo 2 solo acepta valores 1 y 0.")
                MAAE3.config(state="readonly")
        else:
            MAAE1.delete(0,END)
            MAAE1.insert(0,"Ej: 12345678-9")
            MAAE2.delete(0,END)
            MAAE2.insert(0,"Ej: 1")
            MAAE3.config(state="normal")
            MAAE3.delete(0,END)
            MAAE3.insert(0,"No puedes quitarte el privilegio administrativo.")
            MAAE3.config(state="readonly")

    elif tipo==4:
        cuentaactual=MAAE1.get()
        saldonueva=MAAE2.get()
        if (saldonueva.isdigit()):
            strtxt = ".txt"
            fileadmin = str(cuentaactual) + ".txt"
            #verificamos que usuario existe
            if(path.exists(fileadmin)):
                #si edita cuenta propia, guardamos valores en txt
                if cuentaactual==nrocta:
                    guardar_valores_usuario(nrocta)
                #abrimos txt y cargamos valores
                opentxtadmin = open(fileadmin, "r")
                resultadoadmin = opentxtadmin.read().split(",")
                opentxtadmin.close()
                usuarioadmin = resultadoadmin[0]
                nombreusuarioadmin = resultadoadmin[1]
                pinadmin = int(resultadoadmin[2])
                intentosadmin= int(resultadoadmin[3])
                bloqueadoadmin= int(resultadoadmin[4])
                adminadmin = int(resultadoadmin[5])
                saldoadmin = int(resultadoadmin[6])
                nombretipoctaadmin = resultadoadmin[7]
                tipoctaadmin = resultadoadmin[8]
                cobrogiroadmin = int(resultadoadmin[9])
                cobrosaldoadmin = int(resultadoadmin[10])
                #cambiamos el usuario
                saldoadmin=int(saldonueva)
                listaescribiradmin = [usuarioadmin,nombreusuarioadmin,pinadmin,intentosadmin,bloqueadoadmin,adminadmin,saldoadmin,nombretipoctaadmin,tipoctaadmin,cobrogiroadmin,cobrosaldoadmin]
                escribiradmin = ','.join(str(i) for i in listaescribiradmin)
                with open(fileadmin, "w") as output:
                    output.write(str(escribiradmin))
                #si edita cuenta propia, recargamos valores desde txt
                if cuentaactual==nrocta:
                    definir_valores_usuario(nrocta)
                MAAE1.delete(0,END)
                MAAE1.insert(0,"Ej: 12345678-9")
                MAAE2.delete(0,END)
                MAAE2.insert(0,"Ej: 123321123")
                MAAE3.config(state="normal")
                MAAE3.delete(0,END)
                MAAE3.insert(0,"El nuevo SALDO de la cuenta ",cuentaactual," es ",saldonueva," .")
                MAAE3.config(state="readonly")
            else:
                MAAE1.delete(0,END)
                MAAE1.insert(0,"Ej: 12345678-9")
                MAAE2.delete(0,END)
                MAAE2.insert(0,"Ej: 123321123")
                MAAE3.config(state="normal")
                MAAE3.delete(0,END)
                MAAE3.insert(0,"La cuenta ",cuentaactual," no existe.")
                MAAE3.config(state="readonly")
        else:
            MAAE1.delete(0,END)
            MAAE1.insert(0,"Ej: 12345678-9")
            MAAE2.delete(0,END)
            MAAE2.insert(0,"Ej: 123321123")
            MAAE3.config(state="normal")
            MAAE3.delete(0,END)
            MAAE3.insert(0,"El campo 2 acepta solo digitos.")
            MAAE3.config(state="readonly")

    elif tipo==5:
        cuentaactual=MAAE1.get()
        if (True==True):
            strtxt = ".txt"
            fileadmin = str(cuentaactual) + ".txt"
            #verificamos que usuario existe
            if(path.exists(fileadmin)):
                #si edita cuenta propia, guardamos valores en txt
                if cuentaactual==nrocta:
                    guardar_valores_usuario(nrocta)
                #abrimos txt y cargamos valores
                opentxtadmin = open(fileadmin, "r")
                resultadoadmin = opentxtadmin.read().split(",")
                opentxtadmin.close()
                usuarioadmin = resultadoadmin[0]
                nombreusuarioadmin = resultadoadmin[1]
                pinadmin = int(resultadoadmin[2])
                intentosadmin= int(resultadoadmin[3])
                bloqueadoadmin= int(resultadoadmin[4])
                adminadmin = int(resultadoadmin[5])
                saldoadmin = int(resultadoadmin[6])
                nombretipoctaadmin = resultadoadmin[7]
                tipoctaadmin = resultadoadmin[8]
                cobrogiroadmin = int(resultadoadmin[9])
                cobrosaldoadmin = int(resultadoadmin[10])
                MAAE1.delete(0,END)
                MAAE1.insert(0,"Ej: 12345678-9")
                MAAE2.config(state="normal")
                MAAE2.delete(0,END)
                MAAE2.insert(0,saldoadmin)
                MAAE2.config(state="readonly")
                MAAE3.config(state="normal")
                MAAE3.delete(0,END)
                MAAE3.insert(0,nombreusuarioadmin)
                MAAE3.config(state="readonly")
            else:
                MAAE1.delete(0,END)
                MAAE1.insert(0,"Ej: 12345678-9")
                MAAE2.config(state="normal")
                MAAE2.delete(0,END)
                MAAE2.config(state="readonly")
                MAAE3.config(state="normal")
                MAAE3.delete(0,END)
                MAAE3.config(state="readonly")

    elif tipo==6:
        guardar_valores_cajero()
        definir_valores_cajero()
        MAAE2.config(state="normal")
        MAAE2.delete(0,END)
        nombre=MAAE1.get()
        operacionesraw=cargar_transacciones(nombre)
        operacionesjoin="".join(operacionesraw)
        operaciones=operacionesjoin.strip("''[]")
        if operacionesraw:
            MAAE2.insert(0,operaciones)
        else:
            MAAE2.insert(0,"No existen operaciones en el registro.")
        MAAE1.config(state="normal")
        MAAE1.delete(0,END)
        MAAE1.insert(0,"Ej: Tulio")
        MAAE2.config(state="readonly")

    elif tipo==7:
        gavetanueva=MAAE1.get()
        if gavetanueva.isdigit():
            guardar_valores_cajero()
            definir_valores_cajero()
            gavetaanterior=gaveta
            gaveta=int(gavetanueva)
            MAAE1.delete(0,END)
            MAAE1.insert(0,"Ej: 123321123")
            MAAE2.config(state="normal")
            MAAE2.delete(0,END)
            MAAE2.insert(0,gavetaanterior)
            MAAE2.config(state="readonly")
            MAAE3.config(state="normal")
            MAAE3.delete(0,END)
            MAAE3.insert(0,gavetanueva)
            MAAE3.config(state="readonly")
        else:
            MAAE1.delete(0,END)
            MAAE1.insert(0,"Ej: 123321123")
            MAAE2.config(state="normal")
            MAAE2.delete(0,END)
            MAAE2.config(state="readonly")
            MAAE3.config(state="normal")
            MAAE3.delete(0,END)
            MAAE3.insert(0,"El campo 1 acepta solo digitos")
            MAAE3.config(state="readonly")

    elif tipo==8:
        global C1
        busqueda=MAAE1.get()
        #openlistacuentas = open("listacuentas.txt", "r")
        #resultadolistacuentas = openlistacuentas.read().split(",")
        #consultalista=revisar(resultadolistacuentas,busqueda)
        #consultaraw="".join(consultalista)
        #consulta=consultaraw.strip("''[]")
        dataraw=buscar_por_nombre(busqueda)
        if dataraw:
            data=list(dataraw.split(","))
            foto=data[0] + ".png"
            imgc1 = PhotoImage(file=foto)
            Lista_Imagenes.append(imgc1)
            C1.create_image(0, 0, anchor=NW, image=imgc1)
            MAAE1.delete(0,END)
            MAAE1.insert(0,"Ej: Tulio")
            MAAE2.config(state="normal")
            MAAE2.delete(0,END)
            MAAE2.insert(0,data[0])
            MAAE2.config(state="readonly")
            MAAE3.config(state="normal")
            MAAE3.delete(0,END)
            MAAE3.insert(0,data[1])
            MAAE3.config(state="readonly")
        else:
            foto="noexiste.png"
            imgc1 = PhotoImage(file=foto)
            Lista_Imagenes.append(imgc1)
            C1.create_image(0, 0, anchor=NW, image=imgc1)
            MAAE1.delete(0, END)
            MAAE1.insert(0, "Ej: Tulio")
            MAAE2.config(state="normal")
            MAAE2.delete(0, END)
            MAAE2.insert(0, "CUENTA CONSULTADA NO EXISTE")
            MAAE2.config(state="readonly")
            MAAE3.config(state="normal")
            MAAE3.delete(0, END)
            MAAE3.insert(0, "CUENTA CONSULTADA NO EXISTE")
            MAAE3.config(state="readonly")


    elif tipo==9:
        cuentaactual=MAAE1.get()
        if cuentaactual!=nrocta:
            strtxt = ".txt"
            fileadmin = str(cuentaactual) + ".txt"
            #verificamos que usuario existe
            if(path.exists(fileadmin)):
                confirma=MAAE2.get()
                if confirma in ListaSi:
                    MAAE1.delete(0,END)
                    MAAE1.insert(0,"Ej: 12345678-9")
                    MAAE2.config(state="normal")
                    MAAE2.delete(0,END)
                    MAAE2.insert(0,"Escribe 'SI'")
                    MAAE2.config(state="readonly")
                    MAAE3.config(state="normal")
                    MAAE3.delete(0,END)
                    MAAE3.insert(0,"Usuario ",cuentaactual," eliminado.")
                    MAAE3.config(state="readonly")
                else:
                    MAAE1.delete(0,END)
                    MAAE1.insert(0,"Ej: 12345678-9")
                    MAAE2.config(state="normal")
                    MAAE2.delete(0,END)
                    MAAE2.insert(0,"Escribe 'SI'")
                    MAAE2.config(state="readonly")
                    MAAE3.config(state="normal")
                    MAAE3.delete(0,END)
                    MAAE3.insert(0,"Por favor confirma operacion.")
                    MAAE3.config(state="readonly")
            else:
                MAAE1.delete(0,END)
                MAAE1.insert(0,"Ej: 12345678-9")
                MAAE2.config(state="normal")
                MAAE2.delete(0,END)
                MAAE2.insert(0,"Escribe 'SI'")
                MAAE2.config(state="readonly")
                MAAE3.config(state="normal")
                MAAE3.delete(0,END)
                MAAE3.insert(0,"Usuario ",cuentaactual," no existe.")
                MAAE3.config(state="readonly")
        else:
            MAAE1.delete(0,END)
            MAAE1.insert(0,"Ej: 12345678-9")
            MAAE2.config(state="normal")
            MAAE2.delete(0,END)
            MAAE2.insert(0,"Escribe 'SI'")
            MAAE2.config(state="readonly")
            MAAE3.config(state="normal")
            MAAE3.delete(0,END)
            MAAE3.insert(0,"No puedes eliminar tu propio usuario.")
            MAAE3.config(state="readonly")


#se reemplaza temporalmente por "buscar_por_nombre"
def revisar(lista, palabra):
    #Funciona bien, es efectivo, es bonito, es perfecto, pero el profe quiere otra cosa.
    res = [all([k in s for k in palabra]) for s in lista]
    return [lista[i] for i in range(0, len(res)) if res[i]]



def menu_principal_volver(tiposalir):
    tiposalir.withdraw()
    menu_principal()



def menu_salir(tiposalir):
    tiposalir.withdraw()
    log_out()
    E1.delete(0,END)
    E1.insert(0,"Ej: 12345678-9")
    menu_login()



def ventana_error(tipoerror):
    windowerror=Toplevel()
    windowerror.title("ATM BANCO DE CHILE")
    windowerror.configure(bg="#151d2a")
    windowerror.geometry("600x600")
    #main frameerror
    frameerror= LabelFrame(windowerror,text="CAJERO AUTOMATICO BANCO DE CHILE",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9",labelanchor=N,padx=20,pady=20)
    frameerror.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples frameerror
    frameerror0 = LabelFrame(frameerror,bg="#301fc9",relief=FLAT,bd=0)
    frameerror0.pack(expand=True)
    frameerror1 = LabelFrame(frameerror,bg="#301fc9",relief=FLAT,bd=0)
    frameerror1.pack(fill=BOTH,expand=True)
    frameerror2 = LabelFrame(frameerror,bg="#301fc9",relief=FLAT,bd=0)
    frameerror2.pack(fill=BOTH,expand=True)
    frameerror3 = LabelFrame(frameerror,bg="#301fc9",relief=FLAT,bd=0)
    frameerror3.pack(fill=BOTH,expand=True)
    frameerror4 = LabelFrame(frameerror,bg="#301fc9",relief=FLAT,bd=0)
    frameerror4.pack(fill=BOTH,expand=True)
    ML1=Label(frameerror0, text="ERROR",fg="#FF0000",font=("Verdana", 22),bg="#301fc9")
    ML1.pack(in_=frameerror0,fill=BOTH,expand=True)
    ML2=Label(frameerror1, text="Por favor resuelve lo siguiente:",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML2.pack(in_=frameerror1,fill=BOTH,expand=True)
    if tipoerror=="pin":
        ML3=Label(frameerror2, text="PIN INVALIDO/INCORRECTO",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML3.pack(in_=frameerror2,fill=BOTH,expand=True)
    elif tipoerror=="usuario":
        ML3=Label(frameerror2, text="USUARIO INVALIDO/INCORRECTO",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML3.pack(in_=frameerror2,fill=BOTH,expand=True)
    elif tipoerror=="data":
        ML3=Label(frameerror2, text="INGRESAR TODOS LOS DATOS",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML3.pack(in_=frameerror2,fill=BOTH,expand=True)
    else:
        ML3=Label(frameerror2, text="ERROR DESCONOCIDO",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
        ML3.pack(in_=frameerror2,fill=BOTH,expand=True)
    ML4=Label(frameerror3, text="Click en el boton para volver",fg="#f2f5f7",font=("Verdana", 14),bg="#301fc9")
    ML4.pack(in_=frameerror3,fill=BOTH,expand=True)
    MB1=Button(frameerror4, text="VOLVER",command=lambda: windowerror.withdraw())
    MB1.pack(in_=frameerror4,fill=BOTH,expand=True)

### AREA PARA COMPLACER WEONES ###

#generamos una lista de archivos para leer al generar la consulta.
def obtener_archivos():
    lista = os.listdir()
    remover = ["cajero.txt","transacciones.txt"]
    for item in lista:
        pngdat=".png"
        if item.endswith(pngdat):
            remover.append(item)
        pydat=".py"
        if item.endswith(pydat):
            remover.append(item)
    cantidad=int(len(lista))
    n=0
    index=0
    while n < cantidad:
        if lista[index] in remover:
            lista.remove(lista[index])
            index = index - 1
        else:
            pass
        index = index + 1
        n=n+1
    return lista



#buscamos un patron entre la lista (infinita) de archivos.
def buscar_por_nombre(nombre):
    lista = obtener_archivos()
    for line in fileinput.FileInput(lista):
        if nombre.lower() in line.lower():
            return line



#otra busqueda de patrones. Tambien conteo de los mismos.
def cargar_transacciones(nombre):
    lista=[]
    for line in fileinput.FileInput("transacciones.txt"):
        if re.search(nombre.lower(),line.lower()):
            lista.append(line)
    return lista



inicio()