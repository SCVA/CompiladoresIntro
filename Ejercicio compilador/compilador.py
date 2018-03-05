from pila import Pila

from functools import reduce

diccionario=['*','/','+','-','=']
def verDiccionario(diccionario,ch):
    if(len([x for x in diccionario if x==ch])>0):
        return True
    elif (ch.isdigit()):
        return True
    elif (ch.isalpha()):
        return True
    else:
        return False


def analisis(lista):
    error=[]
    for x in lista:
        for ch in x:
            if(not verDiccionario(diccionario,ch)):
                error.append("Error caracter no válido "+ch)
    pila= Pila()
    for x in lista:
        for ch in x:
            pila.apilar(ch)
            if(len((pila)>2):
               signo= pila.desapilar()
               if(len([x for x in diccionario if x==signo])>0):
                   
            
            
    print(error)
           
 def analisisSintactico(lista): 
    print "Analisis Sintactico:"
    expresion1 = lista[0]
    print expresion1
    if (expresion1[0] == '*') or (expresion1[0] == '/') or (expresion1[0]== '+') or (expresion1[0] == '-'):
       print "Analisis Sintactico: incorrecto, No puede iniciar con un operador"
    if(expresion1[len(expresion1)-1] != '='):
        print "Analisis Sintactico: incorrecto, No hay operaador de igualdad"
 
    
        

a=open("datos.txt",'r')
listaG= [y.split() for y in [x.strip('\n') for x in a.readlines()]]

analisis(listaG)
analisisSintactico(listaG)




