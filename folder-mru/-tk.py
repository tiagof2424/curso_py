
import tkinter as tk
def calcular():
    velocidad= entry_velocidad.get()
    movimiento= entry_tiempo.get()
    #op = entry_op.get()
    #r = eval(f"{velocidad}+{op}+{movimiento}")
    distancia =velocidad * movimiento 
    label_result.configure(text=f"result:{distancia}")


#crear ventana 
root = tk.Tk()

# config
root.title("title")
root.minsize(350,250)

#elements

# label
label_title=tk.Label(root,text="calculadora")
label_result=tk.Label(root,text="calculadora")
#texbax
text_velocidad= tk.StringVar()
text_tiempo=tk.StringVar()
#text_op=tk.StringVar()

#Entry
entry_velocidad= tk.Entry(root,width=20,textvariable=text_velocidad) 
entry_tiempo= tk.Entry(root,width=20,textvariable=text_tiempo)
#entry_op= tk.Entry(root,wdite=20,textvariable=text_op)

#Button
button = tk.Button(root, text="calcular",command=calcular)


#positions
label_title.grid(column=0,row=0)
entry_velocidad.grid(column=1,row=1) 
entry_tiempo.grid(column=1,row=2)
button.grid(column=4,row=5)
#entry_op.grid(column=1,row=3)
label_result.grid(column = row)

#iniciar ventana
root.mainloop()

root.mainloop()
