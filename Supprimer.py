from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pymysql


window = Tk()
window.title("Supprimer un produit")
window.geometry("950x550+180+50")


path = "logo.png"
logo=Canvas(window, width=950,height=550,bg="black")
logo.place(x=0,y=10)

image = Image.open(path)
image = image.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

panel = tk.Label(logo, image = img)
panel.place(x=20,y=10)

def supprimer():

    if suppEntry.get() == "":
        messagebox.showinfo('Error', 'Aucun champ ne peut pas etre vide')
    else:
        try:
            con=pymysql.connect(host="localhost", user="root", password="mysql", database="marketnet")
            cur=con.cursor()
            cur.execute("DELETE FROM articles WHERE id=%s",(suppEntry.get()))
            con.commit()
            print("record(s) deleted")
            
            
        except Exception as es:
            messagebox.showinfo('Error', 'Une erreur est apparue ...')
        con.close()

def retour():
    window.destroy()
    import Admin
            

supp= Label(logo, text="Numero Article",bg="black", font=('arial',12,'bold'), fg="#fff")
supp.place(x=310,y=160)


suppEntry=Entry(logo, width=15, relief=FLAT, font=('arial',12))
suppEntry.place(x=310,y=190)



connexion=Button(logo,text="Supprimer",command=supprimer, bg="red", fg="white", relief=FLAT, font=('arial',12), width = 20 )
connexion.place(x=300, y=400)

quitter=Button(logo,text="Retour",command=retour, bg="blue", fg="white", relief=FLAT, font=('arial',12), width = 15 )
quitter.place(x=500, y=400)


window.mainloop()

