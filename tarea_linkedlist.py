#Ejercicio # 1:
print("Ejercicio #1:")
from typing import Optional
from datetime import datetime

class Animal:
    def __init__(self, nombre: str, edad: int, tipo: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
    
        
    def __str__(self):
            return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo: {self.tipo}"

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next: Optional[Nodo] = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza: Optional[Nodo] = None

    def buscar_animal(self, dato) -> bool:
        actual = self.cabeza
        while actual:
            if (actual.dato.nombre == dato.nombre and actual.dato.edad == dato.edad and actual.dato.tipo == dato.tipo):
                return True
            actual = actual.next
        return False
    

    def agregar_animal(self, dato):
        if self.buscar_animal(dato):
            print("El componente ya se encuentra adentro")
            return
        nuevonodo = Nodo(dato)

        if not self.cabeza:
            self.cabeza = nuevonodo
        else: 
            actual = self.cabeza
            while actual.next:
               actual = actual.next
            actual.next = nuevonodo
            
 # Para mostrar de manera iterativa   
    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.next

 # Para mostrar de manera Recursiva           
    def mostrar_animales(self):
        def mostrar_animales_recursivo(nodo: Optional[Nodo]):
             if nodo is None:
                return
             print(nodo.dato)
             mostrar_animales_recursivo(nodo.next)
        
        mostrar_animales_recursivo(self.cabeza)

       




zoo = ListaEnlazada()
zoo.agregar_animal(Animal("Leon", 15, "Felino"))
zoo.agregar_animal(Animal("Paloma", 1, "Ave"))
zoo.agregar_animal(Animal("Lagartija", 3, "Reptil"))

zoo.mostrar_lista()
zoo.mostrar_animales()


# Ejercicio # 2:

print()
print("Ejercicio #2:")


class Tarea:
    def __init__(self, descripcion: str, prioridad: int, fecha_vencimiento: str):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
    
    def __str__(self):
        return (f"Descripción: {self.descripcion}\n"
                f"Prioridad: {self.prioridad}\n"
                f"Vence: {self.fecha_vencimiento}\n"
                "-----------------------------")

class Nodo:
    def __init__(self, tarea: Tarea):
        self.tarea = tarea
        self.next: Optional[Nodo] = None

class ListaTareas:
    def __init__(self):
        self.cabeza: Optional[Nodo] = None
        self.longitud = 0
    
    def agregar_tarea(self, descripcion: str, prioridad: int, fecha_vencimiento: str):
        nuevo_nodo = Nodo(Tarea(descripcion, prioridad, fecha_vencimiento))
        
        actual = self.cabeza
        anterior = None
        

        while actual:
            if actual.tarea.prioridad > prioridad:
                break
            elif actual.tarea.prioridad == prioridad:
                if actual.tarea.fecha_vencimiento > fecha_vencimiento:
                    break
            anterior = actual
            actual = actual.next
        
        if not anterior:
            nuevo_nodo.next = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.next = actual
            anterior.next = nuevo_nodo
        
        self.longitud += 1
    
    def eliminar_por_descripcion(self, descripcion: str) -> bool:
        actual = self.cabeza
        anterior = None
        
        while actual:
            if actual.tarea.descripcion == descripcion:
                if anterior:
                    anterior.next = actual.next
                else:
                    self.cabeza = actual.next
                self.longitud -= 1
                return True
            anterior = actual
            actual = actual.next
        return False
    
    def eliminar_por_posicion(self, posicion: int) -> bool:
        if posicion < 0 or posicion >= self.longitud:
            return False
        
        actual = self.cabeza
        anterior = None
        contador = 0
        
        while contador < posicion:
            anterior = actual
            actual = actual.next
            contador += 1
        
        if anterior:
            anterior.next = actual.next
        else:
            self.cabeza = actual.next
        
        self.longitud -= 1
        return True
    
    def mostrar_tareas(self):
        actual = self.cabeza
        while actual:
            print(actual.tarea)
            actual = actual.next
    
    def buscar_tarea(self, descripcion: str) -> Optional[Tarea]:
        actual = self.cabeza
        while actual:
            if actual.tarea.descripcion == descripcion:
                return actual.tarea
            actual = actual.next
        return None
    
    def marcar_completada(self, descripcion: str) -> bool:
        return self.eliminar_por_descripcion(descripcion)
    

lista = ListaTareas()

lista.agregar_tarea("Comprar pan", 2, "2025-12-01")
lista.agregar_tarea("Hacer examen", 1, "2025-11-15")
lista.agregar_tarea("Ir al médico", 1, "2025-11-10")

lista.mostrar_tareas()

lista.eliminar_por_posicion(0)  
lista.marcar_completada("Hacer examen")
lista.mostrar_tareas()  