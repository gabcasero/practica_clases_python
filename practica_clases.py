#Consigna:

#Realizar un programa que conste de una clase llamada 
# Alumno que tenga como atributos el nombre y la nota del alumno. 
#Definir los métodos para inicializar sus atributos, 
# imprimirlos y mostrar un mensaje con el resultado de la nota 
# y si ha aprobado o no.

class Alumno:
    def __init__(self,nombre,nota): 
        self.nombre = nombre
        self.nota = nota

    def aprobar(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} ha aprobado con una nota de {self.nota}")
        else:
            print(f"El alumno {self.nombre} ha suspendido con una nota de {self.nota}")

alumno1 = Alumno("Lauren", 7)

print(alumno1.aprobar())