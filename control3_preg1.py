def solo_numeros(var):
    números=("1234567890")
    for x in var:
        if x in números:
            sn=True
        else:
            sn=False
            break
    return sn

var=input("Ingrese una variable: ")
print(solo_numeros(var))