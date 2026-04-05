
def cumpleZona(zona):
    return  (zona == "local") or (zona == "regional") or (zona == "nacional")
     
def calculamosCostoSegunZona(peso, zona):
    if (zona == "local"):
        if (peso < 1):
            return 500
        if (peso >= 1 and peso <= 5):
            return 1000
        if (peso > 5):
            return 2000
    if (zona == "regional"):
        if (peso < 1):
            return 1000
        if (peso >= 1 and peso <= 5):
            return 2500
        if (peso > 5):
            return 5000
    if (zona == "nacional"):
        if (peso < 1):
            return 2000
        if (peso >= 1 and peso <= 5):
            return 4500
        if (peso > 5):
            return 8000

def calcularCosto(peso, zona):
    costoCalculado = 0
    peso = float(peso)
    if (cumpleZona(zona)):
        costoCalculado = calculamosCostoSegunZona(peso, zona)
    else:
        print('Zona inválida.')
        costoCalculado = 0
    return costoCalculado