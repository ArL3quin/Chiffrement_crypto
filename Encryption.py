import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import string
import secrets

#=====================================Fonction============================================================================#

def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            # Calcul du décalage en fonction de la casse
            shift = ord(key[i % key_length].upper()) - ord('A')
            if plain_text[i].islower():
                base = ord('a')
            else:
                base = ord('A')
            encrypted_text += chr(((ord(plain_text[i]) - base + shift) % 26) + base)
        else:
            encrypted_text += plain_text[i]
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            # Calcul du décalage en fonction de la casse
            shift = ord(key[i % key_length].upper()) - ord('A')
            if encrypted_text[i].islower():
                base = ord('a')
            else:
                base = ord('A')
            decrypted_text += chr(((ord(encrypted_text[i]) - base - shift) % 26) + base)
        else:
            decrypted_text += encrypted_text[i]
    return decrypted_text

def save_password():
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    encryption_key = encryption_key_entry.get()
    
    if password == confirm_password:
        encrypted_password = vigenere_encrypt(password, encryption_key)
        with open("password.txt", "a") as f:
            f.write(encrypted_password + "\n")
            f.write(encryption_key + "\n")
        messagebox.showinfo("Succès", "Le mot de passe chiffré et la clé de chiffrement ont été enregistrés avec succès dans le fichier password.txt.")
    else:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")

def decrypt_password():
    encrypted_password = encrypted_password_entry.get()
    decryption_key = decryption_key_entry.get()
    decrypted_password = vigenere_decrypt(encrypted_password, decryption_key)
    decrypted_password_entry.delete(0, tk.END)
    decrypted_password_entry.insert(0, decrypted_password)
    

def generate_random_key():
    alphabet = string.ascii_uppercase
    key = ''.join(secrets.choice(alphabet) for _ in range(10))
    encryption_key_entry.delete(0, tk.END)
    encryption_key_entry.insert(0, key)


#============================================================================================================================#


#===========================================Interface Graphique=================================================================================#

# Création de la fenêtre principale
root = tk.Tk()
root.title("Chiffrement Vigenère")


# Chargement de l'image de fond
background_image = Image.open("output.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)



# Adapter la taille de la fenêtre à l'image
root.geometry("{}x{}".format(background_image.width, background_image.height))

# Création des widgets
password_label = tk.Label(root, text="Mot de passe:")
password_entry = tk.Entry(root, show="*")
confirm_password_label = tk.Label(root, text="Confirmer le mot de passe:")
confirm_password_entry = tk.Entry(root, show="*")
encryption_key_label = tk.Label(root, text="Clé de chiffrement (Vigenère):")
encryption_key_entry = tk.Entry(root)
generate_key_button = tk.Button(root, text="Générer une clé aléatoire", command=generate_random_key)
generate_key_button.grid(row=3, column=2, padx=10, pady=5)
save_button = tk.Button(root, text="Enregistrer", command=save_password)
encrypted_password_label = tk.Label(root, text="Mot de passe chiffré (Vigenère):")
encrypted_password_entry = tk.Entry(root)
decryption_key_label = tk.Label(root, text="Clé de déchiffrement (Vigenère):")
decryption_key_entry = tk.Entry(root)
decrypt_button = tk.Button(root, text="Déchiffrer", command=decrypt_password)
decrypted_password_label = tk.Label(root, text="Mot de passe déchiffré:")
decrypted_password_entry = tk.Entry(root)

# Placement des widgets dans la fenêtre
password_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
password_entry.grid(row=0, column=1, padx=10, pady=5)
confirm_password_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
confirm_password_entry.grid(row=1, column=1, padx=10, pady=5)
encryption_key_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
encryption_key_entry.grid(row=2, column=1, padx=10, pady=5)
save_button.grid(row=3, column=0, columnspan=2, pady=10)
encrypted_password_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
encrypted_password_entry.grid(row=4, column=1, padx=10, pady=5)
decryption_key_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
decryption_key_entry.grid(row=5, column=1, padx=10, pady=5)
decrypt_button.grid(row=6, column=0, columnspan=2, pady=10)
decrypted_password_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)
decrypted_password_entry.grid(row=7, column=1, padx=10, pady=5)


# Lancement de la boucle principale
root.mainloop()


#============================================================================================================================#
