op=0
i=0
lista=[]
op=4
print("Menu:\n")

print("Elija una opcion")
op=int(input("Presione 1 para grabar\nPresiones 2 para buscar\nPresiones 3 para imprimir certificados\nPresiones 4 para salir\n"))

while op!=4:
    if op==1:
        import funciones as fn
        for i in range(2):
            fn.datos()
        print(lista)
    elif op==2:
        buscador=input("Indique el NIF que desea buscar: ")


