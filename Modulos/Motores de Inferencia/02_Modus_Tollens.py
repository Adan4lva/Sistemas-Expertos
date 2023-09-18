"""
    Adan Alvarez Barajas 20310442

    Se basa en dos premisas, pero su estructura es un poco diferente.
    Se utiliza para llegar a conclusiones negativas o para refutar afirmaciones.
"""

# Premisas
es_un_pajaro = False  # No es un pájaro
premisa1 = es_un_pajaro
premisa2 = False  # No tiene alas si no es un pájaro

# Aplicación del Modus Tollens
if not premisa2:
    if not premisa1:
        conclusion = "No es un pájaro."
    else:
        conclusion = "No podemos determinar si es un pájaro o no."
else:
    conclusion = "No podemos determinar si es un pájaro o no."

# Imprimir la conclusión
print("\n" + conclusion + "\n")
