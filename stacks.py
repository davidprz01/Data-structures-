from typing import List

class Stack:
    def __init__(self):
        self.stack: List[List[str]] = []
    
    def push(self, item: List[str]) -> None:
        self.stack.append(item)
    
    def pop(self) -> List[int]:
        return self.stack.pop()
    
    def IsEmpty(self) -> bool:
        return len(self.stack) == 0
    
    def top(self) -> List[int]:
        if not self.IsEmpty():
            self.stack [-1]
        else:
            None

def validacionp (x: int, y: int, lab: List[List[str]]) :
    return 0 <= x < len(lab) and 0 <= y < len(lab[0]) and lab[x][y] in ["O", "E"]

lab = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

x = 0
y = 0


encontro_s = False 

for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == "S":
         x,y = i, j
         encontro_s = True
         break
    if encontro_s == True:
        print(f"El inicio esta en {x,y}")
        break

if encontro_s == False:
    print("No hay inicio en este laberinto")

# encontro_e = False


# for i in range(len(lab)):
#     for j in range(len(lab[i])):
#         if lab[i][j] == "E":
#          x,y = i, j
#          encontro_e = True
#          break
#     if encontro_e == True:
#         print(f"El Final esta en {x,y}")
#         break


stack = Stack()
stack.push([x,y])

contador = 0

while not stack.IsEmpty():
    x,y = stack.pop()
    contador += 1
    print(f"El elemento actual es: {x,y}")

    if lab[x][y] == "E":
        print(f"salida: {x,y}")
        break

    if lab[x][y] == "X":
        continue

    if lab[x][y] == "O":
        lab[x][y] = "Visitado"
    
    if validacionp(x + 1,y, lab):
        stack.push([x + 1, y])
        
    if validacionp(x,y + 1, lab):
        stack.push([x, y + 1])

    if validacionp(x - 1,y, lab): 
        stack.push([x - 1, y])

    if validacionp(x,y-1, lab): 
        stack.push([x,y -1])

    
    

