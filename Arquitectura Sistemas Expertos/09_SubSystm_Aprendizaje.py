"""
    Adan Alvarez Barajas 20310442

    El Subsistema de Aprendizaje: Permite al sistema experto
    aprender de nuevos datos y mejorar su capacidad con el tiempo.
    Puede incluir aprendizaje estructural y paramétrico.
"""

print("\n")

class SubsistemaAprendizaje:
    def __init__(self, base_de_conocimiento):
        self.base_de_conocimiento = base_de_conocimiento

    def aprender_de_nuevos_datos(self, nuevos_datos):
        for dato in nuevos_datos:
            sintoma, enfermedad = dato
            self.base_de_conocimiento.agregar_relacion(sintoma, enfermedad)
        print("El sistema experto ha aprendido de nuevos datos.")

class BaseDeConocimiento:
    def __init__(self):
        self.conocimiento = {}

    def agregar_relacion(self, sintoma, enfermedad):
        if sintoma in self.conocimiento:
            self.conocimiento[sintoma].append(enfermedad)
        else:
            self.conocimiento[sintoma] = [enfermedad]

# Crear una instancia de la Base de Conocimiento
base_de_conocimiento = BaseDeConocimiento()

# Crear una instancia del Subsistema de Aprendizaje
subsistema_aprendizaje = SubsistemaAprendizaje(base_de_conocimiento)

# Nuevos datos para aprender
nuevos_datos = [("síntoma D", "enfermedad X"), ("síntoma E", "enfermedad Y")]

# Aprender de los nuevos datos
subsistema_aprendizaje.aprender_de_nuevos_datos(nuevos_datos)

# Mostrar las relaciones actualizadas en la base de conocimiento
for sintoma, enfermedades in base_de_conocimiento.conocimiento.items():
    print(f"Síntoma: {sintoma} - Enfermedades relacionadas: {', '.join(enfermedades)}")
