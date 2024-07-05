import os
import json
os.system("cls")

def leerARchivoJSon(dir):
    with open(dir,'r') as archivo:
        return json.load(archivo)
    
def guardararchivojson(dir,data):
    with open(dir,'w') as archivo:
        json.dump(data,archivo,indent = 4)

def seleccionarOpcion(maxOpciones):
    while True:
        try:
            opcion = int(input("ingrese una de las opciones del menu>>>"))
            if opcion <1 or opcion > maxOpciones:
                print("intente nuevamente")
            else:
                return opcion
        except:
            print("ingrese nuevamente un valor NUMERICO")

