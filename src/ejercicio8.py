def mostrarMensajeCifrado(mensajeUsuario, valor):
    mensajeCifrado = ""
    for caracter in mensajeUsuario:
        if (caracter.isupper()):
            numeroCar = ord(caracter) # si numeroCar = H --> ord(H) = 72
            alfabetoPos = numeroCar - ord('A') # restamos para poder usar el %26
            nuevaPos = (alfabetoPos + valor) % 26 # desplazamiento y rotacion
            caracterCifrado = chr(nuevaPos + ord('A')) # volvemos a ascii y transformamos a letra
            mensajeCifrado += caracterCifrado
        elif (caracter.islower()):
            numeroCar = ord(caracter)
            alfabetoPos = numeroCar - ord('a') 
            nuevaPos = (alfabetoPos + valor) % 26 
            caracterCifrado = chr(nuevaPos + ord('a')) 
            mensajeCifrado += caracterCifrado
        else:
            mensajeCifrado += caracter
    return mensajeCifrado
