from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pymysql


window = Tk()
window.title("Ajouter un produit")
window.geometry("950x550+180+50")


path = "logo.png"
logo=Canvas(window, width=950,height=550,bg="black")
logo.place(x=0,y=10)

# Create a Tkinter variable
tkvar = StringVar(window)
tkvar2 = StringVar(window)

# Dictionary with options
choices = { 'Pantalons','Shorts','Chemises et T-shirts','Accessoires'}
tkvar.set('Pantalons') # set the default option

choices2 = { 'XS','S','M', 'L','XL','XXL'}
tkvar2.set('XS') # set the default option

image = Image.open(path)
image = image.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

panel = tk.Label(logo, image = img)
panel.place(x=20,y=10)

def creer():
    cat = 0 
    if descriptionEntry.get() == "" or prixEntry.get() == "" or nomEntry.get() == "" or tkvar2.get() == "" or tkvar.get() == "" or couleurEntry.get() == "" or photoEntry.get() == ""or stockEntry.get() == "":
        messagebox.showinfo('Error', 'Aucun champ ne peut pas etre vide')
    else:
        try:
            con=pymysql.connect(host="localhost", user="root", password="mysql", database="marketnet")
            cur=con.cursor()
            sql="insert into articles (nom, description, prix, taille, couleur,stock, categories_id, photo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            if tkvar.get() == "Pantalons":
                cat = 1
            elif tkvar.get() == "Shorts":
                cat = 2
            elif tkvar.get() == "Chemises et T-shirts":
                cat = 3
            elif tkvar.get() == "Accessoires":
                cat = 4
                
            val=(nomEntry.get(),descriptionEntry.get(),prixEntry.get(),tkvar2.get(),couleurEntry.get(),stockEntry.get(),cat,photoEntry.get())
            cur.execute(sql,val)
            
            con.commit()
            window.destroy()
            import Admin
            
            
        except Exception as es:
            messagebox.showinfo('Error', 'Une erreur est apparue ...')
        con.close()

def retour():
    window.destroy()
    import Admin
            
nom= Label(logo, text="Nom",bg="black", font=('arial',12,'bold'), fg="#fff")
nom.place(x=310,y=100)

description= Label(logo, text="Description",bg="black", font=('arial',12,'bold'), fg="#fff")
description.place(x=490,y=100)

prix= Label(logo, text="Prix",bg="black", font=('arial',12,'bold'), fg="#fff")
prix.place(x=310,y=160)

popupMenu2 = OptionMenu(logo, tkvar2, *choices2)
taille= Label(logo, text="Taille",bg="black", font=('arial',12,'bold'), fg="#fff")
taille.place(x=490,y=160)

couleur= Label(logo, text="Couleur",bg="black", font=('arial',12,'bold'), fg="#fff")
couleur.place(x=310,y=220)

popupMenu = OptionMenu(logo, tkvar, *choices)
categorie= Label(logo, text="Categorie",bg="black", font=('arial',12,'bold'), fg="#fff")
categorie.place(x=600,y=220)

stock= Label(logo, text="Stock",bg="black", font=('arial',12,'bold'), fg="#fff")
stock.place(x=310,y=290)

photo= Label(logo, text="Photo",bg="black", font=('arial',12,'bold'), fg="#fff")
photo.place(x=600,y=290)


nomEntry=Entry(logo, width=15, relief=FLAT, font=('arial',12))
nomEntry.place(x=310,y=130)

descriptionEntry=Entry(logo, width=15, relief=FLAT, font=('arial',12))
descriptionEntry.place(x=490,y=130)

prixEntry=Entry(logo, width=15, relief=FLAT, font=('arial',12))
prixEntry.place(x=310,y=190)

popupMenu2.place(x=490,y=190)

couleurEntry=Entry(logo, width=25, relief=FLAT, font=('arial',12))
couleurEntry.place(x=310,y=250)

stockEntry=Entry(logo, width=15,relief=FLAT, font=('arial',12))
stockEntry.place(x=310,y=330)

popupMenu.place(x=600,y=250)

photoEntry=Entry(logo, width=15,relief=FLAT, font=('arial',12))
photoEntry.place(x=600,y=330)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# on change dropdown value
def change_dropdown2(*args):
    print( tkvar2.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)
tkvar2.trace('w', change_dropdown2)

connexion=Button(logo,text="Ajouter",command=creer, bg="green", fg="white", relief=FLAT, font=('arial',12), width = 20 )
connexion.place(x=300, y=400)

retour=Button(logo,text="Retour",command=retour, bg="blue", fg="white", relief=FLAT, font=('arial',12), width = 15 )
retour.place(x=500, y=400)


window.mainloop()

