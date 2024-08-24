# app.py
import tkinter as tk
from tkinter import ttk

def create_gui():
    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("Mon Application de Bureau")

    # Créer un label avec un message
    label = ttk.Label(root, text="Bonjour depuis Docker !")
    label.pack(padx=20, pady=20)

    # Démarrer la boucle principale de l'application
    root.mainloop()

if __name__ == "__main__":
    create_gui()
