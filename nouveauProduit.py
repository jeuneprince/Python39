from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pymysql


window = Tk()
window.title("S'inscrire")
window.geometry("950x550+180+50")


path = "logo.png"
logo=Canvas(window, width=950,height=550,bg="#46B8E1")
logo.place(x=0,y=10)

image = Image.open(path)
image = image.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

panel = tk.Label(logo, image = img)
panel.place(x=20,y=10)

def creer():

    if ideEntry.get() == "" or mdpEntry.get() == "" or nomEntry.get() == "" or prenomEntry.get() == "" or telEntry.get() == "" or courrielEntry.get() == "" or addrEntry.get() == "":
        messagebox.showinfo('Error', 'Aucun champ ne peut pas etre vide')
    else:
        try:
            con=pymysql.connect(host="localhost", user="root", password="mysql", database="marketnet")
            cur=con.cursor()
            sql="insert into utilisateurs (nom, prenom, telephone, courriel, adresse,admin, username, password) VALUES (%s,%s,%s,%s,%s,0,%s,%s)"
            val=(nomEntry.get(),prenomEntry.get(),telEntry.get(),courrielEntry.get(),addrEntry.get(),ideEntry.get(),mdpEntry.get())
            cur.execute(sql,val)
            
            con.commit()
            window.destroy()
            import Gui
            
            
        except Exception as es:
            messagebox.showinfo('Error', 'Une erreur est apparue ...')
        con.close()

def quitter():
    window.destroy()
            
nom= Label(logo, text="Nom",bg="#46B8E1", font=('arial',12,'bold'), fg="#fff")
nom.place(x=310,y=100)

prenom= Label(logo, text="Prenom",bg="#46B8E1", font=('arial',12,'bold'), fg="#fff")
prenom.place(x=490,y=100)

tel= Label(logo, text="Telephone",bg="#46B8E1", font=('arial',12,'bold'), fg="#fff")
tel.place(x=310,y=160)

courriel= Label(logo, text="Courriel",bg="#46B8E1", font=('arial',12,'bold'), fg="#fff")
courriel.place(x=490,y=160)

addr= Label(logo, text="Adresse",bg="#46B8E1", font=('arial',12,'bold'), fg="#fff")
addr.place(x=310,y=220)

ide= Label(logo, text="Username",bg="#46B8E1", font=('arial',12,'bold'), fg="#fff")
ide.place(x=600,y=220)

mdp= Label(logo, text="Password",bg="#46B8E1", font=('arial',12,'bold'), fg="#fff")
mdp.place(x=310,y=290)


nomEntry=Entry(logo, width=15, relief=FLAT, font=('arial',12))
nomEntry.place(x=310,y=130)

prenomEntry=Entry(logo, width=15, relief=FLAT, font=('arial',12))
prenomEntry.place(x=490,y=130)

telEntry=Entry(logo, width=15, relief=FLAT, font=('arial',12))
telEntry.place(x=310,y=190)

courrielEntry=Entry(logo, width=25, relief=FLAT, font=('arial',12))
courrielEntry.place(x=490,y=190)

addrEntry=Entry(logo, width=25, relief=FLAT, font=('arial',12))
addrEntry.place(x=310,y=250)

mdpEntry=Entry(logo, width=15,show="*", relief=FLAT, font=('arial',12))
mdpEntry.place(x=310,y=330)

ideEntry=Entry(logo, width=15,relief=FLAT, font=('arial',12))
ideEntry.place(x=600,y=250)



connexion=Button(logo,text="Inscription",command=creer, bg="green", fg="white", relief=FLAT, font=('arial',12), width = 20 )
connexion.place(x=300, y=400)

quitter=Button(logo,text="Quitter",command=quitter, bg="red", fg="white", relief=FLAT, font=('arial',12), width = 15 )
quitter.place(x=500, y=400)


window.mainloop()

