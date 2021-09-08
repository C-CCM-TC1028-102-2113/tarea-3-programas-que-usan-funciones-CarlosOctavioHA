#Año bisiesto

def añobisiesto():
    if 0 ==  año % 4:
        print ("Verdadero")
    else:
        if 0== (año % 100) or (año % 400):
            print ("Falso")

año = int(input("Dame el año"))
añobisiesto()
