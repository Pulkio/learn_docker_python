import tkinter as tk
from tkinter import ttk

def launch_app():
    root = tk.Tk()
    root.title("Mon Application de Bureau")

    # Fenêtre principale
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Exemple de widget
    ttk.Label(mainframe, text="Hello, Docker!").grid(column=1, row=1, sticky=tk.W)

    # Démarrer la boucle principale de l'interface graphique
    root.mainloop()

