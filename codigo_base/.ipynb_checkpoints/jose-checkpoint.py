def calc_fa(fr):
    fa = []
    suma_frecuencias = 0
    for elemento in fr:
        suma_frecuencias += elemento
        fa.append(suma_frecuencias)
    return fa