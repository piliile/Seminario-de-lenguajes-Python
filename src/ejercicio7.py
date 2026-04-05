import random

def cumpleCondiciones(nombresParticipantes):
    participantes = nombresParticipantes.split(",")
    if (len(participantes) < 3):
        print("Debe haber al menos 3 participantes.")
        return False
    if (len(participantes) != len(set(participantes))):
        print("No debe haber nombres repetidos.")
        return False
    return True # si llega hasta esta linea es porque cumple las condiciones

def aleatorio(nombresParticipantes):
    participantes = nombresParticipantes.split(",")
    random.shuffle(participantes)
    
    asignaciones = []
    cantidad = len(participantes)
    for i in range(cantidad-1):
        x = participantes[i]
        y = participantes[i+1]
        asignaciones.append(f"{x} --> {y}")
    ultimo = participantes[-1]
    primero = participantes[0]
    asignaciones.append(f"{ultimo} --> {primero}")
    return asignaciones

def asignarParticipantes(nombresParticipantes):
    if (cumpleCondiciones(nombresParticipantes)):
        return aleatorio(nombresParticipantes)
    else:    
        print("No cumple las condiciones.")