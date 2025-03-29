print("ejercicio #1")
print()

class Persona:
    nombre: str
    edad: int
    genero: str

    def __init__(self, nombre: str, edad: int, genero: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} y soy {self.genero}")


persona1 = Persona("David", 18, "Hombre")
persona1.presentarse()

print()
print("Ejercicio #2")
print()

class CuentaBancaria:
    titular: Persona
    saldo: float
    numeroDeCuenta: str

    def __init__(self, titular: Persona, saldo: float, numeroDeCuenta: str) -> None:
        self.titular = titular
        self.saldo = saldo
        self.numeroDeCuenta = numeroDeCuenta

    def depositar (self, cantidad: float):
        self.saldo += cantidad
        print(f"Deposito realizado, saldo actualizado a {self.saldo}")

    def retirar (self, cantidad: float):
        if self.saldo < cantidad:
            print(f"Fondos insuficientes.")
        else: 
            self.saldo -= cantidad
            print(f"Retiro hecho, el saldo actual es de {self.saldo}")

    
    def consultarSaldo (self):
        print(f"Su saldo actual es: {self.saldo}")

    
titular = Persona("David", 19, "hombre")
cuenta = CuentaBancaria(titular,5000, "400081")

cuenta.consultarSaldo()
cuenta.depositar(10000)
cuenta.consultarSaldo()
cuenta.retirar(5000)
cuenta.consultarSaldo()

print()
print("Ejercicio #3")
print()

class Rectangulo:
    base: float
    altura: float

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


rectangulo1 = Rectangulo(10, 5)
print("Área del rectángulo:", rectangulo1.calcular_area())
print("Perímetro del rectángulo:", rectangulo1.calcular_perimetro())

print()
print("Ejercicio #4")
print()

class Circulo:
    radio: float

    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

    def calcular_circunferencia(self):
        return 2 * 3.1416 * self.radio


circulo1 = Circulo(9)
print("Área del círculo:", circulo1.calcular_area())
print("Circunferencia del círculo:", circulo1.calcular_circunferencia())


print()
print("Ejercicio #5")
print()

class Libro:
    titulo: str
    autor: str
    genero: str
    añoDePublicacion: int

    def __init__(self, titulo: str, autor: str, genero: str, añoDePublicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.añoDePublicacion = añoDePublicacion

    def mostrarDetalles(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año: {self.añoDePublicacion}")


libro1 = Libro("Calculo", "Larson", "Ciencias Basicas", 2006)
libro1.mostrarDetalles()

print()
print("Ejercicio #6")
print()

class Cancion:
    titulo: str
    artista: str
    album: str
    duracion: float

    def __init__(self, titulo: str, artista: str, album: str, duracion: float):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproduciendo: {self.titulo} - {self.artista}")


cancion1 = Cancion("Creep", "RadioHead", "Pablo Honey", 3.59)
cancion1.reproducir()

print()
print("Ejercicio #7")
print()

class Producto:
    nombre: str
    precio: float
    cantidadDisponible: int

    def __init__(self, nombre: str, precio: float, cantidadDisponible: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidadDisponible = cantidadDisponible

    def calcularTotal(self, cantidad: int):
        if cantidad > self.cantidadDisponible:
            print("Stock insuficiente.")
            return 0
        return cantidad * self.precio


producto1 = Producto("Pc gamer", 5.400000, 10)
print("Total a pagar:", producto1.calcularTotal(2))

print()
print("Ejercicio #8")
print()

class Estudiante:
    nombre: str
    edad: int
    curso: str
    calificaciones: list

    def __init__(self, nombre: str, edad: int, curso: str):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregar_calificacion(self, calificacion: float):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def determinar_estado(self):
        promedio = self.calcular_promedio()
        return "Aprobado" if promedio >= 3.0 else "Reprobado"


estudiante1 = Estudiante("David",18, "Calculo 2")
estudiante1.agregar_calificacion(3.1)
estudiante1.agregar_calificacion(5.0)
estudiante1.agregar_calificacion(1.9)
print("Promedio:", estudiante1.calcular_promedio())
print("Promedio:", estudiante1.determinar_estado())



