from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk




def connecter():

        try:
            con=pymysql.connect(host="localhost", user="root", password="mysql", database="marketnet")
            cur=con.cursor()
            result = 0
            cur.execute("SELECT nom_article, prix from commandes")
            rows = cur.fetchall()
            
            for row in rows:
                
                tree.insert("", tk.END, values=row)
               
            
            con.close()
            
        except Exception as es:
            messagebox.showinfo('Error', 'Une erreur est apparue ...')



def deconnexion():
    root.destroy()
    import Gui
    

def retour():
    root.destroy()
    import ClientMenuPrincipal

root = tk.Tk()
root.geometry("950x550+180+50")
root.title("Panier")

logo=Canvas(root, width=950,height=550,bg="black")
logo.place(x=0,y=0)



path = "logo.png"
file4 = "deconnexion.png"
file3 = "e-commerce.png"
file2 = "retour.png"

image = Image.open(path)
image = image.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

image_dec = Image.open(file4)
image = image_dec.resize((30, 30), Image.ANTIALIAS)
img_dec = ImageTk.PhotoImage(image)

image_panier = Image.open(file3)
image = image_panier.resize((30, 30), Image.ANTIALIAS)
img_panier = ImageTk.PhotoImage(image)

image_retour = Image.open(file2)
image = image_retour.resize((30, 30), Image.ANTIALIAS)
img_retour = ImageTk.PhotoImage(image)

panel = tk.Label(logo, image = img)
panel.place(x=20,y=10)


retour=Button(logo,text="retour",command=retour, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 30, height = 40 )
retour.place(x=850, y=10)
retour.configure(image=img_retour)

deconnexion=Button(logo,text="Deconnexion",command=deconnexion, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 30, height = 40 )
deconnexion.place(x=900, y=10)
deconnexion.configure(image=img_dec)

tree = ttk.Treeview(root, column=("c1", "c2"), show='headings')


tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="nom")


tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="prix")


tree.pack(pady=150)



connecter()



root.mainloop()
