"""
    Adan Alvarez Barajas 20310442

    La Base de Conocimiento: Es donde se almacena el conocimiento capturado
    de los expertos. Incluye reglas, relaciones y distribuciones de
    probabilidad que el sistema utiliza para hacer inferencias.
"""

class BaseDeConocimiento:
    def __init__(self):
        self.conocimiento = {}

    def agregar_relacion(self, sintoma, enfermedad):
        if sintoma in self.conocimiento:
            self.conocimiento[sintoma].append(enfermedad)
        else:
            self.conocimiento[sintoma] = [enfermedad]

    def obtener_enfermedades(self, sintoma):
        if sintoma in self.conocimiento:
            return self.conocimiento[sintoma]
        else:
            return []

# Crear una instancia de la Base de Conocimiento
base_de_conocimiento = BaseDeConocimiento()

# Agregar relaciones entre síntomas y enfermedades
base_de_conocimiento.agregar_relacion("síntoma A", "enfermedad X")
base_de_conocimiento.agregar_relacion("síntoma B", "enfermedad Y")
base_de_conocimiento.agregar_relacion("síntoma A", "enfermedad Z")

# Obtener enfermedades relacionadas con un síntoma
sintoma_buscado = "síntoma A"
enfermedades_relacionadas = base_de_conocimiento.obtener_enfermedades(sintoma_buscado)

if enfermedades_relacionadas:
    print(f"\nLas enfermedades relacionadas con '{sintoma_buscado}' son: {', '.join(enfermedades_relacionadas)}")
else:
    print(f"No se encontraron enfermedades relacionadas con '{sintoma_buscado}'.")