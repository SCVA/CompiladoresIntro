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
    a=len(lista)
    cont=0
    op=0
    
    while a>0:
        expresion=lista[cont]
        print expresion
        op=0; 
        if (expresion[0] == '*') or (expresion[0] == '/') or (expresion[0]== '+') or (expresion[0] == '-'):
            print "Analisis Sintactico: incorrecto, No puede iniciar con un operador"
        if(expresion[len(expresion)-1] != '='):
            print "Analisis Sintactico: incorrecto, No hay operaador de igualdad"
        for x in expresion:
            if (x== '*') or (x == '/') or (x== '+') or (x == '-'):
                op=op+1
            #quiero contar la cantidad de digitos y variables que hayan para verificar que la diferencia entre digitos y operadores sea 1
            #pero ya no alcanzo por hoy:v
        if(op==0):
            print "Analisis Sintactico: incorreco, No hay operadores"  
                      
        a=a-1
        cont=cont+1
        

a=open("datos.txt",'r')
listaG= [y.split() for y in [x.strip('\n') for x in a.readlines()]]

analisis(listaG)
analisisSintactico(listaG)




