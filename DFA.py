##Alyx N. Gutierrez Miranda A01640585 
#Act 3.2 Programando un DFA

from dataclasses import dataclass
from sys import displayhook
from tkinter import E
from tokenize import Comment, Special
from xml.dom.minidom import Element
from numpy import char, character
from pyparsing import Word
import pandas as pd
from IPython.display import display


def split(word):
    return [char for char in word]

def isSpecial(character,character2): #Aqui simplemente voy a ahcer un monton de ifs para confirmar si es alguno de los caracteres especiales dentro del lenguaje 
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
    try:
        int(character) #Se verifica si el valor es convertible a entero, si no, entonces a float
    except ValueError:
        try:
            float(character) #Si tampoco con float, entonces no es un numero
        except ValueError:
            return False
        return "Real"
    return "Entero"

def isAlpha(character):
    if(character.isalpha() and character!='E'):
        return True
    else:
        return False


def LexerArimetico(archivo):
    df=pd.DataFrame(columns=['Token', 'Tipo'])
    #Se crea un df de pandas para poder posteriormente organizar la informacion dentro de este
    spltstr=split(archivo)
    print(spltstr)
    element=0
    while element<len(spltstr):
        newn=""
        if(spltstr[element]=='\n' or spltstr[element]==''): #Si el caracter es un empty string, se ignora
            element+=1
            continue
        elif(isDigit(spltstr[element])!=False):
            while (isDigit(spltstr[element])!=False) or (spltstr[element]=='E'): #Se va a formar un neuvo string mientras haya numeros o nos encontremos con un exponencial
                newn.join(spltstr[element])
                element+=1
        elif(isAlpha(spltstr[element])):
            #df.append([spltstr[element]],["Variable"]) #Dentro del dataframe asumiendo que cualquier letra menos la E que es utilizada como exponencial se agrega como variable
            df2=pd.DataFrame([[spltstr[element],"Variable"]],columns=['Token','Tipo']) 
            pd.concat([df,df2]) 
            element+=1      
        elif(isSpecial(spltstr[element],spltstr[element+1])!=False):
            special=isSpecial(spltstr[element],spltstr[element+1]) #Si no regresa false, regresa un strirng que agregaremos a la tabla
            if(special=="NOTRESTA"):
                newn.join(spltstr[element])
            elif(special=="Comentario"):
                comment=""
                while element<len(spltstr):
                    comment.join(spltstr[element]) #Se crea un solo string con lo que queda de toda la linea
                    element+=1
                #df.append([comment],[special])
                df2=pd.DataFrame([[comment,special]],columns=['Token','Tipo']) 
                pd.concat([df,df2])  

            else:
                #df.append([spltstr[element]],[special])
                df2=pd.DataFrame([[spltstr[element],special]],columns=['Token','Tipo']) 
                pd.concat([df,df2])  
            element+=1
        element+=1
    display(df)
                 

# MAIN
# Primero el programa recibira como entrada un archivo de texto
with open("entrada.txt","r") as archivo:
    eqs=[]
    for line in archivo:
        eqs.append(line)
#Todas las entradas del archivo de texto, leidas linea por linea se guardan como indices dentro de una lista
print(eqs)
for line in range(len(eqs)):
    LexerArimetico(eqs[line])

