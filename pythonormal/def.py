numeros=list()
contine: bool = True

def agregar (numeros:list):
    numero = int(input("Agrega un numero"))
    numeros.append(numero)
    print(numeros)

def eliminar (numeros:list):
    numeros.pop()

 

while contine == True:
    print("Selecciona que quieres hacer")
    print("1. Agregar Un numero")
    print("2. Eliminar un numero")
    print("3. Salir")



  
    if contine == 1:
      agregar(numeros)

     
    if contine == 2:
      eliminar() 

    
    if contine == 3:
      contine == False

      



