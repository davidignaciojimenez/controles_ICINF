listadias=["Día 1","Día 2","Día 3","Día 4","Día 5","Día 6","Día 7","Día 8","Día 9","Día 10","Día 11","Día 12","Día 13","Día 14","Día 15"]
listapuntajes=[]
listamayores=[]
listamenores=[]
for q in listadias:
    print(q)
    puntaje=int(input("Ingrese un puntaje: "))
    listapuntajes.append(puntaje)
    if puntaje<60:
        listamenores.append(q)
    else:
        listamayores.append(q)
print(listapuntajes)
print("Puntajes Igual or Mayor a 60: ", listamayores)
print("Puntajes Menores a 60: ", listamenores)