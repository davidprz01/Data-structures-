temperature = list()
cont = 0
cantidad = int(input("ingresa cuantas temperaturas vas a registrar"))
for n in range (cantidad):
    temp = int(input("Ingrese la temperatura"))
    temperature.append(temp)
    cont += temp

prom = cont/cantidad
print(prom)
if prom < 20:
    print("Mucho frio")
elif prom > 30:
    print("mucho calor")

# print(temperature)  =>


