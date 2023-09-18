"""
    Adan Alvarez Barajas 20310442

    Es una regla de inferencia que se basa en dos premisas: 
    una condición (antecedente) y una afirmación (consecuente), 
    y permite derivar una conclusión. 
"""

# Premisas
hace_sol = True  # Hace sol
premisa1 = hace_sol
premisa2 = True  # María va al parque si hace sol

# Aplicación del Modus Ponens
if premisa1:
    if premisa2:
        conclusion = "María va al parque."
    else:
        conclusion = "María no va al parque."
else:
    conclusion = "No podemos determinar si María va al parque o no."

# Imprimir la conclusión
print("\n" + conclusion + "\n")
