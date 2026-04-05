def todoSegundos(cancion):
    m, s = cancion["duration"].split(":")  # en vez de tener un def todoSegundos, podemos utilizar un lambda pero es menos legible.
    return (int(m)*60) + int(s)

def cancionLarga(playlist):
    canMasLarga = max(playlist, key = todoSegundos)
    return f'"{canMasLarga["title"]}" ({canMasLarga["duration"]})'
    

def cancionCorta(playlist):
    canMasCorta = min(playlist, key = todoSegundos)
    return f'"{canMasCorta["title"]}" ({canMasCorta["duration"]})'

def duracionTot(playlist):
    conviertoASegundos = map(todoSegundos, playlist)
    total = sum(conviertoASegundos)
    return f"{total // 60}m {total % 60}s"