def obtener_frecuencias(posts):
    palabras_con_hashtag = []
    for p in posts: 
        palabras = p.split()
        #print(palabras)

        for i in palabras:
            if (i.startswith("#")):
                palabras_con_hashtag.append(i)
    #print(f" Las palabras con hashatg son: {palabras_con_hashtag}")
    frecuencias = {}
    for h in palabras_con_hashtag:
        if (h in frecuencias):
            frecuencias[h] += 1
        else:
            frecuencias[h] = 1
    #print(frecuencias)
    return frecuencias

def hashtagsTrending(posts):
    frecuencias = obtener_frecuencias(posts)
    texto = ""
    for hashtag, cantidad in frecuencias.items():
        if (cantidad > 1):
            texto += f"\n {hashtag}: {cantidad}"
    return texto

def hashtagsUnicos(posts):
    frecuencias = obtener_frecuencias(posts)
    return len(frecuencias)