lista=[]
listacantidadcaracteres=[]
listaextra=[]
while True:
    nombre=input("Ingrese un nombre. Si ingresa un nombre en blanco, el bucle termina: ")
    if nombre=="":
        break
    else:
        lista.append(nombre)
print(lista)
for x in lista:
    cantidadcaracteres=0
    for y in x:
        cantidadcaracteres=cantidadcaracteres+1
    listacantidadcaracteres.append(cantidadcaracteres)
listacantidadcaracteres.sort(reverse=True)
print(listacantidadcaracteres[0])