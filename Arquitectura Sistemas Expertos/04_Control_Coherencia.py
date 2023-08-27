"""
    Adan Alvarez Barajas 20310442

    Control de la Coherencia: Garantiza que el conocimiento
    en la base de datos sea coherente y no contradictorio.
    Detecta inconsistencias y notifica a los expertos.
"""

print("\n")

class SubsistemaControlCoherencia:
    def __init__(self, base_de_conocimiento):
        self.base_de_conocimiento = base_de_conocimiento

    def verificar_coherencia(self):
        print("Verificando coherencia de la base de conocimiento...")
        inconsistencias = []

        for sintoma, enfermedades in self.base_de_conocimiento.conocimiento.items():
            if len(enfermedades) > 1:
                inconsistencias.append((sintoma, enfermedades))

        if inconsistencias:
            print("Inconsistencias encontradas:")
            for sintoma, enfermedades in inconsistencias:
                print(f"Síntoma '{sintoma}' relacionado con múltiples enfermedades: {', '.join(enfermedades)}")
            print("Notificar a los expertos para resolver las inconsistencias.")
        else:
            print("La base de conocimiento es coherente y no tiene inconsistencias.")

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

# Agregar relaciones a la base de conocimiento
base_de_conocimiento.agregar_relacion("síntoma A", "enfermedad X")
base_de_conocimiento.agregar_relacion("síntoma B", "enfermedad Y")
base_de_conocimiento.agregar_relacion("síntoma A", "enfermedad Z")

# Crear una instancia del Subsistema de Control de la Coherencia
subsistema_control = SubsistemaControlCoherencia(base_de_conocimiento)

# Verificar la coherencia
subsistema_control.verificar_coherencia()
