# Import de os para limpiar la consola con os.system("cls")
import os

# Funcion de para crear un nuevo archivo
def createFile():
    # Nombre del archivo
    print ("Nombre del archivo")
    nameFile = input()
    # Añadir una extension al archivo que se creara
    print ("Nombre de la extension (Ej: txt,py,etc)")
    extensionType = input()
    # Si el nameFile no esta vacio y extensionType igualmente
    if nameFile != "" and extensionType != "":
        # Nombre del archivo concatenado con la extension del archivo (Ej. hola.txt) 
        fileName = nameFile + '.' + extensionType
        # Abre un archivo para escribir, crea el archivo si no existe
        fileCreate = open(fileName,"w+")
        print("archivo creado exitosamente")
        # Para agregar contenido al archivo creado
        print("Desea crear un contenido para el archivo? (Y / N)")
        # La entrada que recibira para la siguiente condicion se pasa a minusculas
        condition = input().lower()
        # Si la tecla es y == si (deseo continuar)
        if condition == "y":
            # Almacenar lo que recibira la entrada con input() para despues crear una condicion
            print("Escribe el contenido (Finaliza el programa con ENTER)")
            content = input()
            # Si el contenido recibido tiene mas de un caracter 
            if content != "":
                # Abre un archivo para agregar, crea el archivo si no existe
                f = open(fileName,"a+")
                # Añade el contenido antes escrito al archivo creado
                f.write(content)
                # Cierre del archivo abierto
                f.close()
                # Limpiar la consola
                os.system("cls")

                print("Contenido agregado, Presiona cualquier tecla para cerrar el programa")
                input()
        else:
            print("Presiona cualquier tecla para cerrar el programa")
            input()
    else:
        print("hay un error: Falto el nombre del archivo o la extension")
# Ejecutar la siguiente funcion
createFile()