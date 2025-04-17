# importar libreria
import tkinter as tk
from tkinter import ttk

# funciones

# nota : las funciones deben agregarse antes del codigo pricipal que las manda llamar.
def function_click():
    pass

# inicializar ventana
root = tk.TK() 
root.title("Python-TKinter")
root.resizable(0, 0)

# elementos
label = ttk.Label(root, text="partidos ganados")
# agregar una caja de texto
partidos_ganados = tk.StringVar()


# positions
label.grid(column=0, row=0)

# activar ventana
root.mainloop()


