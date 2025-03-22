# Ejercicio 1: Fibonacci recursivo

print("Fibonacci")
def fibo(n: int) -> int:
   if n == 0:
      return 0
   if n == 1:
      return 1
   return fibo(n - 1) + fibo(n - 2)

for i in range(5):
   print(fibo(i))

print(" ")

# Ejercicio 2: Sumar los elementos de un arreglo

print("Suma de arrays")

def sumarray(numeros: list, n: int) -> int:
   if n == 0:
      return 0
   return numeros[n-1] + sumarray(numeros, n-1)

numeros = [1,2,3,4,5,6]

print(sumarray(numeros, len(numeros)))

print(" ")

# Realizar multiplicacion a base de sumas:

print("Multiplicacion a base de sumas:")

def multi(a: int, b: int) -> int:
    if b == 0:
       return 0
    if a == 0:
       return 0
    if b > 0:
       return a + multi(a, b - 1)
    return -multi(a, -b)

print(multi(5,5))

print(" ")


#Ejericio 3: Division a base de restas:

print("Divison con restas")

def div(a:int, b: int) -> int:
    if a<b:
        return 0
    return 1 + div(a - b, b)


print (div(50,3))

print(" ")

# Ejercicio 4: triangulo de int:

print("Triangulo de int")

def triangu(n: int, espacio: int = 1):
    if espacio > n:
        return
    for i in range(1, espacio + 1):
        print(i, end="")
    print()
    triangu(n, espacio + 1)

triangu(10)
print(" ")


