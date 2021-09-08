#Área de un rectángulo

def arearect (base,altura):
    area = base * altura
    return area

base = float (input("Dame la base: "))
altura = float (input("Dame la altura: "))
areat = arearect (base,altura)
print ("El área del rectángulo es: ", float(areat))