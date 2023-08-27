"""
    Adan Alvarez Barajas 20310442

    Interfase de Usuario: Permite la interacción entre el
    sistema experto y los usuarios. Muestra resultados,
    solicita información adicional y permite a los usuarios
    obtener explicaciones.
"""

import tkinter as tk
from tkinter import simpledialog, messagebox

class InterfaseUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto")

        self.resultados_label = tk.Label(root, text="Resultados:")
        self.resultados_label.pack()

        self.resultados_text = tk.Text(root, height=5, width=30)
        self.resultados_text.pack()

        self.solicitar_info_button = tk.Button(root, text="Solicitar Información Adicional", command=self.solicitar_informacion)
        self.solicitar_info_button.pack()

        self.explicacion_button = tk.Button(root, text="Mostrar Explicación", command=self.mostrar_explicacion)
        self.explicacion_button.pack()

    def mostrar_resultados(self, resultados):
        self.resultados_text.delete(1.0, tk.END)  # Limpiar contenido anterior
        for resultado in resultados:
            self.resultados_text.insert(tk.END, resultado + "\n")

    def solicitar_informacion(self):
        informacion = simpledialog.askstring("Solicitar Información", "Por favor, proporcione información adicional:")
        if informacion:
            messagebox.showinfo("Información Adicional", f"Se proporcionó la siguiente información:\n\n{informacion}")

    def mostrar_explicacion(self):
        explicacion = "Las enfermedades inferidas se basan en los síntomas proporcionados por el paciente."
        messagebox.showinfo("Explicación", explicacion)

# Crear una instancia de la Interfase de Usuario
root = tk.Tk()
interfase_usuario = InterfaseUsuario(root)

# Resultados inferidos del Motor de Inferencia
resultados_inferidos = ["Enfermedad X", "Enfermedad Y"]

# Mostrar resultados en la interfaz gráfica
interfase_usuario.mostrar_resultados(resultados_inferidos)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
