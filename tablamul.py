#Programa para multiplicar

tabla=int(input("Introduce la tabla de multiplicar:"))
for i in range(1,11):
    resultado = tabla*i
    print (tabla, "*", i, "=", resultado)