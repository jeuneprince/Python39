from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pymysql


window = Tk()
window.title("Menu principal")
window.geometry("950x550+180+50")


path = "logo.png"

file2 = "prod.png"
file3="quitter.png"
file4 = "deconnexion.png"

logo=Canvas(window, width=950,height=550,bg="black")
logo.place(x=0,y=10)

image = Image.open(path)
image = image.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

image_dec = Image.open(file4)
img_dec = ImageTk.PhotoImage(image_dec)


image_quit = Image.open(file3)
img_quit = ImageTk.PhotoImage(image_quit)

image_prod = Image.open(file2)
img_prod = ImageTk.PhotoImage(image_prod)

panel = tk.Label(logo, image = img)
panel.place(x=20,y=10)

def supprimer():
    window.destroy()
    import Supprimer
            
def ajouter():
    window.destroy()
    import Ajouter

def retour():
    window.destroy()
    import menuPrincipal



prod= Label(logo, text="Ajouter un produit",bg="black", font=('arial',13,'bold'), fg="#fff")
prod.place(x=370,y=350)
produit=Button(logo,text="Ajout",command=ajouter, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 80 )
produit.place(x=400, y=380)
produit.configure(image=img_prod)

quitt= Label(logo, text="Supprimer un produit",bg="black", font=('arial',13,'bold'), fg="#fff")
quitt.place(x=160,y=220)
quitter=Button(logo,text="Delete",command=supprimer, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 80 )
quitter.place(x=200, y=250)
quitter.configure(image=img_quit)

dec= Label(logo, text="Retour",bg="black", font=('arial',15,'bold'), fg="#fff")
dec.place(x=620,y=220)
deconnexion=Button(logo,text="Back",command=retour, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 80 )
deconnexion.place(x=610, y=250)
deconnexion.configure(image=img_dec)


window.mainloop()

