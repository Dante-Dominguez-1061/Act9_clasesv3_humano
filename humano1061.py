print("Act 9 clase humano")
print("Dante Dominguez Mat: 22308051281061")
# Zona de clases
class Humano1061:
    # Zona de atributos dentro de la clase
    edad = 0
    genero = ""
    estatura = 0.0
    peso = 0
    color_pelo = ""
    color_ojos = ""

    # Zona de funciones dentro de la clase
    def saltar1061(self,n):
        print(f"{n} esta saltando wow")
    def jugar1061(self,n):
        print(f"{n} esta jugando, yo tambien quiero")
    def comer1061(self,n):
        print(f"{n} esta comiendo, que delicia")
    def dormir1061(self,n):
        print(f"{n} esta durmiendo, no hagan ruido\n")

# Zona de creacion de objetos
Dante = Humano1061()
Lesly = Humano1061()
# Zona de usando objetos
print("Resultados para Dante")
print("Atributos\n")
Dante.genero = "Hombre"
Dante.estatura = 1.66
Dante.peso = 50
Dante.color_pelo = "Negro"
Dante.color_ojos = "Negros"

print(f"Genero: {Dante.genero}")
print(f"Estatura: {Dante.estatura}")
print(f"Peso: {Dante.peso}kg")
print(f"Color de pelo: {Dante.color_pelo}")
print(f"Color de ojos: {Dante.color_ojos}\n")

print("Funciones\n")
Dante.saltar1061("Dante")
Dante.jugar1061("Dante")
Dante.comer1061("Dante")
Dante.dormir1061("Dante")

print("Resultados para Lesly")
print("Atributos\n")
Lesly.genero = "Mujer"
Lesly.estatura = 1.50
Lesly.peso = 50
Lesly.color_pelo = "Cafe"

print(f"Genero: {Lesly.genero}")
print(f"Estatura: {Lesly.estatura}")
print(f"Peso: {Lesly.peso}kg")
print(f"Color de pelo: {Lesly.color_pelo}\n")

print("Funciones\n")
Lesly.saltar1061("Lesly")
Lesly.jugar1061("Lesly")
Lesly.comer1061("Lesly")