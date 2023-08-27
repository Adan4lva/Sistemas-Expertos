"""
    Adan Alvarez Barajas 20310442

    El Subsistema de Ejecución de Órdenes: Actúa sobre las
    conclusiones del motor de inferencia, iniciando acciones
    basadas en el conocimiento del sistema.
"""

print("\n")

class SubsistemaEjecucionOrdenes:
    def __init__(self, base_de_conocimiento):
        self.base_de_conocimiento = base_de_conocimiento

    def ejecutar_acciones(self, enfermedades):
        for enfermedad in enfermedades:
            acciones = self.base_de_conocimiento.obtener_acciones(enfermedad)
            if acciones:
                print(f"Acciones para la enfermedad '{enfermedad}': {', '.join(acciones)}")
            else:
                print(f"No se encontraron acciones para la enfermedad '{enfermedad}'.")

class BaseDeConocimiento:
    def __init__(self):
        self.conocimiento = {
            "Enfermedad X": ["Tomar medicamento A", "Descansar"],
            "Enfermedad Y": ["Tomar medicamento B", "Beber líquidos"],
        }

    def obtener_acciones(self, enfermedad):
        return self.conocimiento.get(enfermedad, [])

# Crear una instancia de la Base de Conocimiento
base_de_conocimiento = BaseDeConocimiento()

# Crear una instancia del Subsistema de Ejecución de Órdenes
subsistema_ejecucion = SubsistemaEjecucionOrdenes(base_de_conocimiento)

# Enfermedades inferidas del Motor de Inferencia
enfermedades_inferidas = ["Enfermedad X", "Enfermedad Y"]

# Ejecutar acciones basadas en las enfermedades inferidas
subsistema_ejecucion.ejecutar_acciones(enfermedades_inferidas)