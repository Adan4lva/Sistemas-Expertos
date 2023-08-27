"""
    Adan Alvarez Barajas 20310442

    La Componente Humana: Los expertos humanos aportan el conocimiento básico
    y especializado sobre un tema. Los ingenieros del conocimiento traducen
    este conocimiento en un formato comprensible para el sistema experto.
"""

class ExpertoHumano:
   def obtener_conocimiento(self):
       conocimiento = [
           ("síntoma A", "enfermedad X"),
           ("síntoma B", "enfermedad Y"),
           ("síntoma C", "enfermedad Z"),
       ]
       return conocimiento

class IngenieroConocimiento:
   def traducir_conocimiento(self, conocimiento):
       base_conocimiento = {}
       for sintoma, enfermedad in conocimiento:
           if sintoma in base_conocimiento:
               base_conocimiento[sintoma].append(enfermedad)
           else:
               base_conocimiento[sintoma] = [enfermedad]
       return base_conocimiento

# Simulación de la colaboración
experto = ExpertoHumano()
ingeniero = IngenieroConocimiento()

conocimiento_experto = experto.obtener_conocimiento()
base_de_conocimiento = ingeniero.traducir_conocimiento(conocimiento_experto)

print("\nBase de Conocimiento:")
for sintoma, enfermedades in base_de_conocimiento.items():
   print(f"Síntoma: {sintoma} - Enfermedades: {', '.join(enfermedades)}")