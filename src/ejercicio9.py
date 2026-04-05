def cumpleCondiciones(nom, nota):
    if (nom is None) or (nom.strip() == ""):
        return False
    if (nota is None) or not str(nota).isdigit(): # sin el str tira error c el none
        return False
    return True

def armarListadoFinal(students):
    nuevaLista = []
    for d in students:
        nombreEstudiante = d.get("name")
        notaEstudiante = d.get("grade")
        estadoEstudiante = d.get("status")

        if (cumpleCondiciones(nombreEstudiante, notaEstudiante)):
            nombreEstudiante = nombreEstudiante.strip().title()
            estadoEstudiante = estadoEstudiante.strip().title()
            notaEstudiante = int(notaEstudiante)
        
            encontrado = False
            for a in nuevaLista:
                if (a["Nombre"] == nombreEstudiante):
                 encontrado = True
                if (notaEstudiante > a["Nota"]):
                    a["Nota"] = notaEstudiante
                    a["Estado"] = estadoEstudiante
            
            if not encontrado:
                nuevaLista.append(
                    { "Nombre": nombreEstudiante,
                    "Nota": notaEstudiante,
                    "Estado": estadoEstudiante
                    })
    nuevaLista.sort(key = lambda x: x["Nombre"])
    return nuevaLista

