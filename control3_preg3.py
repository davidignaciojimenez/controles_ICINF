def potencia(num,exp):
    if exp>1:
        num=num*(potencia(num,exp-1))
    return num

num=int(input("Ingrese la base: "))
exp=int(input("Ingrese el exponente: "))
print(f"El resultado de los valores ingresados es: {potencia(num,exp)}")