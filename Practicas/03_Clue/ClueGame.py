import random
import tkinter as tk

# Definición de personajes, locaciones y armas
personajes = ["Rojas", "El Doc", "Victor", "Orozco", "Filiberto"]
locaciones = ["Laboratorio", "Cafeteria", "Auditorio", "Colomos", "Edificio B"]
armas = ["Osciloscopio", "Cautín", "Pistola", "Examen", "Silla"]

# Elegir aleatoriamente el culpable, el arma y la locación
culpable = random.choice(personajes)
arma = random.choice(armas)
locacion = random.choice(locaciones)

# Función para adivinar la solución
def verificar_solucion():
    sospechoso = entry_sospechoso.get()
    arma_sospechosa = entry_arma.get()
    lugar_sospechoso = entry_locacion.get()

    if sospechoso == culpable and arma_sospechosa == arma and lugar_sospechoso == locacion:
        resultado_label.config(text="¡Felicidades! Has resuelto el misterio.")
    else:
        resultado_label.config(text="Lo siento, esa no es la solución correcta.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Juego Clue")

# Crear elementos de la interfaz
label_instrucciones = tk.Label(ventana, text="¡¡Mataron a un inocente!! Descubre al culpable, el arma y la locación.")
label_sospechoso = tk.Label(ventana, text="¿Quién es el culpable?")
label_arma = tk.Label(ventana, text="¿Con qué arma?")
label_locacion = tk.Label(ventana, text="¿En qué locación?")
entry_sospechoso = tk.Entry(ventana)
entry_arma = tk.Entry(ventana)
entry_locacion = tk.Entry(ventana)
verificar_button = tk.Button(ventana, text="Verificar", command=verificar_solucion)
resultado_label = tk.Label(ventana, text="")

# Colocar elementos en la ventana
label_instrucciones.pack()
label_sospechoso.pack()
entry_sospechoso.pack()
label_arma.pack()
entry_arma.pack()
label_locacion.pack()
entry_locacion.pack()
verificar_button.pack()
resultado_label.pack()

# Comienza la interfaz gráfica
ventana.mainloop()
