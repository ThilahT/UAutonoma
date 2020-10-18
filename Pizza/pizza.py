from tkinter import ttk
from tkinter import *
import time
import os
import sys

def definir_valores():
    global usuario
    usuario = "cajero"
    global pin
    pin = int(1111)
    global intentos
    intentos = int(0)
    global bloqueado
    bloqueado = int(0)
    global usuarioadmin
    usuarioadmin = "supervisor"
    global pinadmin
    pinadmin = int(7272)
    global tipologeado
    tipologeado = "cajero"
    global ventas
    ventas= int(0)
    global gaveta
    gaveta=int(50000)
    global costo_ingredientes
    costo_ingredientes= int(500)
    global costo_bebida
    costo_bebida= int(800)
    global sesion
    sesion = int(0)
    global ingredientes
    ingredientes = int(0)
    global ListaIngredientes
    ListaIngredientes = ["",""]
    global en_grande
    en_grande= ("Verdana", 22)
    global fondo
    fondo = int(0)
    global cajacerrada
    cajacerrada=int(0)
    global Lista_Imagenes
    Lista_Imagenes = []

def verificar_pin():
    global tipologeado
    if E1.get():
        if E2.get():
            #recibimos el pin como string y lo convertimos a integro
            pintrystr= E2.get()
            pintry=int(pintrystr)
            usuariotry= E1.get()
            #verificamos que el usuario sea correcto
            if (usuariotry==usuario):
                #verificamos pin
                if (pintry==pin):
                    #si es correcto, enviamos a menu principal
                    sesion=int(1)
                    tipologeado="cajero"
                    menu_principal()
                else:
                    #si es incorrecto, enviamos error
                    numero_teclado("borrar")
                    ventana_error("pin")
            elif (usuariotry==usuarioadmin):
                #verificamos pin
                if (pintry==pinadmin):
                    #si es correcto, enviamos a menu principal
                    sesion=int(1)
                    tipologeado="admin"
                    menu_principal()
                else:
                    #si es incorrecto, enviamos error
                    numero_teclado("borrar")
                    ventana_error("pin")
            else: 
                ventana_error("usuario")
        else:
            ventana_error("pin")
    else: 
        ventana_error("usuario")

def log_out():
    global inicio
    inicio = 1
    global windowmenu
    windowmenu.withdraw()
    if cajacerrada!=0:
        global windowcierrecaja
        windowcierrecaja.withdraw()
    sesion=int(0)
    tipologeado="cajero"
    menu_login()

def inicio():
    global sesion
    global inicio
    titulo()
    inicio = 0
    definir_valores()
    if (sesion!=0):
        #verificamos si el usuario esta logeado o login automatico esta habilitado
        if (sesion==1):
            menu_principal()
        else:
            #en caso de error, borramos la sesion
            sesion=int(0)
            menu_login()
    else:
        #si no esta logeado, lo enviamos al login
        sesion=int(0)
        menu_login()

def menu_login():
    global windowlogin
    global framelogin2
    global E1
    global E2
    if inicio==0:
        #creamos la ventana
        windowlogin = Tk()
        windowlogin.title("POS Friends Pizza - LOGIN")
        windowlogin.configure(bg="#2e2d2b")
        windowlogin.geometry("600x600")
        #main framelogin
        framelogin = LabelFrame(windowlogin,text="LOGIN Friends Pizza",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
        framelogin.pack(fill=BOTH,expand=True,padx=20,pady=20)
        #dividimos en multiples framelogins
        framelogin0 = LabelFrame(framelogin,bg="#4f4e4a",relief=FLAT,bd=0)
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
        canvaslogin = Canvas(framelogin0,width=200,height=200,bg="#4f4e4a",bd=0,relief=FLAT)      
        canvaslogin.pack(in_=framelogin0)
        imglogologin = PhotoImage(file="./img/logo.png")
        Lista_Imagenes.append(imglogologin)
        canvaslogin.create_image(0,0, anchor=NW, image=imglogologin)
        L1=Label(framelogin1,text="Usuario: ")
        L1.pack(in_=framelogin1,side=LEFT,fill=BOTH,expand=True)
        E1=Entry(framelogin1)
        E1.pack(in_=framelogin1,side=RIGHT,fill=BOTH,expand=True)
        E1.insert(0,"cajero")
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

def menu_principal():
    global windowlogin
    global windowmenu
    global tipologeado
    #reducimos ventana login
    windowlogin.withdraw()
    #creamos ventana menu
    windowmenu=Toplevel()
    windowmenu.geometry("900x760")
    windowmenu.title("POS Friends Pizza - Menú Principal")
    windowmenu.configure(bg="#2e2d2b")
    #creamos el framemenu principal
    framemenu = LabelFrame(windowmenu,text="POS Friends Pizza",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
    framemenu.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    framemenu0 = LabelFrame(framemenu,bg="#4f4e4a",relief=FLAT,bd=0)
    framemenu0.pack(fill=BOTH,expand=True)
    framemenu1 = LabelFrame(framemenu)
    framemenu1.pack(fill=BOTH,expand=True)
    framemenu2 = LabelFrame(framemenu)
    framemenu2.pack(fill=BOTH,expand=True)
    framemenu3 = LabelFrame(framemenu)
    framemenu3.pack(fill=BOTH,expand=True)
    framemenu4 = LabelFrame(framemenu)
    framemenu4.pack(fill=BOTH,expand=True)
    framemenu5 = LabelFrame(framemenu,bg="#4f4e4a",relief=FLAT,bd=0)
    framemenu5.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    ML1=Label(framemenu0, text="POS Friends Pizza",font=en_grande,bg="#4f4e4a",justify=CENTER,fg="#ffffff")
    ML1.pack(in_=framemenu0,side=TOP,fill=BOTH,expand=True)
    canvasMLI1 = Canvas(framemenu1,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI1.pack(in_=framemenu1,side=LEFT)
    imgMLI1 = PhotoImage(file="./img/casa.png")
    Lista_Imagenes.append(imgMLI1)
    canvasMLI1.create_image(0,0, anchor=NW, image=imgMLI1)
    MBP1=Button(framemenu1,text="Pizza de la Casa ($7590)",command=lambda:pizza(1))
    MBP1.pack(in_=framemenu1,side=LEFT,fill=BOTH,expand=True)
    canvasMLI2 = Canvas(framemenu1,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI2.pack(in_=framemenu1,side=LEFT)
    imgMLI2 = PhotoImage(file="./img/napolitana.png")
    Lista_Imagenes.append(imgMLI2)
    canvasMLI2.create_image(0,0, anchor=NW, image=imgMLI2)
    MBP2=Button(framemenu1,text="Pizza Napolitana ($7590)",command=lambda:pizza(2))
    MBP2.pack(in_=framemenu1,side=LEFT,fill=BOTH,expand=True)
    canvasMLI3 = Canvas(framemenu1,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI3.pack(in_=framemenu1,side=LEFT)
    imgMLI3 = PhotoImage(file="./img/hawai.png")
    Lista_Imagenes.append(imgMLI3)
    canvasMLI3.create_image(0,0, anchor=NW, image=imgMLI3)
    MBP3=Button(framemenu1,text="Pizza Hawaiana ($7590)",command=lambda:pizza(3))
    MBP3.pack(in_=framemenu1,side=LEFT,fill=BOTH,expand=True)
    canvasMLI4 = Canvas(framemenu2,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI4.pack(in_=framemenu2,side=LEFT)
    imgMLI4 = PhotoImage(file="./img/salami.png")
    Lista_Imagenes.append(imgMLI4)
    canvasMLI4.create_image(0,0, anchor=NW, image=imgMLI4)
    MBP4=Button(framemenu2,text="Pizza Salami ($7590)",command=lambda:pizza(4))
    MBP4.pack(in_=framemenu2,side=LEFT,fill=BOTH,expand=True)
    canvasMLI5 = Canvas(framemenu2,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI5.pack(in_=framemenu2,side=LEFT)
    imgMLI5 = PhotoImage(file="./img/peppe.png")
    Lista_Imagenes.append(imgMLI5)
    canvasMLI5.create_image(0,0, anchor=NW, image=imgMLI5)
    MBP5=Button(framemenu2,text="Pizza Pepperoni ($7590)",command=lambda:pizza(5))
    MBP5.pack(in_=framemenu2,side=LEFT,fill=BOTH,expand=True)
    canvasMLI6 = Canvas(framemenu2,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI6.pack(in_=framemenu2,side=LEFT)
    imgMLI6 = PhotoImage(file="./img/vegetariana.png")
    Lista_Imagenes.append(imgMLI6)
    canvasMLI6.create_image(0,0, anchor=NW, image=imgMLI6)
    MBP6=Button(framemenu2,text="Pizza Vegetariana ($8090)",command=lambda:pizza(6))
    MBP6.pack(in_=framemenu2,side=LEFT,fill=BOTH,expand=True)
    canvasMLI7 = Canvas(framemenu3,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI7.pack(in_=framemenu3,side=LEFT)
    imgMLI7 = PhotoImage(file="./img/bbq.png")
    Lista_Imagenes.append(imgMLI7)
    canvasMLI7.create_image(0,0, anchor=NW, image=imgMLI7)
    MBP7=Button(framemenu3,text="Pizza Pollo+BBQ ($8090)",command=lambda:pizza(7))
    MBP7.pack(in_=framemenu3,side=LEFT,fill=BOTH,expand=True)
    canvasMLI8 = Canvas(framemenu3,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI8.pack(in_=framemenu3,side=LEFT)
    imgMLI8 = PhotoImage(file="./img/mar.png")
    Lista_Imagenes.append(imgMLI8)
    canvasMLI8.create_image(0,0, anchor=NW, image=imgMLI8)
    MBP8=Button(framemenu3,text="Pizza del Mar ($8090)",command=lambda:pizza(8))
    MBP8.pack(in_=framemenu3,side=LEFT,fill=BOTH,expand=True)
    canvasMLI9 = Canvas(framemenu3,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI9.pack(in_=framemenu3,side=LEFT)
    imgMLI9 = PhotoImage(file="./img/hambur.png")
    Lista_Imagenes.append(imgMLI9)
    canvasMLI9.create_image(0,0, anchor=NW, image=imgMLI9)
    MBP9=Button(framemenu3,text="HamburPizza ($8090)",command=lambda:pizza(9))
    MBP9.pack(in_=framemenu3,side=LEFT,fill=BOTH,expand=True)
    canvasMLI0 = Canvas(framemenu4,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI0.pack(in_=framemenu4,side=LEFT)
    imgMLI0 = PhotoImage(file="./img/arma.png")
    Lista_Imagenes.append(imgMLI0)
    canvasMLI0.create_image(0,0, anchor=NW, image=imgMLI0)
    MBP0=Button(framemenu4,text="Arma tu Pizza! ($9000)",command=lambda:pizza(0))
    MBP0.pack(in_=framemenu4,side=LEFT,fill=BOTH,expand=True)
    canvasMLI01 = Canvas(framemenu4,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI01.pack(in_=framemenu4,side=LEFT)
    imgMLI01 = PhotoImage(file="./img/registradora.png")
    Lista_Imagenes.append(imgMLI01)
    canvasMLI01.create_image(0,0, anchor=NW, image=imgMLI01)
    MBPI=Button(framemenu4, text="Cierre de Caja",command=lambda:cierre_caja())
    MBPI.pack(in_=framemenu4,side=LEFT,fill=BOTH,expand=True)
    canvasMLI02 = Canvas(framemenu4,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
    canvasMLI02.pack(in_=framemenu4,side=LEFT)
    imgMLI02 = PhotoImage(file="./img/cierre.png")
    Lista_Imagenes.append(imgMLI02)
    canvasMLI02.create_image(0,0, anchor=NW, image=imgMLI02)
    MBPB=Button(framemenu4, text="Cerrar Sesión",command=lambda:log_out())
    MBPB.pack(in_=framemenu4,side=LEFT,fill=BOTH,expand=True)
    if tipologeado=="admin":
        canvasMLI03 = Canvas(framemenu5,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
        canvasMLI03.pack(in_=framemenu5,side=LEFT)
        imgMLI03 = PhotoImage(file="./img/reporte.png")
        Lista_Imagenes.append(imgMLI03)
        canvasMLI03.create_image(0,0, anchor=NW, image=imgMLI03)
        MAB1=Button(framemenu5,text="Reporte de Ventas",command=lambda:reporte_ventas())
        MAB1.pack(in_=framemenu5,side=LEFT,fill=BOTH,expand=True)
        canvasMLI04 = Canvas(framemenu5,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
        canvasMLI04.pack(in_=framemenu5,side=LEFT)
        imgMLI04 = PhotoImage(file="./img/pizza.png")
        Lista_Imagenes.append(imgMLI04)
        canvasMLI04.create_image(0,0, anchor=NW, image=imgMLI04)
        MAB2=Button(framemenu5,text="Pizza!",command=lambda:ventana_pizza())
        MAB2.pack(in_=framemenu5,side=LEFT,fill=BOTH,expand=True)
        canvasMLI05 = Canvas(framemenu5,width=120,height=120,bg="#4f4e4a",bd=0,relief=FLAT)      
        canvasMLI05.pack(in_=framemenu5,side=LEFT)
        imgMLI05 = PhotoImage(file="./img/cerrado.png")
        Lista_Imagenes.append(imgMLI05)
        canvasMLI05.create_image(0,0, anchor=NW, image=imgMLI05)
        MAB3=Button(framemenu5,text="Cierre de Local",command=lambda:cierre_local())
        MAB3.pack(in_=framemenu5,side=LEFT,fill=BOTH,expand=True)
    else:
        tipologeado="cajero"

def cierre_caja():
    global windowcierrecaja
    global deposito
    #creamos ventana nueva (emergente)
    windowcierrecaja=Toplevel()
    windowcierrecaja.geometry("400x400")
    windowcierrecaja.title("Cierre de Caja")
    windowcierrecaja.configure(bg="#4f4e4a")
    #creamos el framemenu principal
    framecierrecaja = LabelFrame(windowcierrecaja,text="Cierre de Caja",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
    framecierrecaja.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    framecierrecaja0 = LabelFrame(framecierrecaja,bg="#4f4e4a",relief=FLAT,bd=0)
    framecierrecaja0.pack(fill=BOTH,expand=True)
    framecierrecaja1 = LabelFrame(framecierrecaja)
    framecierrecaja1.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    WCCL1=Label(framecierrecaja0, text="Cierre de caja:")
    WCCL1.pack(in_=framecierrecaja0,side=TOP,fill=BOTH,expand=True)
    WCCL2=Label(framecierrecaja0, text="Ventas del Día:")
    WCCL2.pack(in_=framecierrecaja0,side=TOP,fill=BOTH,expand=True)
    totalventas=str("$" + str(ventas) + " CLP")
    WCCL3=Label(framecierrecaja0, text=totalventas)
    WCCL3.pack(in_=framecierrecaja0,side=TOP,fill=BOTH,expand=True)
    WCCL4=Label(framecierrecaja0, text="Total Gaveta:")
    WCCL4.pack(in_=framecierrecaja0,side=TOP,fill=BOTH,expand=True)
    totalgaveta=str("$" + str(gaveta) + " CLP")
    WCCL5=Label(framecierrecaja0, text=totalgaveta)
    WCCL5.pack(in_=framecierrecaja0,side=TOP,fill=BOTH,expand=True)
    deposito=gaveta-50000
    textdeposito="Debes depositar: $" + str(deposito) + " CLP en el fondo."
    WCCL6=Label(framecierrecaja0, text=textdeposito)
    WCCL6.pack(in_=framecierrecaja0,side=TOP,fill=BOTH,expand=True)
    WCCB1=Button(framecierrecaja1, text="Volver",command=lambda: windowcierrecaja.withdraw())
    WCCB1.pack(in_=framecierrecaja1,side=LEFT,fill=Y,expand=True)
    WCCB2=Button(framecierrecaja1, text="CERRAR CAJA",command=lambda: cerrar_caja())
    WCCB2.pack(in_=framecierrecaja1,side=RIGHT,fill=Y,expand=True)

def cerrar_caja():
    global fondo
    fondo = fondo+deposito
    global ventas
    ventas= int(0)
    global gaveta
    gaveta=int(50000)
    global windowmenu
    windowmenu.withdraw()
    global windowcierrecaja
    windowcierrecaja.withdraw()
    global cajacerrada
    cajacerrada=cajacerrada+1
    log_out()

def reporte_ventas():
    global windowreporte
    #creamos ventana nueva (emergente)
    windowreporte=Toplevel()
    windowreporte.geometry("400x400")
    windowreporte.title("Reporte de Ventas")
    windowreporte.configure(bg="#4f4e4a")
    #creamos el framemenu principal
    framereporte = LabelFrame(windowreporte,text="Reporte de Ventas",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
    framereporte.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    framereporte0 = LabelFrame(framereporte,bg="#4f4e4a",relief=FLAT,bd=0)
    framereporte0.pack(fill=BOTH,expand=True)
    framereporte1 = LabelFrame(framereporte)
    framereporte1.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    WCCL1=Label(framereporte0, text="Reporte de Caja N°1:")
    WCCL1.pack(in_=framereporte0,side=TOP,fill=BOTH,expand=True)
    WCCL2=Label(framereporte0, text="Ventas del Día:")
    WCCL2.pack(in_=framereporte0,side=TOP,fill=BOTH,expand=True)
    totalventas=str("$" + str(ventas) + " CLP")
    WCCL3=Label(framereporte0, text=totalventas)
    WCCL3.pack(in_=framereporte0,side=TOP,fill=BOTH,expand=True)
    WCCL4=Label(framereporte0, text="Total Gaveta:")
    WCCL4.pack(in_=framereporte0,side=TOP,fill=BOTH,expand=True)
    totalgaveta=str("$" + str(gaveta) + " CLP")
    WCCL5=Label(framereporte0, text=totalgaveta)
    WCCL5.pack(in_=framereporte0,side=TOP,fill=BOTH,expand=True)
    deposito=gaveta-50000
    textdeposito="Falta depositar: $" + str(deposito) + " CLP en el fondo."
    WCCL6=Label(framereporte0, text=textdeposito)
    WCCL6.pack(in_=framereporte0,side=TOP,fill=BOTH,expand=True)
    WCCB1=Button(framereporte1, text="Volver",command=lambda: windowreporte.withdraw())
    WCCB1.pack(in_=framereporte1,side=LEFT,fill=BOTH,expand=True)

def cierre_local():
    global windowcierrelocal
    global gif2
    global frames2
    frames2 = [PhotoImage(file='./img/kirbycierre.gif',format = 'gif -index %i' %(i)) for i in range(10)]
    #creamos ventana nueva (emergente)
    windowcierrelocal=Toplevel()
    windowcierrelocal.geometry("600x600")
    windowcierrelocal.title("Cierre de Local")
    windowcierrelocal.configure(bg="#4f4e4a")
    #creamos el framemenu principal
    framecierrelocal = LabelFrame(windowcierrelocal,text="Cierre de Local",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
    framecierrelocal.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    framecierrelocal0 = LabelFrame(framecierrelocal,bg="#4f4e4a",relief=FLAT,bd=0)
    framecierrelocal0.pack(fill=BOTH,expand=True)
    framecierrelocal1 = LabelFrame(framecierrelocal)
    framecierrelocal1.pack(fill=BOTH,expand=True)
    framecierrelocal2 = LabelFrame(framecierrelocal)
    framecierrelocal2.pack(fill=BOTH,expand=True)  
    #empezamos a crear objetos
    gif2= Label(framecierrelocal0)
    gif2.pack(in_=framecierrelocal0,side=TOP,fill=BOTH,expand=True)
    WCCL1=Label(framecierrelocal1, text="Cierre de Local:")
    WCCL1.pack(in_=framecierrelocal1,side=TOP,fill=BOTH,expand=True)
    WCCL2=Label(framecierrelocal1, text="Ventas del Día:")
    WCCL2.pack(in_=framecierrelocal1,side=TOP,fill=BOTH,expand=True)
    totalventas=str("$" + str(ventas) + " CLP")
    WCCL3=Label(framecierrelocal1, text=totalventas)
    WCCL3.pack(in_=framecierrelocal1,side=TOP,fill=BOTH,expand=True)
    WCCL4=Label(framecierrelocal1, text="Total Gaveta:")
    WCCL4.pack(in_=framecierrelocal1,side=TOP,fill=BOTH,expand=True)
    totalgaveta=str("$" + str(gaveta) + " CLP")
    WCCL5=Label(framecierrelocal1, text=totalgaveta)
    WCCL5.pack(in_=framecierrelocal1,side=TOP,fill=BOTH,expand=True)
    deposito=gaveta-50000
    textdeposito="Debería haber: $" + str(fondo+deposito) + " CLP en el fondo."
    WCCL6=Label(framecierrelocal1, text=textdeposito)
    WCCL6.pack(in_=framecierrelocal1,side=TOP,fill=BOTH,expand=True)
    WCCB1=Button(framecierrelocal2, text="Volver",command=lambda: windowcierrelocal.withdraw())
    WCCB1.pack(in_=framecierrelocal2,side=LEFT,fill=BOTH,expand=True)
    WCCB2=Button(framecierrelocal2, text="CERRAR LOCAL",command=lambda: cerrar_local())
    WCCB2.pack(in_=framecierrelocal2,side=RIGHT,fill=Y,expand=True)
    windowcierrelocal.after(0, actualizar2, 0)
    windowcierrelocal.mainloop() 

def cerrar_local():
    sys.exit()

def pizza(numpizza):
    global windowmenu
    global windowpizza
    global CBSiRaw
    global MPE1
    #reducimos ventana login
    windowmenu.withdraw()
    #creamos ventana menu
    windowpizza=Toplevel()
    windowpizza.geometry("900x760")
    windowpizza.title("POS Friends Pizza - Elección de Pizza")
    windowpizza.configure(bg="#2e2d2b")
    #creamos el framemenu principal
    framepizza = LabelFrame(windowpizza,text="POS Friends Pizza",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
    framepizza.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    framepizza0 = LabelFrame(framepizza,bg="#4f4e4a",relief=FLAT,bd=0)
    framepizza0.pack(fill=BOTH,expand=True)
    framepizza1 = LabelFrame(framepizza)
    framepizza1.pack(fill=BOTH,expand=True)
    framepizza2 = LabelFrame(framepizza)
    framepizza2.pack(fill=BOTH,expand=True)
    framepizza3 = LabelFrame(framepizza)
    framepizza3.pack(fill=BOTH,expand=True)
    framepizza4 = LabelFrame(framepizza)
    framepizza4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    MPL1=Label(framepizza0, text="POS Friends Pizza",font=en_grande,bg="#4f4e4a",justify=CENTER,fg="#ffffff")
    MPL1.pack(in_=framepizza0,side=TOP,fill=BOTH,expand=True)
    if numpizza!=0:
        if numpizza==1:
            MPL2=Label(framepizza1, text="Ingredientes Pizza De La Casa:")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="Salsa de tomate, Queso Mozarella y Dulce de Guayaba.")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
            MPL5=Label(framepizza3, text="Confirma elección:")
        elif numpizza==2:
            MPL2=Label(framepizza1, text="Ingredientes Pizza Napolitana:")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="Salsa de tomate, Queso Mozarella, Jamón y Tomates Frescos.")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
            MPL5=Label(framepizza3, text="Confirma elección:")
        elif numpizza==3:
            MPL2=Label(framepizza1, text="Ingredientes Pizza Hawaiana:")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="Salsa de tomate, Queso Mozarella, Jamón y Piña.")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
            MPL5=Label(framepizza3, text="Confirma elección:")
        elif numpizza==4:
            MPL2=Label(framepizza1, text="Ingredientes Pizza Salami:")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="Salsa de tomate, Queso Mozarella, Salami, Aceitunas Negras y Tomates Frescos.")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
            MPL5=Label(framepizza3, text="Confirma elección:")
        elif numpizza==5:
            MPL2=Label(framepizza1, text="Ingredientes Pizza Pepperoni:")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="Salsa de tomate, Queso Mozarella y Pepperoni.")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
            MPL5=Label(framepizza3, text="Confirma elección:")
        elif numpizza==6:
            MPL2=Label(framepizza1, text="Ingredientes Pizza Vegetariana:")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="Salsa de tomate, Queso Mozarella, Choclo, Champiñón y Pimentón.")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
            MPL5=Label(framepizza3, text="Confirma elección:")
        elif numpizza==7:
            MPL2=Label(framepizza1, text="Ingredientes Pizza con Pollo y BBQ:")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="Salsa de tomate, Queso Mozarella, Pollo, Salsa BBQ y Tocino.")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
            MPL5=Label(framepizza3, text="Confirma elección:")
        elif numpizza==8:
            MPL2=Label(framepizza1, text="Ingredientes Pizza del Mar:")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="Salsa de tomate, Queso Mozarella, Atún y Mariscos Surtidos.")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
            MPL5=Label(framepizza3, text="Confirma elección:")
        elif numpizza==9:
            MPL2=Label(framepizza1, text="Ingredientes HamburPizza:")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="Salsa de tomate, Queso Mozarella, Carne de Hamburguesa.")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
            MPL5=Label(framepizza3, text="Confirma elección:")
        else:
            #dificil que ocurra, pero verificamos el caso de error.
            MPL2=Label(framepizza1, text="ERROR")
            MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL3=Label(framepizza1, text="ERROR")
            MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
            MPL4=Label(framepizza2, text="ERROR")
            MPL5=Label(framepizza3, text="ERROR")
            menu_principal()
    else:
        MPL2=Label(framepizza1, text="La pizza incluye 2 ingredientes elegibles, la Salsa de Tomate y el Queso Mozarella son gratis.")
        MPL2.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
        MPL3=Label(framepizza1, text="Elige 2 ingredientes (adicionales $500 c/u):")
        MPL3.pack(in_=framepizza1,side=TOP,fill=BOTH,expand=True)
        framepizza5 = LabelFrame(framepizza1)
        framepizza5.pack(fill=BOTH,expand=True)
        framepizza6 = LabelFrame(framepizza1)
        framepizza6.pack(fill=BOTH,expand=True)
        framepizza7 = LabelFrame(framepizza1)
        framepizza7.pack(fill=BOTH,expand=True)
        framepizza8 = LabelFrame(framepizza1)
        framepizza8.pack(fill=BOTH,expand=True)
        framepizza9 = LabelFrame(framepizza1)
        framepizza9.pack(fill=BOTH,expand=True)
        global varcheckaceitunas
        global checkaceitunas
        varcheckaceitunas = IntVar()
        checkaceitunas = Checkbutton(framepizza1, text="Aceitunas", variable=varcheckaceitunas)
        checkaceitunas.pack(in_=framepizza5,side=LEFT,fill=BOTH,expand=True)
        global varcheckajo
        global checkajo
        varcheckajo = IntVar()
        checkajo = Checkbutton(framepizza1, text="Ajo", variable=varcheckajo)
        checkajo.pack(in_=framepizza5,side=LEFT,fill=BOTH,expand=True)
        global varcheckchampinon
        global checkchampinon
        varcheckchampinon = IntVar()
        checkchampinon = Checkbutton(framepizza1, text="Champiñón", variable=varcheckchampinon)
        checkchampinon.pack(in_=framepizza5,side=LEFT,fill=BOTH,expand=True)
        global varcheckchoclo
        global checkchoclo
        varcheckchoclo = IntVar()
        checkchoclo = Checkbutton(framepizza1, text="Choclo", variable=varcheckchoclo)
        checkchoclo.pack(in_=framepizza6,side=LEFT,fill=BOTH,expand=True)
        global varcheckchoricillo
        global checkchoricillo
        varcheckchoricillo = IntVar()
        checkchoricillo = Checkbutton(framepizza1, text="Choricillo", variable=varcheckchoricillo)
        checkchoricillo.pack(in_=framepizza6,side=LEFT,fill=BOTH,expand=True)
        global varcheckjamon
        global checkjamon
        varcheckjamon = IntVar()
        checkjamon = Checkbutton(framepizza1, text="Jamón", variable=varcheckjamon)
        checkjamon.pack(in_=framepizza6,side=LEFT,fill=BOTH,expand=True)
        global varcheckpalmitos
        global checkpalmitos
        varcheckpalmitos = IntVar()
        checkpalmitos = Checkbutton(framepizza1, text="Palmitos", variable=varcheckpalmitos)
        checkpalmitos.pack(in_=framepizza7,side=LEFT,fill=BOTH,expand=True)
        global varcheckpimenton
        global checkpimenton
        varcheckpimenton = IntVar()
        checkpimenton = Checkbutton(framepizza1, text="Pimentón", variable=varcheckpimenton)
        checkpimenton.pack(in_=framepizza7,side=LEFT,fill=BOTH,expand=True)
        global varcheckpina
        global checkpina
        varcheckpina = IntVar()
        checkpina = Checkbutton(framepizza1, text="Piña", variable=varcheckpina)
        checkpina.pack(in_=framepizza7,side=LEFT,fill=BOTH,expand=True)
        global varcheckpollo
        global checkpollo
        varcheckpollo = IntVar()
        checkpollo = Checkbutton(framepizza1, text="Pollo", variable=varcheckpollo)
        checkpollo.pack(in_=framepizza8,side=LEFT,fill=BOTH,expand=True)
        global varcheckquesoextra
        global checkquesoextra
        varcheckquesoextra = IntVar()
        checkquesoextra = Checkbutton(framepizza1, text="Extra Queso", variable=varcheckquesoextra)
        checkquesoextra.pack(in_=framepizza8,side=LEFT,fill=BOTH,expand=True)
        global varchecksalame
        global checksalame
        varchecksalame = IntVar()
        checksalame = Checkbutton(framepizza1, text="Salami", variable=varchecksalame)
        checksalame.pack(in_=framepizza8,side=LEFT,fill=BOTH,expand=True)
        global varchecktomate
        global checktomate
        varchecktomate = IntVar()
        checktomate = Checkbutton(framepizza1, text="Tomate", variable=varchecktomate)
        checktomate.pack(in_=framepizza9,side=LEFT,fill=BOTH,expand=True)
        global varchecksalsa
        global checksalsa
        varchecksalsa = IntVar()
        checksalsa = Checkbutton(framepizza1, text="Salsa de Tomate", variable=varchecksalsa)
        checksalsa.pack(in_=framepizza9,side=LEFT,fill=BOTH,expand=True)
        checksalsa.select()
        global varcheckqueso
        global checkqueso
        varcheckqueso = IntVar()
        checkqueso = Checkbutton(framepizza1, text="Queso", variable=varcheckqueso)
        checkqueso.pack(in_=framepizza9,side=LEFT,fill=BOTH,expand=True)
        checkqueso.select()
        MPL4=Label(framepizza2, text="Si el cliente desea eliminar un ingrediente, comentar:")
        MPL5=Label(framepizza3, text="Confirma elección:")
    #el vendedor puede ingresar comentarios, ej: "pizza sin queso".
    MPL4.pack(in_=framepizza2,side=TOP,fill=BOTH,expand=True)
    MPE1=Entry(framepizza2)
    MPE1.pack(in_=framepizza2,side=BOTTOM,fill=BOTH,expand=True)
    #el vendedor debe confirmar si no hay problemas en la seleccion.
    MPL5.pack(in_=framepizza3,side=TOP,fill=BOTH,expand=True)
    CBSiRaw = IntVar()
    CBSi = Checkbutton(framepizza3, text="Sí", variable=CBSiRaw)
    CBSi.pack(in_=framepizza3,side=BOTTOM,fill=BOTH,expand=True)
    #boton para enviar a la siguiente funcion (y siguiente ventana).
    MPB1=Button(framepizza4, text="CANCELAR",command=lambda: cancelar("windowpizza"))
    MPB1.pack(in_=framepizza4,side=LEFT,expand=True)
    MPB2=Button(framepizza4, text="Siguiente",command=lambda: adicionales_verifica(numpizza))
    MPB2.pack(in_=framepizza4,side=RIGHT,fill=BOTH,expand=True)

def adicionales(numpizza):
    global windowpizza
    global windowadicionales
    global MAE6
    global MAE2
    global MAE3
    global MAE4
    global MAE5
    global ListaIngredientes
    global strlistaingredientes
    global comment
    if numpizza==0:
        generar_lista_ingredientes()
    else:
        ListaIngredientes = ["",""]
    #reducimos ventana pizza
    windowpizza.withdraw()
    #creamos ventana adicionales
    windowadicionales=Toplevel()
    windowadicionales.geometry("900x760")
    windowadicionales.title("POS Friends Pizza - Elección de Adicionales")
    windowadicionales.configure(bg="#2e2d2b")
    #creamos el framemenu principal
    frameadicionales = LabelFrame(windowadicionales,text="POS Friends Adicionales",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
    frameadicionales.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    frameadicionales0 = LabelFrame(frameadicionales,bg="#4f4e4a",relief=FLAT,bd=0)
    frameadicionales0.pack(fill=BOTH,expand=True)
    frameadicionales1 = LabelFrame(frameadicionales)
    frameadicionales1.pack(fill=BOTH,expand=True)
    frameadicionales2 = LabelFrame(frameadicionales)
    frameadicionales2.pack(fill=BOTH,expand=True)
    frameadicionales3 = LabelFrame(frameadicionales)
    frameadicionales3.pack(fill=BOTH,expand=True)
    frameadicionales4 = LabelFrame(frameadicionales)
    frameadicionales4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    MAL1=Label(frameadicionales0, text="POS Friends Pizza",font=en_grande,bg="#4f4e4a",justify=CENTER,fg="#ffffff")
    MAL1.pack(in_=frameadicionales0,side=TOP,fill=BOTH,expand=True)
    if numpizza!=0:
        if numpizza==1:
            MAL2=Label(frameadicionales1, text="Pizza De La Casa:")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="Salsa de tomate, Queso Mozarella y Dulce de Guayaba.")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="Comentario:")
            MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
        elif numpizza==2:
            MAL2=Label(frameadicionales1, text="Pizza Napolitana:")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="Salsa de tomate, Queso Mozarella, Jamón y Tomates Frescos.")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="Comentario:")
            MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
        elif numpizza==3:
            MAL2=Label(frameadicionales1, text="Pizza Hawaiana:")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="Salsa de tomate, Queso Mozarella, Jamón y Piña.")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="Comentario:")
            MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
        elif numpizza==4:
            MAL2=Label(frameadicionales1, text="Pizza Salami:")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="Salsa de tomate, Queso Mozarella, Salami, Aceitunas Negras y Tomates Frescos.")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="Comentario:")
            MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
        elif numpizza==5:
            MAL2=Label(frameadicionales1, text="Pizza Pepperoni:")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="Salsa de tomate, Queso Mozarella y Pepperoni.")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="Comentario:")
            MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
        elif numpizza==6:
            MAL2=Label(frameadicionales1, text="Pizza Vegetariana:")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="Salsa de tomate, Queso Mozarella, Choclo, Champiñón y Pimentón.")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="Comentario:")
            MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
        elif numpizza==7:
            MAL2=Label(frameadicionales1, text="Pizza con Pollo y BBQ:")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="Salsa de tomate, Queso Mozarella, Pollo, Salsa BBQ y Tocino.")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="Comentario:")
            MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
        elif numpizza==8:
            MAL2=Label(frameadicionales1, text="Pizza del Mar:")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="Salsa de tomate, Queso Mozarella, Atún y Mariscos Surtidos.")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="Comentario:")
            MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
        elif numpizza==9:
            MAL2=Label(frameadicionales1, text="HamburPizza:")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="Salsa de tomate, Queso Mozarella, Carne de Hamburguesa.")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="Comentario:")
            MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
        else:
            #dificil que ocurra, pero verificamos el caso de error.
            MAL2=Label(frameadicionales1, text="ERROR")
            MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL3=Label(frameadicionales1, text="ERROR")
            MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
            MAL4=Label(frameadicionales2, text="ERROR")
            MAL5=Label(frameadicionales3, text="ERROR")
            menu_principal()
    else:
        MAL2=Label(frameadicionales1, text="Arma tu Pizza:")
        MAL2.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
        MAL3=Label(frameadicionales1, text="Ingredientes Elegidos:")
        MAL3.pack(in_=frameadicionales1,side=TOP,fill=BOTH,expand=True)
        MAL4=Label(frameadicionales2, text="Comentario:")
        MAL5=Label(frameadicionales3, text="Adicionales (INGRESAR SOLO NÚMEROS):")
    MAL4.pack(in_=frameadicionales2,side=TOP,fill=BOTH,expand=True)
    MAL5.pack(in_=frameadicionales3,side=TOP,fill=BOTH,expand=True)
    if numpizza==0:
        strlistaingredientes = " ".join([str(elem) for elem in ListaIngredientes])
        MALI=Label(frameadicionales1, text=strlistaingredientes)
        MALI.pack(in_=frameadicionales1,side=BOTTOM,fill=BOTH,expand=True)
    else:
        ListaIngredientes = ["",""]
    rawcomment = MPE1.get()
    comment = str(rawcomment)
    MAE1=Entry(frameadicionales2)
    MAE1.pack(in_=frameadicionales2,side=BOTTOM,fill=BOTH,expand=True)
    MAE1.insert(0,comment)
    MAE1.config(state="readonly")
    frameadicionales5 = LabelFrame(frameadicionales3)
    frameadicionales5.pack(fill=BOTH,expand=True)
    frameadicionales6 = LabelFrame(frameadicionales3)
    frameadicionales6.pack(fill=BOTH,expand=True)
    frameadicionales7 = LabelFrame(frameadicionales3)
    frameadicionales7.pack(fill=BOTH,expand=True)
    frameadicionales8 = LabelFrame(frameadicionales3)
    frameadicionales8.pack(fill=BOTH,expand=True)
    frameadicionales9 = LabelFrame(frameadicionales3)
    frameadicionales9.pack(fill=BOTH,expand=True)
    MAL6=Label(frameadicionales5, text="($"+str(costo_bebida)+") Bebidas:")
    MAL6.pack(in_=frameadicionales5,side=TOP,fill=BOTH,expand=True)
    MAE2=Entry(frameadicionales5)
    MAE2.pack(in_=frameadicionales5,side=BOTTOM,fill=BOTH,expand=True)
    MAE2.insert(0,0)
    MAL7=Label(frameadicionales6, text="($2500) Palitos de Ajo:")
    MAL7.pack(in_=frameadicionales6,side=TOP,fill=BOTH,expand=True)
    MAE3=Entry(frameadicionales6)
    MAE3.pack(in_=frameadicionales6,side=BOTTOM,fill=BOTH,expand=True)
    MAE3.insert(0,0)
    MAL8=Label(frameadicionales7, text="($2500) Palitos de Queso:")
    MAL8.pack(in_=frameadicionales7,side=TOP,fill=BOTH,expand=True)
    MAE4=Entry(frameadicionales7)
    MAE4.pack(in_=frameadicionales7,side=BOTTOM,fill=BOTH,expand=True)
    MAE4.insert(0,0)
    MAL9=Label(frameadicionales8, text="($2000) Nuggets:")
    MAL9.pack(in_=frameadicionales8,side=TOP,fill=BOTH,expand=True)
    MAE5=Entry(frameadicionales8)
    MAE5.pack(in_=frameadicionales8,side=BOTTOM,fill=BOTH,expand=True)
    MAE5.insert(0,0)
    MAL10=Label(frameadicionales9, text="($500) Salsa Adicional:")
    MAL10.pack(in_=frameadicionales9,side=TOP,fill=BOTH,expand=True)
    MAE6=Entry(frameadicionales9)
    MAE6.pack(in_=frameadicionales9,side=BOTTOM,fill=BOTH,expand=True)
    MAE6.insert(0,0)
    #boton para enviar a la siguiente funcion (y siguiente ventana).
    MAB1=Button(frameadicionales4, text="CANCELAR",command=lambda: cancelar("windowadicionales"))
    MAB1.pack(in_=frameadicionales4,side=LEFT,expand=True)
    MAB2=Button(frameadicionales4, text="Siguiente",command=lambda: cobro(numpizza))
    MAB2.pack(in_=frameadicionales4,side=RIGHT,fill=BOTH,expand=True)

def titulo():
    os.system('cls')
    print("\n\n")
    print("\t******************************************************************")
    print("\t***               Jorge Labraña & Juan Pablo Grez              ***")
    print("\t******************************************************************")
    print("\n\n")

def cobro(numpizza):
    global windowcobro
    global windowadicionales
    #reducimos ventana pizza
    windowadicionales.withdraw()
    #creamos ventana adicionales
    windowcobro=Toplevel()
    windowcobro.geometry("900x760")
    windowcobro.title("POS Friends Pizza - Cobro")
    windowcobro.configure(bg="#2e2d2b")
    #creamos el framemenu principal
    framecobro = LabelFrame(windowcobro,text="POS Friends Pizza - Cobro",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
    framecobro.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    framecobro0 = LabelFrame(framecobro,bg="#4f4e4a",relief=FLAT,bd=0)
    framecobro0.pack(fill=BOTH,expand=True)
    framecobro1 = LabelFrame(framecobro)
    framecobro1.pack(fill=BOTH,expand=True)
    framecobro2 = LabelFrame(framecobro)
    framecobro2.pack(fill=BOTH,expand=True)
    framecobro3 = LabelFrame(framecobro)
    framecobro3.pack(fill=BOTH,expand=True)
    framecobro4 = LabelFrame(framecobro)
    framecobro4.pack(fill=BOTH,expand=True)
    framecobro5 = LabelFrame(framecobro)
    framecobro5.pack(fill=BOTH,expand=True)
    framecobro6 = LabelFrame(framecobro)
    framecobro6.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    MCL0=Label(framecobro0, text="POS Friends Pizza",font=en_grande,bg="#4f4e4a",justify=CENTER,fg="#ffffff")
    MCL0.pack(in_=framecobro0,side=TOP,fill=BOTH,expand=True)
    MCL1=Label(framecobro1, text="Estás finalizando una venta por:")
    MCL1.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
    if numpizza==1:
        MCL2=Label(framecobro1, text="Una Pizza de la Casa")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        valorpizza=int(7590)
    elif numpizza==2:
        MCL2=Label(framecobro1, text="Una Pizza Napolitana")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        valorpizza=int(7590)
    elif numpizza==3:
        MCL2=Label(framecobro1, text="Una Pizza Hawaiana")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        valorpizza=int(7590)
    elif numpizza==4:
        MCL2=Label(framecobro1, text="Una Pizza Salami")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        valorpizza=int(7590)
    elif numpizza==5:
        MCL2=Label(framecobro1, text="Una Pizza Pepperoni")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        valorpizza=int(7590)
    elif numpizza==6:
        MCL2=Label(framecobro1, text="Una Pizza Vegetariana")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        valorpizza=int(8090)
    elif numpizza==7:
        MCL2=Label(framecobro1, text="Una Pizza con Pollo y BBQ")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        valorpizza=int(8090)
    elif numpizza==8:
        MCL2=Label(framecobro1, text="Una Pizza del Mar")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        valorpizza=int(8090)
    elif numpizza==9:
        MCL2=Label(framecobro1, text="Una HamburPizza")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        valorpizza=int(8090)
    elif numpizza==0:
        MCL2=Label(framecobro1, text="Una 'Arma tu Pizza'")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        MCLI = Label(framecobro1, text="Ingredientes pizza:")
        MCLI.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        totalingredientes=int(ingredientes*costo_ingredientes)
        MCLL=Label(framecobro1, text=strlistaingredientes)
        MCLL.pack(in_=framecobro1,side=BOTTOM,fill=BOTH,expand=True)
        if (totalingredientes<=costo_ingredientes*2):
            valorpizza=int(9000)
        else:
            valorpizza=int(9000+int(costo_ingredientes*ingredientes-int(costo_ingredientes*2)))
    else:
        #posible caso de error
        TitleCobro2=Label(framecobro1, text="ERROR")
        MCL2.pack(in_=framecobro1,side=TOP,fill=BOTH,expand=True)
        ventanacobro.withdraw()
        menu_principal()
    MCL3=Label(framecobro2, text="Comentario cliente: ")
    MCL3.pack(in_=framecobro2,side=TOP,fill=BOTH,expand=True)
    MCE1=Entry(framecobro2)
    MCE1.pack(in_=framecobro2,side=BOTTOM,fill=BOTH,expand=True)
    MCE1.insert(0,comment)
    MCE1.config(state="readonly")
    MCL4=Label(framecobro3, text="Adicionales:")
    MCL4.pack(in_=framecobro3,side=TOP,fill=BOTH,expand=True)
    if (int(MAE2.get())>=0):
        databebidas=int(MAE2.get())
    else:
        databebidas=int(0)
    if (int(MAE3.get())>=0):
        datapalitosa=int(MAE3.get())
    else:
        datapalitosa=int(0)
    if (int(MAE4.get())>=0):
        datapalitosq=int(MAE4.get())
    else:
        datapalitosq=int(0)
    if (int(MAE5.get())>=0):
        datanuggets=int(MAE5.get())
    else:
        datanuggets=int(0)
    if (int(MAE6.get())>=0):
        datasalsa=int(MAE6.get())
    else:
        datasalsa=int(0)
    stradicionales="Bebidas: " + str(databebidas) + ". Palitos de Ajo: " + str(datapalitosa) + ". Palitos de Queso: " + str(datapalitosq) + ". Nuggets:" + str(datanuggets) + ". Salsa Adicional: " + str(datasalsa) + "."
    MCL5=Label(framecobro3, text=stradicionales)
    MCL5.pack(in_=framecobro3,side=BOTTOM,fill=BOTH,expand=True)
    MCL6=Label(framecobro4, text="Costo total:")
    MCL6.pack(in_=framecobro4,side=TOP,fill=BOTH,expand=True)
    datatotalcobro=int(valorpizza+int(costo_bebida*databebidas)+int(2500*datapalitosa)+int(2500*datapalitosq)+int(2000*datanuggets)+int(500*datasalsa))
    totalcobro=str("$" + str(datatotalcobro) + " CLP")
    MCL7=Label(framecobro4, text=totalcobro)
    MCL7.pack(in_=framecobro4,side=BOTTOM,fill=BOTH,expand=True)
    MCL8=Label(framecobro5, text="¿Con cuánto paga?")
    MCL8.pack(in_=framecobro5,side=TOP,fill=BOTH,expand=True)
    MCL9=Label(framecobro5, text="(ingrese solo números)")
    MCL9.pack(in_=framecobro5,side=TOP,fill=BOTH,expand=True)
    MCE2=Entry(framecobro5)
    MCE2.pack(in_=framecobro5,side=BOTTOM,fill=BOTH,expand=True)
    #boton para enviar a la siguiente funcion (y siguiente ventana).
    MCB1=Button(framecobro6, text="CANCELAR",command=lambda: cancelar("windowcobro"))
    MCB1.pack(in_=framecobro6,side=LEFT,expand=True)
    MCB2=Button(framecobro6, text="Finalizar Venta",command=lambda: cierre_gaveta(datatotalcobro,MCE2))
    MCB2.pack(in_=framecobro6,side=RIGHT,fill=BOTH,expand=True)

def cierre_gaveta(totalcobro,MCE2):
    global gaveta
    global ventas
    global windowgaveta
    #creamos ventana nueva (emergente)
    windowgaveta=Toplevel()
    windowgaveta.geometry("400x400")
    windowgaveta.title("POS Friends Pizza - Finalizar")
    windowgaveta.configure(bg="#2e2d2b")
    #creamos el framemenu principal
    framegaveta = LabelFrame(windowgaveta,text="POS Friends Pizza - Cobro",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
    framegaveta.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    framegaveta0 = LabelFrame(framegaveta,bg="#4f4e4a",relief=FLAT,bd=0)
    framegaveta0.pack(fill=BOTH,expand=True)
    framegaveta1 = LabelFrame(framegaveta)
    framegaveta1.pack(fill=BOTH,expand=True)
    framegaveta2 = LabelFrame(framegaveta)
    framegaveta2.pack(fill=BOTH,expand=True)
    framegaveta3 = LabelFrame(framegaveta)
    framegaveta3.pack(fill=BOTH,expand=True)
    framegaveta4 = LabelFrame(framegaveta)
    framegaveta4.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    MCL0=Label(framegaveta0, text="POS Friends Pizza",font=en_grande,bg="#4f4e4a",justify=CENTER,fg="#ffffff")
    MCL0.pack(in_=framegaveta0,side=TOP,fill=BOTH,expand=True)
    if MCE2.get():
        if(int(int(MCE2.get())-totalcobro)>=0):
            MCL1=Label(framegaveta1, text="La venta ha sido finalizada.")
            MCL1.pack(in_=framegaveta1,side=TOP,fill=BOTH,expand=True)
            MCL2=Label(framegaveta1, text="Has hecho una venta por:")
            MCL2.pack(in_=framegaveta1,side=TOP,fill=BOTH,expand=True)
            MCL3=Label(framegaveta1, text=totalcobro)
            MCL3.pack(in_=framegaveta1,side=BOTTOM,fill=BOTH,expand=True)
            gaveta = gaveta+totalcobro
            ventas = ventas+totalcobro
            MCL4=Label(framegaveta2, text="Por favor entrega al cliente su vuelto.")
            MCL4.pack(in_=framegaveta2,side=TOP,fill=BOTH,expand=True)
            MCL5=Label(framegaveta2, text="Vuelto:")
            MCL5.pack(in_=framegaveta2,side=TOP,fill=BOTH,expand=True)
            datavuelto=int(int(MCE2.get())-totalcobro)
            totalvuelto=str("$" + str(datavuelto) + " CLP")
            MCL6=Label(framegaveta2, text=totalvuelto)
            MCL6.pack(in_=framegaveta2,side=BOTTOM,fill=BOTH,expand=True)
            MCL7=Label(framegaveta3, text="No te olvides de cerrar la gaveta!")
            MCL7.pack(in_=framegaveta3,side=TOP,fill=BOTH,expand=True)
            MCB1=Button(framegaveta4, text="Finalizar",command=cierra_todo)
            MCB1.pack(in_=framegaveta4,side=LEFT,fill=BOTH,expand=True)
        else:
            MCL1=Label(framegaveta1, text="ERROR")
            MCL1.pack(in_=framegaveta1,side=TOP,fill=BOTH,expand=True)
            MCL2=Label(framegaveta2,text="El monto con el que paga el cliente")
            MCL2.pack(in_=framegaveta2,side=TOP,fill=BOTH,expand=True)
            MCL3=Label(framegaveta3,text="es menor al total de la compra!")
            MCL3.pack(in_=framegaveta3,side=TOP,fill=BOTH,expand=True)
            MCB1=Button(framegaveta4, text="REINTENTAR",command=lambda: windowgaveta.withdraw())
            MCB1.pack(in_=framegaveta4,side=RIGHT,fill=BOTH,expand=True)
    else:
            MCL1=Label(framegaveta1, text="ERROR")
            MCL1.pack(in_=framegaveta1,side=TOP,fill=BOTH,expand=True)
            MCL2=Label(framegaveta2,text="El monto con el que paga el cliente")
            MCL2.pack(in_=framegaveta2,side=TOP,fill=BOTH,expand=True)
            MCL3=Label(framegaveta3,text="es menor al total de la compra!")
            MCL3.pack(in_=framegaveta3,side=TOP,fill=BOTH,expand=True)
            MCB1=Button(framegaveta4, text="REINTENTAR",command=lambda: windowgaveta.withdraw())
            MCB1.pack(in_=framegaveta4,side=RIGHT,fill=BOTH,expand=True)

def cierra_todo():
    global ListaIngredientes
    global windowagaveta
    global windowcobro
    global ingredientes
    ListaIngredientes = ["",""]
    ingredientes = int(0)
    windowgaveta.withdraw()
    windowcobro.withdraw()
    menu_principal()

def generar_lista_ingredientes():
    global aceitunas
    global ajo
    global champinon
    global choclo
    global choricillo
    global jamon
    global palmitos
    global pimenton
    global pina
    global pollo
    global quesoextra
    global salame
    global tomate
    global queso
    global salsa
    global ingredientes
    global ListaIngredientes
    aceitunas = varcheckaceitunas.get()
    ajo = varcheckajo.get()
    champinon = varcheckchampinon.get()
    choclo = varcheckchoclo.get()
    choricillo = varcheckchoricillo.get()
    jamon = varcheckjamon.get()
    palmitos = varcheckpalmitos.get()
    pimenton = varcheckpimenton.get()
    pina = varcheckpina.get()
    pollo = varcheckpollo.get()
    quesoextra = varcheckquesoextra.get()
    salame = varchecksalame.get()
    tomate = varchecktomate.get()
    queso = varcheckqueso.get()
    salsa = varchecksalsa.get()
    if aceitunas!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Aceitunas")
    if ajo!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Ajo")
    if champinon!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Champinón")
    if choclo!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Choclo")
    if choricillo!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Choricillo")
    if jamon!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Jamón")
    if palmitos!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Palmitos")
    if pimenton!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Pimentón")
    if pina!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Pina")
    if pollo!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Pollo")
    if quesoextra!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Extra Queso")
    if salame!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Salame")
    if tomate!=0:
        ingredientes = ingredientes+1
        ListaIngredientes.append("Tomate")
    if salsa!=0:
        ListaIngredientes.append("Salsa de Tomate")
    if queso!=0:
        ListaIngredientes.append("Queso")

def cancelar(windowget):
    data= windowget+str(".withdraw()")
    exec(data)
    menu_principal()

def adicionales_verifica(numpizza):
    CBSi=CBSiRaw.get()
    if (CBSi==1):
        adicionales(numpizza)
    else:
        windowpizza.withdraw()
        menu_principal()

def ventana_pizza():
    global windowgifpizza
    global frames
    global gif1
    frames = [PhotoImage(file='./img/kirbypizza.gif',format = 'gif -index %i' %(i)) for i in range(11)]
    #creamos ventana nueva (emergente)
    windowgifpizza=Toplevel()
    windowgifpizza.geometry("400x400")
    windowgifpizza.title("PIZZA!!!")
    windowgifpizza.configure(bg="#fca39d")
    #creamos el framemenu principal
    framegifpizza = LabelFrame(windowgifpizza,text="PIZZA!!!!!",bg="#fca39d",labelanchor=N,padx=20,pady=20)
    framegifpizza.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    framegifpizza0 = LabelFrame(framegifpizza,bg="#fca39d",relief=FLAT,bd=0)
    framegifpizza0.pack(fill=BOTH,expand=True)
    framegifpizza1 = LabelFrame(framegifpizza)
    framegifpizza1.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    gif1= Label(framegifpizza0)
    gif1.pack(in_=framegifpizza0,side=TOP,fill=BOTH,expand=True)
    WGPB1=Button(framegifpizza1, text="Volver",command=lambda: windowgifpizza.withdraw())
    WGPB1.pack(in_=framegifpizza1,side=RIGHT,fill=BOTH,expand=True)
    windowgifpizza.after(0, actualizar, 0)
    windowgifpizza.mainloop()    

def actualizar(num):
    frame = frames[num]
    num += 1
    if num>10:
        num = 0
    gif1.configure(image=frame)
    windowgifpizza.after(100, actualizar, num)
    
def actualizar2(num):
    frame = frames2[num]
    num += 1
    if num>9:
        num = 0
    gif2.configure(image=frame)
    windowcierrelocal.after(100, actualizar2, num)

def ventana_error(tipoerror):
    global windowerror
    #creamos ventana nueva (emergente)
    windowerror=Toplevel()
    windowerror.geometry("400x400")
    windowerror.title("Error!")
    windowerror.configure(bg="#4f4e4a")
    #creamos el framemenu principal
    frameerror = LabelFrame(windowerror,text="Error!",bg="#4f4e4a",labelanchor=N,padx=20,pady=20)
    frameerror.pack(fill=BOTH,expand=True,padx=20,pady=20)
    #dividimos en multiples framemenu
    frameerror0 = LabelFrame(frameerror,bg="#4f4e4a",relief=FLAT,bd=0)
    frameerror0.pack(fill=BOTH,expand=True)
    frameerror1 = LabelFrame(frameerror)
    frameerror1.pack(fill=BOTH,expand=True)
    #empezamos a crear objetos
    WEL1=Label(frameerror0, text="ERROR")
    WEL1.pack(in_=frameerror0,side=TOP,fill=BOTH,expand=True)
    WEB1=Button(frameerror1, text="Volver",command=lambda: windowerror.withdraw())
    WEB1.pack(in_=frameerror1,side=RIGHT,fill=X,expand=True)
    if tipoerror=="pin":
        WEL2=Label(frameerror0, text="PIN Incorrecto!")
        WEL2.pack(in_=frameerror0,side=BOTTOM,fill=BOTH,expand=True)
        WEL3=Label(frameerror0, text="Inténtalo nuevamente!")
        WEL3.pack(in_=frameerror0,side=BOTTOM,fill=BOTH,expand=True)
    elif tipoerror=="usuario":
        WEL2=Label(frameerror0, text="USUARIO Incorrecto!")
        WEL2.pack(in_=frameerror0,side=BOTTOM,fill=BOTH,expand=True)
        WEL3=Label(frameerror0, text="Inténtalo nuevamente!")
        WEL3.pack(in_=frameerror0,side=BOTTOM,fill=BOTH,expand=True)

inicio()
