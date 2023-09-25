"""fileName = 'CODIGOS.txt'

with open(fileName) as f_obj:
    lines = f_obj.readlines()
    for line in lines:
        print("'" + line.rstrip() + "',")"""
#Importar librerias
import tkinter as tk
from tkinter import messagebox

def procesar_contratos():
    contratos = txt_contratos.get("1.0", "end-1c").split("\n")
    contratos_procesados = []
    
    for i, contrato in enumerate(contratos):
        contrato = contrato.strip()
        
        if contrato:
            if i == len(contratos) - 1:
                contrato = "'" + contrato + "'"
            else:
                contrato = "'" + contrato + "',"
            
            contratos_procesados.append(contrato)
    
    resultado = "\n".join(contratos_procesados)
    messagebox.showinfo("EXITO AL PROCESAR", f"{len(contratos_procesados)} CONTRATOS PROCESADOS.")    
    # Mostrar el botón para copiar
    copiar_button.pack()
    
    txt_contratos.delete("1.0", "end")
    txt_contratos.insert("1.0", resultado)
    
    # Habilitar el botón de limpiar
    limpiar_button.config(state=tk.NORMAL)    
    # Habilitar el botón de copiar
    copiar_button.config(state=tk.NORMAL)

def copiar_contratos():
    contratos_procesados = txt_contratos.get("1.0", "end-1c")
    window.clipboard_clear()
    window.clipboard_append(contratos_procesados)

def limpiar_texto():
    txt_contratos.delete("1.0", "end")
    # Deshabilitar el botón de limpiar
    limpiar_button.config(state=tk.DISABLED)
    # Deshabilitar el botón de copiar
    copiar_button.config(state=tk.DISABLED)

# Crear la ventana
window = tk.Tk()
window.title("Procesamiento de Contratos")
window.geometry("400x300")
window.resizable(True, True)
window.eval('tk::PlaceWindow . center')
# Crear el Text Area
txt_contratos = tk.Text(window, height=10, width=40)
txt_contratos.pack(pady=10)
# Crear el botón de procesar
btn_procesar = tk.Button(window, text="Procesar Contratos", command=procesar_contratos)
btn_procesar.pack(pady=10)
# Crear el botón para copiar contratos
copiar_button = tk.Button(window, text="COPIAR", command=copiar_contratos, state=tk.DISABLED)
copiar_button.pack(pady=5)
# Crear el botón para limpiar el texto
limpiar_button = tk.Button(window, text="Limpiar", command=limpiar_texto, state=tk.DISABLED)
limpiar_button.pack(pady=5)
# Ajustar el tamaño del Text Area al cambiar el tamaño de la ventana
def resize(event):
    width = window.winfo_width()
    height = window.winfo_height()
    txt_contratos.config(width=int(width/10), height=int(height/30))

window.bind("<Configure>", resize)
# Iniciar el bucle de la ventana
window.mainloop()