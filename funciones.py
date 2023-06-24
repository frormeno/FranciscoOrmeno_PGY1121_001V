lista=[]
def datos():
        ("Ingrese los siguientes datos: ")
        nif=(input("Ingrese su NIF sin el codigo verificador: "))
        lista.append(nif)
        while len(nif)<8:
            print("El nif debe tener minimo 8 caracteres")
            nif=(input("Ingrese un nif valido: "))
        codVerificador=input("Ingrese el codigo verificador de su NIF: ")
        nombre=input("Ingrese su nombre completo: ")
        edad=int(input("Ingrese su edad"))
        while edad<0:
            print("La edad debe ser mayor a 0")
            edad=int(input("Ingrese una edad valida"))
        return nif, codVerificador, edad,lista


print(lista)