import os
import json
import math
import modulos
import random
os.system("cls")

def AsignarValores():
    todosLosProductos = modulos.leerARchivoJSon('productos.json')
    print("CARGANDO VENTAS.....")
    for producto in todosLosProductos:
        producto['precio'] = round(random.randint(20,100) * 100)
        producto['iva'] = round(producto['precio'] * 0.1)

    modulos.guardararchivojson('productos.json', todosLosProductos)
    print("VETNAS CARGADAS :D")

def buscarproductomasalto():
    todosLosProductos = modulos.leerARchivoJSon('productos.json')

    productosOrdenados = sorted( todosLosProductos, key = lambda productos:productos['precio'],reverse = True)

    for productos in productosOrdenados[:1]:
        if productos['precio'] == 0:
            print("si no hay  precio en los productos no puedo hacer nada joven")
        else:
            print("el producto con el precio mas alto es ")
            print("NOMBRE | PRECIO")
            print(f"{productos['nombre']} | {productos['precio']}")

def buscarproductoIVABajo():
    todosLosProductos = modulos.leerARchivoJSon('productos.json')

    productosOrdenados = sorted( todosLosProductos, key = lambda productos:productos['iva'],reverse = True)

    for productos in productosOrdenados[-1:]:
        if productos['iva'] == 0:
            print("si no hay  precio en los productos no puedo hacer nada joven")
        else:
            print("el producto con el iva mas bajo es ")
            print("NOMBRE | iva")
            print(f"{productos['nombre']} | {productos['iva']}")

def promedioPRoductos():
    todosLosProductos = modulos.leerARchivoJSon('productos.json')

    sumaProductos = 0
    cantidadProductos = 0

    for productos in todosLosProductos:
        if productos['precio'] == 0:
            sumaProductos == 0
        else:
            sumaProductos = round(sumaProductos + productos['precio'])
            cantidadProductos = cantidadProductos + 1

    try:
        if sumaProductos == 0:
            promedio = 0
            print("sin el precio en los productos la media geometrica por ende ....")
        else:
            promedio = round(sumaProductos/cantidadProductos)
    except:
        ("el promedio de los productos es 0")
    print(f" el promedio del precio de los productos es {promedio} ")

def mediaGEometrica():
    todosLosProductos = modulos.leerARchivoJSon('productos.json')

    sumaProductos = 0
    cantidadProductos = 0

    for productos in todosLosProductos:
        if productos['precio'] == 0:
            sumaProductos == 0
        else:
            sumaProductos = round(math.log(productos['precio']) + sumaProductos)
            cantidadProductos = cantidadProductos + 1

    try:
        if sumaProductos == 0:
            mediaGeometrica = 0
            print("sin el precio en los productos la media geometrica por ende ....")
        else:
            mediaGeometrica = round(math.exp(sumaProductos/cantidadProductos))
    except:
        ("la media Geometrica de los productos es 0")
    print(f" la media Geometrica del precio de los productos es {mediaGeometrica} ")

