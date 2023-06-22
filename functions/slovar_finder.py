def slovar_find(slovar, a):
    baab = a.capitalize()
    if baab in slovar:
        return slovar[baab]
    else:
        return False
