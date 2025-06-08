import tkinter as tk
from tkinter import ttk
import subprocess


def ejecutar(programa, datos):
    try:
        resultado = subprocess.run([programa], input=datos, text=True, capture_output=True)
        return resultado.stdout.strip()
    except FileNotFoundError:
        return f"No se encontro {programa}"


def ventana_cesar(parent):
    frame = ttk.LabelFrame(parent, text="Cifrado Cesar")
    ttk.Label(frame, text="Clave:").grid(row=0, column=0, sticky="w")
    clave = ttk.Entry(frame, width=10)
    clave.grid(row=0, column=1)

    ttk.Label(frame, text="Texto:").grid(row=1, column=0, sticky="w")
    texto = ttk.Entry(frame, width=40)
    texto.grid(row=1, column=1)

    resultado = ttk.Label(frame, text="")
    resultado.grid(row=3, column=0, columnspan=2)

    def accion():
        datos = f"{clave.get()}\n{texto.get()}\n"
        salida = ejecutar("./cifrado_cesar.exe", datos)
        resultado.config(text=salida)

    ttk.Button(frame, text="Cifrar", command=accion).grid(row=2, column=0, columnspan=2, pady=5)
    return frame


def ventana_vigenere(parent):
    frame = ttk.LabelFrame(parent, text="Cifrado Vigenere")
    ttk.Label(frame, text="Clave:").grid(row=0, column=0, sticky="w")
    clave = ttk.Entry(frame, width=15)
    clave.grid(row=0, column=1)

    ttk.Label(frame, text="Texto:").grid(row=1, column=0, sticky="w")
    texto = ttk.Entry(frame, width=40)
    texto.grid(row=1, column=1)

    resultado = ttk.Label(frame, text="")
    resultado.grid(row=3, column=0, columnspan=2)

    def accion():
        datos = f"{clave.get()}\n{texto.get()}\n"
        salida = ejecutar("./cifrado_vigenere.exe", datos)
        resultado.config(text=salida)

    ttk.Button(frame, text="Cifrar", command=accion).grid(row=2, column=0, columnspan=2, pady=5)
    return frame


def ventana_busqueda(parent):
    frame = ttk.LabelFrame(parent, text="Busqueda Lineal")
    ttk.Label(frame, text="Lista:").grid(row=0, column=0, sticky="w")
    lista = ttk.Entry(frame, width=40)
    lista.grid(row=0, column=1)

    ttk.Label(frame, text="Valor:").grid(row=1, column=0, sticky="w")
    valor = ttk.Entry(frame, width=10)
    valor.grid(row=1, column=1)

    resultado = ttk.Label(frame, text="")
    resultado.grid(row=3, column=0, columnspan=2)

    def accion():
        datos = f"{lista.get()}\n{valor.get()}\n"
        salida = ejecutar("./busqueda_lineal.exe", datos)
        resultado.config(text=salida)

    ttk.Button(frame, text="Buscar", command=accion).grid(row=2, column=0, columnspan=2, pady=5)
    return frame


def ventana_round_robin(parent):
    frame = ttk.LabelFrame(parent, text="Round Robin")
    ttk.Label(frame, text="Duraciones:").grid(row=0, column=0, sticky="w")
    duraciones = ttk.Entry(frame, width=40)
    duraciones.grid(row=0, column=1)

    ttk.Label(frame, text="Quantum:").grid(row=1, column=0, sticky="w")
    quantum = ttk.Entry(frame, width=10)
    quantum.grid(row=1, column=1)

    salida = tk.Text(frame, width=40, height=5)
    salida.grid(row=3, column=0, columnspan=2)

    def accion():
        datos = f"{duraciones.get()}\n{quantum.get()}\n"
        resultado = ejecutar("./round_robin.exe", datos)
        salida.delete(1.0, tk.END)
        salida.insert(tk.END, resultado)

    ttk.Button(frame, text="Simular", command=accion).grid(row=2, column=0, columnspan=2, pady=5)
    return frame


def main():
    root = tk.Tk()
    root.title("Algoritmos en C++ con Tkinter")

    ventana_cesar(root).pack(padx=10, pady=5, fill="x")
    ventana_vigenere(root).pack(padx=10, pady=5, fill="x")
    ventana_busqueda(root).pack(padx=10, pady=5, fill="x")
    ventana_round_robin(root).pack(padx=10, pady=5, fill="x")

    root.mainloop()


if __name__ == "__main__":
    main()
