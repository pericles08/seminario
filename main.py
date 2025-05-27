# hola_mundo.py

# Parte 1: Mensaje inicial
print("Hola mundo")  # Mensaje clásico de inicio

# Parte 2: Función
def saludar(nombre):
    print(f"Hola, {nombre}. Bienvenido a Python.")

# Usamos la función
saludar("Carlos")

# Parte 3: Programación orientada a objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años."

# Creamos una instancia de la clase
persona1 = Persona("VS", 100000)

# Usamos un método de la clase
print(persona1.presentar())
