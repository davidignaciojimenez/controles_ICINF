def convertir_negativo(lista):
    posicion=0
    for x in lista:
        lista.pop(posicion)
        x=x*-1
        lista.insert(posicion,x)
        posicion+=1


lista=[1,2,3,4,5,6,7,8,9,10]
print(f"Lista en positivo: {lista}")
convertir_negativo(lista)
print(f"lista en negativo: {lista}")