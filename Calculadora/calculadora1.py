def suma(x, y):
   return x + y

def resta(x, y):
   return x - y

def multiplica(x, y):
   return x * y

def divide(x, y):
   return x / y

print ("Calculadora basica por Jorge Labraña.")
print ("-----------------------------------------------------")
print ("Primero debes ingresar el operador, selecciona de los siguientes e ingresa el numero correspondiente.")
print("Selecciona operacion.")
print("1.Sumar (+)")
print("2.Restar (-)")
print("3.Multiplicar (*)")
print("4.Dividir (/)")

choice = input("Elige una operacion(1/2/3/4): ")

print ("Ahora se te pediran los valores a calcular, por favor ingresa los numeros cuando se te soliciten")
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

if choice == '1':
   print("El resultado de tu suma de",num1,"+",num2,"es:")
   print(num1,"+",num2,"=", suma(num1,num2))

elif choice == '2':
   print("El resultado de tu resta de",num1,"-",num2,"es:")
   print(num1,"-",num2,"=", resta(num1,num2))

elif choice == '3':
   print("El resultado de tu multiplicacion de",num1,"*",num2,"es:")
   print(num1,"*",num2,"=", multiplica(num1,num2))

elif choice == '4':
   print("El resultado de tu division de",num1,"/",num2,"es:")
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Error de sintaxis, lee bien las instrucciones y vuelve a intentarlo :)")

input("Presiona cualquier tecla para salir ;)")
