import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

fenetre = tk.Tk()
fenetre.title("Pokédex")
fenetre.geometry("600x695")
background_image = Image.open("projet pokédex/pokédexe.png")
background_image_tk = ImageTk.PhotoImage(background_image)
background_label = tk.Label(fenetre, image=background_image_tk)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

police = ("Helvetica", 12, "bold")
police1 = ("Helvetica", 9, "bold")
fg_color = "#F2F2F2"

class Pokemon():
    def __init__(self, number, name, type, abilite):
        self.number = number
        self.name = name
        self.type = type
        self.abilite = abilite

def bouton_clic(event):
    print("Bouton cliqué!")

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
    pokedex.sort(key=lambda x: int(x.number))  
    zone_enregistrement.delete(0, tk.END)
    for pokemon in pokedex:
        zone_enregistrement.insert(tk.END, f"{pokemon.number} - {pokemon.name}")
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
        save_pokedex(pokedex)

pokedex = load_pokedex()

zone_enregistrement = tk.Listbox(fenetre, height=9, width=25, font=police, bg=fg_color )
for pokemon in pokedex:
    zone_enregistrement.insert(tk.END, f"{pokemon.number} - {pokemon.name}")
zone_enregistrement.place(x=250, y=100)

text1 = tk.Label(fenetre, text="Numéro :", font=police1, bg="#c4e4b2")
text1.place(x=250, y=440)

zone_text_1 = tk.Entry(fenetre, font=police1, width=23, bg= "#c4e4b2")
zone_text_1.place(x=310, y=440)

text2 = tk.Label(fenetre, text="Nom :", font=police1, bg="#c4e4b2")
text2.place(x=250, y=470)

zone_text_2 = tk.Entry(fenetre, font=police1, width=23, bg="#c4e4b2")
zone_text_2.place(x=310, y=470)

text3 = tk.Label(fenetre, text="Type(s) :", font=police1, bg="#c4e4b2")
text3.place(x=250, y=500)

zone_text_3 = tk.Entry(fenetre, font=police1, width=23, bg="#c4e4b2")
zone_text_3.place(x=310, y=500)

text4 = tk.Label(fenetre, text="Talent spécial :", font=police1, bg="#c4e4b2")
text4.place(x=250, y=530)

zone_text_4 = tk.Entry(fenetre, font=police1, width=18, bg="#c4e4b2")
zone_text_4.place(x=340, y=530)

bouton_ajouter = tk.Label(fenetre, text="A", font=police, bg="#d1d3d3",fg="blue")
bouton_ajouter.place(x=492, y=525)
bouton_ajouter.bind("<Button-1>", lambda event: ajout_pokemon(pokedex, zone_text_1, zone_text_2, zone_text_3, zone_text_4, zone_enregistrement))

# Bouton Supprimer
bouton_supprimer = tk.Label(fenetre, text="S", font=police, bg="#d1d3d3",fg="red")
bouton_supprimer.place(x=492, y=567)
bouton_supprimer.bind("<Button-1>", lambda event: supprimer_pokemon(pokedex, zone_enregistrement))
zone_enregistrement.bind("<<ListboxSelect>>", lambda event: afficher_details_pokemon(pokedex, zone_enregistrement))

fenetre.mainloop()