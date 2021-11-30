from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pymysql


window = Tk()
window.title("Menu principal")
window.geometry("950x550+180+50")


path = "logo.png"
file1="e-commerce.png"
file2 = "reseau.png"
file3="quitter.png"
file4 = "deconnexion.png"

logo=Canvas(window, width=950,height=550,bg="black")
logo.place(x=0,y=10)

image = Image.open(path)
image = image.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

image_dec = Image.open(file4)
img_dec = ImageTk.PhotoImage(image_dec)

image_ach = Image.open(file1)
img_ach = ImageTk.PhotoImage(image_ach)

image_quit = Image.open(file3)
img_quit = ImageTk.PhotoImage(image_quit)

image_prod = Image.open(file2)
img_prod = ImageTk.PhotoImage(image_prod)

panel = tk.Label(logo, image = img)
panel.place(x=20,y=10)

def quitter():
    window.destroy()
            
def produit():
    window.destroy()
    import Admin

def deconnexion():
    window.destroy()
    import Gui

def achat():
    window.destroy()
    import ClientMenuPrincipal

mag= Label(logo, text="Achat",bg="black", font=('arial',15,'bold'), fg="#fff")
mag.place(x=410,y=120)
magasin=Button(logo,text="Achat",command=achat, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 80 )
magasin.place(x=400, y=150)
magasin.configure(image=img_ach)

prod= Label(logo, text="Admin",bg="black", font=('arial',15,'bold'), fg="#fff")
prod.place(x=410,y=350)
produit=Button(logo,text="Produit",command=produit, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 80 )
produit.place(x=400, y=380)
produit.configure(image=img_prod)

quitt= Label(logo, text="Quitter",bg="black", font=('arial',15,'bold'), fg="#fff")
quitt.place(x=210,y=220)
quitter=Button(logo,text="Quitter",command=quitter, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 80 )
quitter.place(x=200, y=250)
quitter.configure(image=img_quit)

dec= Label(logo, text="Deconnexion",bg="black", font=('arial',15,'bold'), fg="#fff")
dec.place(x=610,y=220)
deconnexion=Button(logo,text="Achat",command=deconnexion, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 80 )
deconnexion.place(x=610, y=250)
deconnexion.configure(image=img_dec)


window.mainloop()

