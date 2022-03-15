##Alyx N. Gutierrez Miranda A01640585 
#Act 3.2 Programando un DFA

from dataclasses import dataclass
from sys import displayhook
from tkinter import E
from tokenize import Comment, Special
from xml.dom.minidom import Element
from numpy import char, character, inner
from pyparsing import Word
import pandas as pd
from IPython.display import display
from io import StringIO


def split(word):
    return [char for char in word]

def isSpecial(character,character2): #Aqui simplemente voy a hacer un monton de ifs para confirmar si es alguno de los caracteres especiales dentro del lenguaje 
    if(character=='='):
        return "Asignacion"
    elif(character=='*'):
        return "Multiplicacion"
    elif(character=='('):
        return "Parentesis que abre"
    elif(character==')'):
        return "Parentesis que cierra"
    elif(character=='-'):
        if(isDigit(character2)): #En el caso de la resta esta complicado definir si es una assignaciona resta o un numero negativo, entonces verificaremos que el valor despues no sea un numero
            return "NOTRESTA"
        else:
            return "Resta"
    elif(character=='/'):
        if(character2=='/'):
            return "Comentario"
        else:
            return "Division"
    elif(character=='^'):
        return "Potencia"
    else:
        return False 

def isDigit(character):
    if(character=='.'):
        return True
    elif(character=='E' or character=='e'):
        return True
    try:
        int(character) #Se verifica si el valor es convertible a entero, si no, entonces a float
    except ValueError:
        try:
            float(character) #Si tampoco con float, entonces no es un numero
        except ValueError:
            return False
        return "Real"
    return "Entero"

def isAlpha(character): #Se confirma si es algun tipo de caracter alfanumerico con excepcion a la E
    if(character.isalpha() and character!='E' and character!='e' or character=='_'):
        return True
    else:
        return False

def LexerArimetico(archivo):
    list=[]
    #Se crea un df de pandas para poder posteriormente organizar la informacion dentro de este
    spltstr=split(archivo)
    element=0
    newS=StringIO() #Con la libreria StringIO (para una concatenacion de strings mas sencilla), se crea un string nuevo para los numeros en general para poder asi agrupar a los float
    while element<len(spltstr):
        if(spltstr[element]=='\n' or spltstr[element]==' '): #Si el caracter es un empty string, se ignora
            element+=1
            continue
        elif(isDigit(spltstr[element])!=False):
            while (element<=len(spltstr)-1):
                if(isDigit(spltstr[element])!=False or spltstr[element]=='E'): #Se va a formar un nuevo string mientras haya numeros o nos encontremos con un exponencial
                    newS.write(spltstr[element])
                    element+=1
                else:
                    break
            if(element==len(spltstr)): #Por errores en la compilacion del codigo que se quedaba en un indice fuera de la lista, nose podia obtener el valor para el siguieente if
                element-=1
            if(spltstr[element]!='-'):
                list.append((newS.getvalue(),isDigit(newS.getvalue())))
                element+=1
            else:
                continue
        elif(isAlpha(spltstr[element])):
            newS.seek(0)
            newS.truncate(0)
            list.append((spltstr[element],"Variable"))
            element+=1     
        elif(isSpecial(spltstr[element],spltstr[element+1])!=False):
            special=isSpecial(spltstr[element],spltstr[element+1]) #Si no regresa false, regresa un strirng que agregaremos a la tabla
            if(special=="NOTRESTA"):
                newS.write(spltstr[element])
                element+=1
            elif(special=="Comentario"):
                newS.seek(0)
                newS.truncate(0)
                comment=StringIO()
                while element<len(spltstr):
                    comment.write(spltstr[element]) #Se crea un solo string con lo que queda de toda la linea
                    element+=1
                list.append((comment.getvalue(),special)) 
            else:
                newS.seek(0)
                newS.truncate(0)
                list.append((spltstr[element],special)) 
                element+=1  
    df=pd.DataFrame(list, columns=['Token','Tipo'])
    return df
                 

# MAIN
# Primero el programa recibira como entrada un archivo de texto
with open("entrada.txt","r") as archivo:
    eqs=[]
    for line in archivo:
        eqs.append(line)
#Todas las entradas del archivo de texto, leidas linea por linea se guardan como indices dentro de una lista
#for line in range(len(eqs)):
df=pd.DataFrame()
for i in range(len(eqs)):
    df2=LexerArimetico(eqs[i])
    df=pd.concat([df,df2]  )
display(df)

