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



pokedex = []

mewtwo = Pokemon(150, "Mewtwo", "Psy", "Psykokinesie")
mew = Pokemon(151, "Mew", "Psy", "Psykokinesie")
pikachu = Pokemon(25, "Pikachu", "Electrique", "Eclair")

pokedex.extend([mewtwo, mew, pikachu])


def ajout_pokemon():
    
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
    messagebox.showinfo("Sauvegarde", "Pokémon sauvegardée avec succès!")


def afficher_details_pokemon():
    index_selectionne = zone_enregistrement.curselection()
    if index_selectionne:
        pokemon_selectionne = pokedex[index_selectionne[0]]
        messagebox.showinfo("Info sur le Pokémon", f"Numéro : {pokemon_selectionne.number}\n Nom : {pokemon_selectionne.name}\n Type : {pokemon_selectionne.type}\n Abilité : {pokemon_selectionne.abilite}")

def save_pokedex():
    with open('projet pokédex\pokedex.txt', 'w', encoding= "utf-8") as f:
        for pokemon in pokedex:
            f.write(f"{pokemon.number},{pokemon.name},{pokemon.type},{pokemon.abilite}\n")
    messagebox.showinfo("Sauvegarde", "Pokédex sauvegardé avec succès!")

def load_pokedex():
    try:
        with open('projet pokédex\pokedex.txt', 'r', encoding= "utf-8") as f:
            for line in f:
                number, name, type, abilite = line.strip().split(',')
                pokedex.append(Pokemon(number, name, type, abilite))
        messagebox.showinfo("Chargement", "Pokédex chargé avec succès!")
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Aucun fichier de sauvegarde trouvé.")    

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

bouton_enregistre = tk.Button(fenetre, text="Ajouté", command=ajout_pokemon)
bouton_enregistre.pack()

zone_enregistrement.bind("<<ListboxSelect>>", lambda event: afficher_details_pokemon())

load_pokedex()

fenetre.mainloop()