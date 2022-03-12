##Alyx N. Gutierrez Miranda A01640585 
#Act 3.2 Programando un DFA

from dataclasses import dataclass
from tkinter import E
from pyparsing import Word
import pandas as pd


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
            return False
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
    if(character.isalpha()):
        return True
    else:
        return False


def LexerArimetico(archivo):
    data={
    "Token":[],
    "Tipo":[]
    }
    df=pd.DataFrame(data)
    #Se crea un df de pandas para poder posteriormente organizar la informacion dentro de este
    spltstr=split(archivo)
    for element in range(len(spltstr)):
        if(element==' '): #Si el caracter es un empty string, se ignora
            continue
        elif(isAlpha(spltstr[element])):

            df.append([spltstr[element]],["Variable"]) #Dentro del dataframe asumiendo que cualquier letra menos la E que es utilizada como exponencial se agrega como variable
        elif(isDigit(spltstr[element])!=False):
            newn=""
            newn.join(spltstr[element]) #Se va a crear un nuevo string con los numeros
            while isDigit()!=False:
                newn.join(spltstr[element+1])
                
        elif(isSpecial(spltstr[element],spltstr[element+1])):










# MAIN
# Primero el programa recibira como entrada un archivo de texto
with open("entrada.txt","r") as archivo:
    eqs=[]
    for line in archivo:
        eqs.append(line)
#Todas las entradas del archivo de texto, leidas linea por linea se guardan como indices dentro de una lista

