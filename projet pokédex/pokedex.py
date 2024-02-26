import tkinter as tk
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.title("Pokédex")
fenetre.geometry("500x500")
fenetre.config(bg="red")

class Pokemon():
    def __init__(self, number, name, type, abilite):
        self.number = number
        self.name = name
        self.type = type
        self.abilite = abilite

def save_pokedex(pokedex):
    with open('pokedex.txt', 'w') as f:
        for pokemon in pokedex:
            f.write(f"{pokemon.number},{pokemon.name},{pokemon.type},{pokemon.abilite}\n")
    messagebox.showinfo("Sauvegarde", "Pokédex sauvegardé avec succès!")

def load_pokedex():
    pokedex = []
    try:
        with open('pokedex.txt', 'r') as f:
            for line in f:
                number, name, type, abilite = line.strip().split(',')
                pokedex.append(Pokemon(number, name, type, abilite))
        messagebox.showinfo("Chargement", "Pokédex chargé avec succès!")
        return pokedex
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Aucun fichier de sauvegarde trouvé.")
        return []

def ajout_pokemon(pokedex, zone_text_1, zone_text_2, zone_text_3, zone_text_4, zone_enregistrement):
    number = zone_text_1.get()
    name = zone_text_2.get()
    type = zone_text_3.get()
    abilite = zone_text_4.get()
    pokedex.append(Pokemon(number, name, type, abilite))
    zone_enregistrement.insert(tk.END, f"{number} - {name}")
    zone_text_1.delete(0, tk.END)
    zone_text_2.delete(0, tk.END)
    zone_text_3.delete(0, tk.END)
    zone_text_4.delete(0, tk.END)
    save_pokedex(pokedex)

def afficher_details_pokemon(pokedex, zone_enregistrement):
    index_selectionne = zone_enregistrement.curselection()
    if index_selectionne:
        pokemon_selectionne = pokedex[index_selectionne[0]]
        messagebox.showinfo("Info sur le Pokémon", f"Numéro : {pokemon_selectionne.number}\nNom : {pokemon_selectionne.name}\nType : {pokemon_selectionne.type}\nAbilité : {pokemon_selectionne.abilite}")

def supprimer_pokemon(pokedex, zone_enregistrement):
    index_selectionne = zone_enregistrement.curselection()
    if index_selectionne:
        index = index_selectionne[0]
        del pokedex[index]
        zone_enregistrement.delete(index)

pokedex = load_pokedex()

zone_enregistrement = tk.Listbox(fenetre, height=7, width=35)
for pokemon in pokedex:
    zone_enregistrement.insert(tk.END, f"{pokemon.number} - {pokemon.name}")
zone_enregistrement.pack()

text1 = tk.Label(fenetre, text="Entré le numéro du Pokémon :", bg="red", fg="#ffffff")
text1.pack()

zone_text_1 = tk.Entry(fenetre)
zone_text_1.pack()

text2 = tk.Label(fenetre, text="Entré le Nom du Pokémon :", bg="red", fg="#ffffff")
text2.pack()

zone_text_2 = tk.Entry(fenetre)
zone_text_2.pack()

text3 = tk.Label(fenetre, text="Entré le(s) Type(s) du Pokémon :", bg="red", fg="#ffffff")
text3.pack()

zone_text_3 = tk.Entry(fenetre)
zone_text_3.pack()

text4 = tk.Label(fenetre, text="Entré le Talent spécial du Pokémon :", bg="red", fg="#ffffff")
text4.pack()

zone_text_4 = tk.Entry(fenetre)
zone_text_4.pack()

bouton_enregistre = tk.Button(fenetre, text="Ajouté", command=lambda: ajout_pokemon(pokedex, zone_text_1, zone_text_2, zone_text_3, zone_text_4, zone_enregistrement))
bouton_enregistre.pack()

bouton_supprimer = tk.Button(fenetre, text="Supprimer", command=lambda: supprimer_pokemon(pokedex, zone_enregistrement))
bouton_supprimer.pack()

zone_enregistrement.bind("<<ListboxSelect>>", lambda event: afficher_details_pokemon(pokedex, zone_enregistrement))

fenetre.mainloop()