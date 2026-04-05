def esSpoiler(p):
    return "*" * len(p)

def censurarSpoiler(review, palabras_spoiler):
    lista_palabras_spoiler = [s.strip().lower() for s in palabras_spoiler.split(",")]
    palabras = review.split()
    review_sin_spoilers = [esSpoiler(p) if p.strip(".").lower() in lista_palabras_spoiler else p for p in palabras]
    return " ".join(review_sin_spoilers)
    