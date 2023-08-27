"""
    Adan Alvarez Barajas 20310442

    El Subsistema de Explicación: Proporciona explicaciones a
    los usuarios sobre las decisiones y acciones del sistema
    experto, ayudando a entender el proceso de razonamiento.
"""

print("\n")

class SubsistemaExplicacion:
    def __init__(self, base_de_conocimiento):
        self.base_de_conocimiento = base_de_conocimiento

    def obtener_explicacion(self, enfermedad):
        explicacion = self.base_de_conocimiento.obtener_explicacion(enfermedad)
        if explicacion:
            return explicacion
        else:
            return "No se encontró explicación para esta enfermedad."

class BaseDeConocimiento:
    def __init__(self):
        self.conocimiento = {
            "Enfermedad X": "Las enfermedades X se relacionan con la exposición a alérgenos.",
            "Enfermedad Y": "Las enfermedades Y son causadas por una infección viral.",
        }

    def obtener_explicacion(self, enfermedad):
        return self.conocimiento.get(enfermedad, "")

# Crear una instancia de la Base de Conocimiento
base_de_conocimiento = BaseDeConocimiento()

# Crear una instancia del Subsistema de Explicación
subsistema_explicacion = SubsistemaExplicacion(base_de_conocimiento)

# Enfermedad para la que se solicita una explicación
enfermedad_solicitada = "Enfermedad X"

# Obtener y mostrar explicación para la enfermedad
explicacion_obtenida = subsistema_explicacion.obtener_explicacion(enfermedad_solicitada)
print(f"Explicación para '{enfermedad_solicitada}': {explicacion_obtenida}")