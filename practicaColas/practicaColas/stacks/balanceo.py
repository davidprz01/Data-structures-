class Pila:
    def __init__(self):
        self.simbolos = []  
        self.posiciones = []  

    def push(self, simbolo, posicion):
        self.simbolos.append(simbolo)
        self.posiciones.append(posicion)

    def pop(self):
        if not self.IsEmpty():
            self.posiciones.pop()
            return self.simbolos.pop()
        return ""

    def peek(self):
        return self.simbolos[-1] if not self.IsEmpty() else ""

    def peek_lugar(self):
        return self.posiciones[-1] if not self.IsEmpty() else -1

    def IsEmpty(self) -> bool:
        return len(self.simbolos) == 0
    


def verificar_balanceo(expresion):
    pila = Pila()
    errores = []
    pares = {')': '(', '}': '{', ']': '['}  

    posicion = 0  
    for caracter in expresion:

        if caracter in "({[":
            pila.push(caracter, posicion)  

        elif caracter in ")}]":

            if pila.IsEmpty():
                errores.append(f"Error: '{caracter}' en posición {posicion} sin apertura.")
            else:
                simbolo_tope = pila.pop()
                posicion_tope = pila.peek_lugar()

                if pares[caracter] != simbolo_tope:
                    errores.append(f"Error: '{caracter}' en posición {posicion} no coincide con '{simbolo_tope}' en {posicion_tope}.")
        posicion += 1  



    while not pila.IsEmpty():
        errores.append(f"Error: '{pila.pop()}' en posición {pila.peek_lugar()} sin cierre.")

    return errores if errores else ["Expresión balanceada."]


expresion = "{[()]}(){}["
resultado = verificar_balanceo(expresion)


for mensaje in resultado:
    print(mensaje)
