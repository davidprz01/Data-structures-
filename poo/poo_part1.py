class Vehiculo: 
    marca: str
    combustible: int
    cap_gal: int
    tipo: str 
    encendido: bool

    def __init__(self, marca: str, combustible: int, tipo: str, cap_gal: int) -> None:
        self.marca = marca
        self.combustible = combustible
        self.cap_gal = cap_gal
        self.tipo = tipo  
        self.encendido = False  

    def __str__(self) -> str:
        return f"La marca del vehículo es {self.marca}, el nivel de combustible es de {self.combustible} galones y es un {self.tipo}."

    def encender(self):
        if self.combustible < self.cap_gal * 0.1:
            print(f"Gasolina baja en {self.marca} ({self.tipo}), dirígete a la gasolinera más cercana.")
        else:
            self.encendido = True
            print(f"El {self.tipo} {self.marca} ha sido encendido.")

    
    def arrancar(self): 
        if not self.encendido:
            print(f"El {self.tipo} {self.marca} no puede arrancar porque esta bajo de gasolina y no ha encendido")
            return
        
        if self.combustible <= 0:
            print(f"El {self.tipo} {self.marca} se ha quedado sin combustible")
            self.encendido = False
            return
        
        while self.combustible > 0:
            self.combustible -= 1
            print(f"Quedan {self.combustible} de combustible")

            if self.combustible == 0:
                print(f"Te has quedado sin gasolina, el vehiculo no podra encender")
                self.encender = False
            
            if self.combustible < self.cap_gal * 0.1:
                print(f"Conmbustible bajo, dirijete a una gasolineria")



        

class Moto(Vehiculo):
    def __init__(self, marca: str, combustible: int):
        super().__init__(marca, combustible, "moto", 20)

class Carro(Vehiculo):
    def __init__(self, marca: str, combustible: int):
        super().__init__(marca, combustible, "carro", 60)

moto1 = Moto("BMW", 15)
carro1 = Carro("Suzuki", 5)

print(moto1)
print(carro1)

moto1.encender()
moto1.arrancar()

carro1.encender()
carro1.arrancar()