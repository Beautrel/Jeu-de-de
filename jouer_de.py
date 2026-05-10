from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

score = 0  # ✅ Variable globale

def lancer_de():
    global score  # ✅ On utilise la variable globale

    image_choisi = random.choice(liste_images)
    image1 = ImageTk.PhotoImage(Image.open(image_choisi))
    label_image.configure(image=image1)
    label_image.image = image1

    numero_sorti = liste_images.index(image_choisi) + 1  # ✅ Plus besoin des if/elif

    if numero_choisi.get() == "":
        messagebox.showerror("Erreur", "Veuillez entrer un nombre entre 1 et 6")
        return

    try:
        valeur = int(numero_choisi.get())
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide")
        return

    if valeur < 1 or valeur > 6:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre entre 1 et 6")
        return

    if numero_sorti == valeur:
        score += 1
        label_result.configure(text="Vous avez gagné !", fg="green")
        label_score.config(text="Score: " + str(score), fg="green")
        label_emoji.config(text="✅", fg="green")
    else:
        score -= 1
        label_result.configure(text="Vous avez perdu !", fg="red")
        label_score.config(text="Score: " + str(score), fg="red")
        label_emoji.config(text="❌", fg="red")


root = Tk()
root.title("Jeu de simulation de dé")
root.geometry("400x550+500+200")
root.resizable(False, False)

label1 = Label(root, text="Choisir un nombre entre 1 et 6", pady=10, bg="blue", fg="white", font=("Arial", 14))
label1.grid(row=1, column=1, columnspan=2)

numero_choisi = Entry(root, width=30, border=10, bg="#10d135", fg="red")
numero_choisi.grid(row=2, column=1, columnspan=2, pady=15)

liste_images = ["images/de1.png", "images/de2.png", "images/de3.png",
                "images/de4.png", "images/de5.png", "images/de6.png"]

image_de = ImageTk.PhotoImage(Image.open(random.choice(liste_images)))
label_image = Label(root, image=image_de)
label_image.image = image_de
label_image.grid(row=3, column=1, columnspan=2)

button_lancer = Button(root, text="Lancer", fg="blue", font=("Arial", 14, "bold"), width=10, command=lancer_de, cursor="hand2")
button_lancer.grid(row=4, column=1, padx=20, pady=20)

button_quitter = Button(root, text="Quitter", fg="red", font=("Arial", 14, "bold"), width=10, command=root.quit, cursor="hand2")
button_quitter.grid(row=4, column=2, padx=20, pady=20)

label_result = Label(root, text="", font=("Arial", 14, "bold"), pady=20)
label_result.grid(row=5, column=1, columnspan=2)

label_score = Label(root, text="Score: 0", pady=10, font=("Arial", 15, "bold"))
label_score.grid(row=6, column=2)

label_emoji = Label(root, text="", pady=10, font=("Arial", 15, "bold"))
label_emoji.grid(row=6, column=1)

root.mainloop()