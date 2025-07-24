import random
import tkinter as tk
from tkinter import messagebox

def elegir_frase():
    if len(frases) == 5:
        frase_aleatoria = random.choice(frases)
        messagebox.showinfo("Frase Elegida", frase_aleatoria)
    else:
        messagebox.showwarning("Error", "Por favor ingresa 5 frases antes de elegir.")

def agregar_frase():
    frase = entrada.get()
    if frase and len(frases) < 5:
        frases.append(frase)
        entrada.delete(0, tk.END)
    elif len(frases) >= 5:
        messagebox.showwarning("Error", "Ya has ingresado 6 frases.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Selector de Frases")

frases = []

entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=10)

boton_agregar = tk.Button(ventana, text="Agregar Frase", command=agregar_frase)
boton_agregar.pack(pady=5)

boton_elegir = tk.Button(ventana, text="Elegir Frase al Azar", command=elegir_frase)
boton_elegir.pack(pady=5)

ventana.mainloop()
