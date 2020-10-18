def factorial(numero):
    if numero==0:
        resultado = 1
        return resultado
    elif numero > 1:
        resultado = numero*factorial(numero-1)
        return resultado
    elif numero == 1:
        return 1
    else:
        return "Operacion invalida"
