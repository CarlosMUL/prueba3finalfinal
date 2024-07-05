import os
import json
import modulos
import reportes






def menuEstadisticas():
    print("""
    ------MENU ESTADISTICAS------
        1.- Producto con valor más alto.
        2.- Producto con valor del IVA más bajo.
        3.- Promedio del valor de los productos.
        4.- Media geométrica del valor de los productos
    
    """)

    opcion = modulos.seleccionarOpcion(4)
    if opcion == 1:
        reportes.buscarproductomasalto()
    if opcion == 2:
        reportes.buscarproductoIVABajo()
    if opcion == 3:
        reportes.promedioPRoductos()
    if opcion == 4:
        reportes.mediaGEometrica()

def menuPrincipal():
    print("""
    -----MENU PRINCIPAL-----
    1.- Asignar valor a los productos
    2.- Estadisticas
    3.- Salir del programa

    
    """)

def iniciarPrograma():
    while True:
        menuPrincipal()
        opcion = modulos.seleccionarOpcion(3)

        if opcion == 1:
            reportes.AsignarValores()
        if opcion == 2:
            menuEstadisticas()
        if opcion == 3:
            print("SALIR")
            print(" Y NO VUELVA ._.")
            break

if __name__=="__main__":
    iniciarPrograma()