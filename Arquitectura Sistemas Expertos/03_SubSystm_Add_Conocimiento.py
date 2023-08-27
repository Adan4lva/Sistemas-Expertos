"""
    Adan Alvarez Barajas 20310442

    Subsistema de Adquisición de Conocimiento: Controla
    la incorporación de nuevo conocimiento a la base de datos.
    Evalúa si el conocimiento es nuevo y relevante.
"""

print("\n")

class SubsistemaAdquisicionConocimiento:
    def __init__(self, base_de_conocimiento):
        self.base_de_conocimiento = base_de_conocimiento

    def agregar_nuevo_conocimiento(self, sintoma, enfermedad):
        if sintoma not in self.base_de_conocimiento.obtener_sintomas():
            print(f"Síntoma '{sintoma}' no conocido. Agregando a la base de conocimiento.")
            self.base_de_conocimiento.agregar_sintoma(sintoma)
        self.base_de_conocimiento.agregar_relacion(sintoma, enfermedad)
        print(f"Relación agregada: '{sintoma}' - '{enfermedad}'")

class BaseDeConocimiento:
    def __init__(self):
        self.conocimiento = {}

    def agregar_sintoma(self, sintoma):
        self.conocimiento[sintoma] = []

    def agregar_relacion(self, sintoma, enfermedad):
        if sintoma in self.conocimiento:
            self.conocimiento[sintoma].append(enfermedad)

    def obtener_sintomas(self):
        return list(self.conocimiento.keys())

# Crear una instancia de la Base de Conocimiento
base_de_conocimiento = BaseDeConocimiento()

# Crear una instancia del Subsistema de Adquisición de Conocimiento
subsistema_adquisicion = SubsistemaAdquisicionConocimiento(base_de_conocimiento)

# Agregar nuevo conocimiento
subsistema_adquisicion.agregar_nuevo_conocimiento("síntoma A", "enfermedad X")
subsistema_adquisicion.agregar_nuevo_conocimiento("síntoma B", "enfermedad Y")
subsistema_adquisicion.agregar_nuevo_conocimiento("síntoma A", "enfermedad Z")

# Obtener síntomas y sus relaciones
for sintoma, enfermedades in base_de_conocimiento.conocimiento.items():
    print(f"Síntoma: {sintoma} - Enfermedades relacionadas: {', '.join(enfermedades)}")