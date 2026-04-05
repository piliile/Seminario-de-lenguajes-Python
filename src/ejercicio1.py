# Acá declaramos las funciones
def cantidadLineas(text):
    lineas = text.splitlines()
    numLineas = len(lineas)
    return numLineas

def cantidadPalabras(text):
    palabras = text.split()
    cantPal = len(palabras)
    return cantPal

def promedioPalabras(text):
    promedio = cantidadPalabras(text)/cantidadLineas(text)
    return promedio

def lineasEncimaPromedio(text):
    promedio = promedioPalabras(text)
    lineas = text.splitlines()
    lineasEnProm = [linea for linea in lineas if (len(linea.split()) > promedio)]
    return lineasEnProm