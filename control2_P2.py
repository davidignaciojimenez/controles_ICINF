lista=[]
listaeliminados=[]
letraobjetivo="a"
for x in range(7):
    nombre=input("Ingrese un nombre: ")
    if nombre[-1]==letraobjetivo:
         listaeliminados.append(nombre)
    else:
         lista.append(nombre)
print(lista)
print(listaeliminados)