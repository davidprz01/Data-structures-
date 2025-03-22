hash=dict()
contine: bool = True

def agregar (key:str, value:str):
    hash.update({key:value})
    print(hash)

def eliminar ():
    hash.popitem()
    print(hash)

 

while contine == True:
    print("Selecciona que quieres hacer")
    print("1. Agregar Una persona")
    print("2. Eliminar una persona")
    print("3. Salir")
    
    response = int(input())



  
    if response == 1:
      nombre = str(input("Agrega una persona"))
      agregar("name", nombre)
      print()

     
    if response == 2:
      eliminar() 

    
    if response == 3:
     contine = False

      



