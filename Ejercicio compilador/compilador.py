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
        

a=open("datos.txt",'r')
listaG= [y.split() for y in [x.strip('\n') for x in a.readlines()]]

analisis(listaG)



