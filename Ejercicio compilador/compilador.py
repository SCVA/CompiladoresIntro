from pila import Pila

from functools import reduce

diccionario=['*','/','+','-','=']
variables = {}
error=[]

def esOperador(diccionario,ch):
    if(len([x for x in diccionario if x==ch])>0):
        return True
    else:
        return False

def verDiccionario(diccionario,ch):
    if(esOperador(diccionario,ch)):
        return True
    elif (ch.isdigit()):
        return True
    elif (ch.isalpha()):
        return True
    else:
        return False

def estaAsignada(variable):
    if (variable in variables):
        return True
    else:
        return False

def analisis(lista):
    for x in lista:
        for ch in x:
            if(not verDiccionario(diccionario,ch)):
                error.append("Error caracter no válido "+ch)
    if (not(len(error)>0)):
        pila= Pila()
        for x in lista:
            if(not(len(error)>0)):
                analisisSintactico(x)
                for ch in x:
                    if(not(len(error)>0)):
                        pila.apilar(ch)
                        if(ch=="="):
                            pila.desapilar()
                        elif((ch.isalpha)and (not(ch.isdigit())) and (not(esOperador(diccionario,ch)))):
                            if(ch==x[len(x)-2]):
                                pila.desapilar()
                                if(len(pila.items)>1):
                                    error.append("Error no hay operador")
                                else:
                                    variables[ch]=pila.desapilar()
                            else:
                                if(estaAsignada(ch)):
                                    pila.desapilar()
                                    pila.apilar(variables[ch])
                                else:
                                    error.append("Error variable inexistente "+ch)
                        elif((len(pila.items)>2)and(esOperador(diccionario,ch))):
                            signo = pila.desapilar()
                            num2 = pila.desapilar()
                            num1 = pila.desapilar()
                            pila.apilar(resolver(num1,num2,signo))
                    else:
                        print(error)
            else:
                print(error)
        print(variables)
    else:   
        print(error)

def evaluar(num1,num2,signo):
    if signo=='+':
        return str(int(num1) + int(num2))
    elif signo=='-':
        return str(int(num1) - int(num2))
    elif signo=='*':
        return str(int(num1) * int(num2))
    elif signo=='/':
        return str(int((int(num1) / int(num2))))
    else:
        return 0
    
               

def resolver(num1,num2,signo):
    if(num1.isdigit())and(num2.isdigit())and(esOperador(diccionario,signo)):
        return evaluar(num1,num2,signo)
    else:
        error.append("Error sintaxis invalida "+num2+" "+signo+" "+num1)
        return 0
           
def analisisSintactico(lista):
    if(esOperador(diccionario,lista[0])):
        error.append("Analisis Sintactico: incorrecto, No puede iniciar con un operador")
    elif(lista[len(lista)-1] != '='):
        error.append("Analisis Sintactico: incorrecto, No hay operaador de igualdad")
    elif(not(lista[len(lista)-2].isalpha())):
        error.append("Analisis Sintactico: incorrecto, No hay variable para asignar valor")
        

a=open("datos.txt",'r')
listaG= [y.split() for y in [x.strip('\n') for x in a.readlines()]]

analisis(listaG)




