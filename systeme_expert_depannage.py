import tkinter as tk
from tkinter import messagebox

# Base de connaissances pour le dépannage
base_de_connaissances = {
    ("ordinateur ne s'allume pas",): "Vérifiez si l'ordinateur est branché et si la prise fonctionne.",
    ("écran bleu",): "Essayyez de redémarrer l'ordinateur en mode sans échec.",
    ("internet ne fonctionne pas",): "Vérifiez si le câble Ethernet est correctement branché ou si le Wi-Fi est activé.",
    ("application ne s'ouvre pas",): "Vérifiez si l'application est à jour et essayez de la réinstaller.",
    ("ordinateur ne s'allume pas", "écran bleu"): "Vérifiez les connexions matérielles et redémarrez l'ordinateur.",
    ("internet ne fonctionne pas", "ordinateur ne s'allume pas"): "Si l'ordinateur ne s'allume pas, il est probable que la connexion Internet soit impossible.",
}

def diagnostiquer(symptomes):
    """Retourne la solution associée à une combinaison de symptômes."""
    symptomes_tuple = tuple(symptome.lower() for symptome in symptomes)
    return base_de_connaissances.get(symptomes_tuple, "Désolé, je n'ai pas de solution pour ce problème.")

def diagnostiquer_symptome():
    """Fonction pour diagnostiquer à partir de l'entrée utilisateur."""
    symptome_input = entree_symptome.get().strip()
    symptomes = [symptome.strip() for symptome in symptome_input.split(",")]
    solution = diagnostiquer(symptomes)
    messagebox.showinfo("Diagnostic", solution)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Système Expert de Dépannage")

# Label pour l'entrée de l'utilisateur
label_instruction = tk.Label(fenetre, text="Entrez les symptômes (séparés par des virgules) :")
label_instruction.pack()

# Champ de saisie pour les symptômes
entree_symptome = tk.Entry(fenetre, width=50)
entree_symptome.pack()

# Bouton pour obtenir le diagnostic
bouton_diagnostiquer = tk.Button(fenetre, text="Diagnostiquer", command=diagnostiquer_symptome)
bouton_diagnostiquer.pack()

# Lancer l'interface graphique
fenetre.mainloop()
