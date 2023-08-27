"""
    Adan Alvarez Barajas 20310442

    El Motor de Inferencia: Es el núcleo del sistema experto.
    Utiliza el conocimiento almacenado para hacer inferencias
    y tomar decisiones basadas en datos proporcionados.
"""

print("\n")

class MotorDeInferencia:
    def __init__(self, base_de_conocimiento):
        self.base_de_conocimiento = base_de_conocimiento

    def inferir_enfermedades(self, sintomas):
        enfermedades_inferidas = []

        for sintoma in sintomas:
            if sintoma in self.base_de_conocimiento.conocimiento:
                enfermedades_inferidas.extend(self.base_de_conocimiento.conocimiento[sintoma])

        return list(set(enfermedades_inferidas))  # Eliminar duplicados

class BaseDeConocimiento:
    def __init__(self):
        self.conocimiento = {
            "síntoma A": ["enfermedad X"],
            "síntoma B": ["enfermedad Y"],
            "síntoma C": ["enfermedad Z"],
        }

# Crear una instancia de la Base de Conocimiento
base_de_conocimiento = BaseDeConocimiento()

# Crear una instancia del Motor de Inferencia
motor_de_inferencia = MotorDeInferencia(base_de_conocimiento)

# Síntomas del paciente
sintomas_paciente = ["síntoma A", "síntoma C"]

# Inferir enfermedades basadas en los síntomas del paciente
enfermedades_inferidas = motor_de_inferencia.inferir_enfermedades(sintomas_paciente)

if enfermedades_inferidas:
    print(f"Basado en los síntomas proporcionados, las enfermedades inferidas son: {', '.join(enfermedades_inferidas)}")
else:
    print("No se encontraron enfermedades relacionadas con los síntomas proporcionados.")
