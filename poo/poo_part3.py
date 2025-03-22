print("Ejercicio #1")
print()

class Empleado:
    nombre: str
    salario: float
    departamento: str

    def __init__(self, nombre: str, salario: float, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        pass


class Gerente(Empleado):
    equipo: list

    def __init__(self, nombre: str, salario: float, departamento: str, equipo: list):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def trabajar(self):
        print(f"{self.nombre} está supervisando al equipo de {len(self.equipo)} empleados")


class Desarrollador(Empleado):
    lenguajeDeProgramacion: str

    def __init__(self, nombre: str, salario: float, departamento: str, lenguajeDeProgramacion: str):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def trabajar(self):
        print(f"{self.nombre} está desarrollando en {self.lenguajeDeProgramacion}")


empleado1 = Gerente("David", 5000, "IT", ["David", "Luis"])
empleado2 = Desarrollador("Andres", 3000, "IT", "Python")

empleado1.trabajar()
empleado2.trabajar()

print()
print("Ejercicio #2")
print()

class FiguraGeometrica:
    def calcular_area(self):
        pass


class Triangulo(FiguraGeometrica):
    base: float
    altura: float

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Cuadrado(FiguraGeometrica):
    lado: float

    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2
    

triangulo1 = Triangulo(6, 12)
cuadrado1 = Cuadrado(5)

print(f"Área del triángulo: {triangulo1.calcular_area()}")
print(f"Área del cuadrado: {cuadrado1.calcular_area()}")

print()
print("Ejercicio #3")
print()

class Electrodomestico:
    marca: str
    modelo: str
    consumoEnergetico: str

    def __init__(self, marca: str, modelo: str, consumoEnergetico: str):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico

    def encender(self):
        pass


class Lavadora(Electrodomestico):
    capacidad: float

    def __init__(self, marca: str, modelo: str, consumoEnergetico: str, capacidad: float):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad

    def encender(self):
        print(f"Lavadora {self.marca} {self.modelo} encendida, iniciando ciclo de lavado")


class Refrigerador(Electrodomestico):
    tieneCongelador: bool

    def __init__(self, marca: str, modelo: str, consumoEnergetico: str, tieneCongelador: bool):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tieneCongelador = tieneCongelador

    def encender(self):
        print(f"Refrigerador {self.marca} {self.modelo} encendido, regulando temperatura")

lavadora1 = Lavadora("Samsung", "X200", "A++", 8)
refrigerador1 = Refrigerador("Samsung", "Frost200", "A+", True)

lavadora1.encender()
refrigerador1.encender()

print()
print("Ejercicio #4")
print()

class Usuario:
    nombreDeUsuario: str
    contraseña: str

    def __init__(self, nombreDeUsuario: str, contraseña: str):
        self.nombreDeUsuario = nombreDeUsuario
        self.contraseña = contraseña

    def iniciar_sesion(self, usuario: str, contraseña: str) -> bool:
        if self.nombreDeUsuario == usuario and self.contraseña == contraseña:
            print("Inicio de sesión exitoso")
            return True
        else:
            print("Usuario y/o contraseña incorrectas")
            return False


class Administrador(Usuario):
    def gestionar_usuarios(self):
        print(f"{self.nombreDeUsuario} está gestionando usuarios")


class Cliente(Usuario):
    def realizar_compra(self, usuario: str, contraseña: str):
        if self.iniciar_sesion(usuario, contraseña):
            print(f"{self.nombreDeUsuario} está realizando una compra")
        else:
            print("No puedes realizar la compra, usuario y/o contraseña incorrectas")


admin1 = Administrador("admin", "1234")
cliente1 = Cliente("user1", "abcd")

if admin1.iniciar_sesion("admin", "1234"):
    admin1.gestionar_usuarios()

cliente1.realizar_compra("user1", "abcd")  
print()
cliente1.realizar_compra("user1", "wrongpass")  




