#Tarjetería Española

def maximo(pliegos,plumones):
    tarjetaxpliego = pliegos * 12
    tarjetasxplumon = plumones * 35
    if tarjetaxpliego > tarjetasxplumon:
        total = tarjetasxplumon
    if tarjetaxpliego < tarjetasxplumon:
        total = tarjetaxpliego
    return total
pliegos = int (input ("Dame la cantidad de pliegos de papel albanene: "))
plumones = int (input ("Dame la cantidad de plumones: "))
tarjetas = maximo(pliegos,plumones)
print ("El número máximo de tarjetas que se pueden hacer es: ", int(tarjetas))
