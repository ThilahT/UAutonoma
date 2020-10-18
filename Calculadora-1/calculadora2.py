import os
import operator

def titulo_persistente():
    os.system('cls')
    print("\t**********************************************")
    print("\t***     Calculadora por Jorge Labraña      ***")
    print("\t**********************************************")
    print("\n\n")
    print("Operadores disponibles: suma (+), resta (-), multiplicación (*) y división (/).")
    print("\n\n")
    
def fin_script():
    print ("Presiona cualquier tecla para cerrar...")
    os.system("pause >nul")

OPS = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}
ERROR = lambda arg1, arg2: print("Opearador no reconocido!")

    
def calcular(num1, num2, ope):
    return OPS.get(ope, ERROR)(num1, num2)

def calcular2():
    titulo_persistente()
    user_input=input("Ingresa tu calculo de la siguiente manera: Numero1 Operador Numero2 (Con un espacio entre ellos): ")
    var1, operador, var2=user_input.split()
    if(operador=='/' and var2==0):
        titulo_persistente()
        print("NO EXISTE LA DIVISIÓN ENTRE 0, HUEÓN DE MIERDA!")
        fin_script()
    else:
        titulo_persistente()
        print("El resultado de tu operacion es:")
        print(var1,operador,var2,"=",calcular(float(var1), float(var2), operador))
        fin_script()

def calcular3():
    titulo_persistente()
    user_input=input("Ingresa tu calculo de la siguiente manera: Numero1 Operador Numero2 Operador Numero3 (Con un espacio entre ellos): ")
    var1, operador1, var2, operador2, var3=user_input.split()
    if(operador1=='/' and var2==0 or operador2=='/' and var3==0):
        titulo_persistente()
        print("NO EXISTE LA DIVISIÓN ENTRE 0, HUEÓN DE MIERDA!")
    elif((operador2=='*' or operador2=='/') and (operador1=='+' or operador2=='-')):
        titulo_persistente()
        total=calcular(float(var2), float(var3), operador2)
        print("El resultado de tu operacion es:")
        print(var1,operador1,var2,operador2,var3,"=",calcular(float(var1), float(total), operador1))
        fin_script()
    else:
        titulo_persistente()
        total=calcular(float(var1), float(var2), operador1) 
        print("El resultado de tu operacion es:")
        print(var1,operador1,var2,operador2,var3,"=",calcular(float(total), float(var3), operador2))
        fin_script()

def iniciar():
    titulo_persistente()
    cantidad=float(input("¿Cuantos numeros vas a calcular? ( 2 o 3 ) "))
    if(cantidad==2):
        calcular2()
    elif(cantidad==3):
        calcular3()
    else:
        print("SOLO ENTRE 2 O 3! (de momento)")
        iniciar()

iniciar()
