def tabla_del_5 (tabla=5):
    for i in range (1,11):
       print(tabla,'x',i,'=',tabla*i)
print(tabla_del_5(6))
#nombre de la pelicula, año, lanzamiento 

def datos_pelicula (nombre, año, director ):
    return f"su nombre es {nombre}, el año fue {año}, y su director fue {director}"

print (datos_pelicula("titanic", "1992", "james cameron"))

#(3 valores, suma, promedio, numero mayor 
def operaciones (a,b):
    suma = a+b
    promedio= (a+b)/2
    numero_mayor= f"{a} es mayor a {b}" if a>b else f"{b} es mayor a {a}"
    return suma, promedio, numero_mayor
digitos=operaciones(5,3)
print(digitos)

#argumentos variables 
def sumar_todo(*args):
    total=0
    for numero in args:
        total+=numero
    return total
print(sumar_todo(1,2,3,4))
