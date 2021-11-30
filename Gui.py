from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pymysql

window = Tk()
window.title("Bienvenue chez Paris Tendance")
window.geometry("950x550+180+50")


path = "logo.png"
logo=Canvas(window, width=950,height=550,bg="black")
logo.place(x=0,y=10)

image = Image.open(path)
image = image.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

panel = tk.Label(logo, image = img)
panel.place(x=20,y=10)

def menu():
    window.destroy()
    import menuPrincipal

def menuClient():
    window.destroy()
    import ClientMenuPrincipal

def connecter():

    if ideEntry.get() == "" or mdpEntry.get() == "":
        messagebox.showinfo('Error', 'Ne peut pas etre vide')
    else:
        try:
            con=pymysql.connect(host="localhost", user="root", password="mysql", database="marketnet")
            cur=con.cursor()
            cur.execute("select * from utilisateurs where username=%s and password=%s",(ideEntry.get(),mdpEntry.get()))
            row= cur.fetchone()
            if row==None:
                messagebox.showinfo('Error', 'mauvais mot de passe ou identifiant')
            else:
                if ideEntry.get() == "djacoumani":
                    menu()
                else:
                    menuClient()
        except Exception as es:
            messagebox.showinfo('Error', 'Une erreur est apparue ...')


def inscription():
    window.destroy()
    import nouveauUtilisateur

def oublie():
    window.destroy()
    import mdpOublie

ide= Label(logo, text="Username",bg="black", font=('arial',15,'bold'), fg="#fff")
ide.place(x=430,y=140)

mdp= Label(logo, text="Password",bg="black", font=('arial',15,'bold'), fg="#fff")
mdp.place(x=430,y=200)

ideEntry=Entry(logo, width=50, relief=FLAT, font=('arial',12))
ideEntry.place(x=260,y=170)

mdpEntry=Entry(logo, width=50, show="*", relief=FLAT, font=('arial',12))
mdpEntry.place(x=260,y=230)

connexion=Button(logo,text="Se connecter",command=connecter, bg="green", fg="white", relief=FLAT, font=('arial',12), width = 20 )
connexion.place(x=400, y=280)

nouveaucompte=Button(logo,text="Creer un compte", command=inscription, bg="black", fg="#fff", relief=FLAT, font=('arial',12) )
nouveaucompte.place(x=310, y=350)

mdpoublie=Button(logo,text="Mot de passe oublié ?",command=oublie, bg="black", fg="#fff", relief=FLAT, font=('arial',12) )
mdpoublie.place(x=490, y=350)

window.mainloop()        

