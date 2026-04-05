def cumple(email):
    if (email.count("@") != 1):
        return False
    posicionArroba = email.find("@")
    antesArroba = email[:posicionArroba] 
    if (len(antesArroba) < 1):
        return False
    despuesArroba = email[posicionArroba+1:] 
    if (despuesArroba.count(".") < 1 ):
        return False
    if (email.startswith("@") or email.endswith("@") or 
        email.startswith(".") or email.startswith(".")):
        return False
    posicionPunto = email.rfind(".")  
    dominio = email[posicionPunto + 1:]
    if len(dominio) < 2:
        return False
    return True # si llega hasta aca es xq no entró en ningun if para retornar false

def validar(email):
    if (cumple(email)):
        return("El email es válido.")
    else:    
        return("El email no es válido.")