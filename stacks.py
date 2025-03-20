from typing import List
#Entendiendo la estructura de un stack con un undo:

# class Stack:
    
#     def __init__(self):
#         self.item = []
#         self.peek = None
    
#     def pushtext(self,dato):
#         self.item.append(dato)
#         print(f"Se ha agregado el elemento: {dato}")

#     def popundo(self):
#         self.peek = self.item[-1]
#         print(f"Undo al elemento {self.peek}")
#         self.item.pop()
#         self.peek = self.item[-1]
#         print(f"Ahora los elementos son: {self.item}")
#         return self.peek
    

#     def __str__(self):
#         return str(self.item)
    


# pila1 = Stack()

# pila1.pushtext(1)
# pila1.pushtext(2)
# pila1.pushtext(3)
# pila1.pushtext(5)
# pila1.popundo()


#Entendiendo el backtracking

laberinto = [ 
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'O', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'O', 'E', 'O'],
    ['X', 'O', 'O', 'O', 'X']
]

inicio = laberinto [0][0]
obstaculo = laberinto["X"]
libre = laberinto ["O"]
salida = laberinto ["E"]

print(libre)


class Stack:
    def __init__(self):
        self.stack = laberinto
        self.peek = laberinto [4][4]
