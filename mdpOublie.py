from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pymysql

window = Tk()
window.title("Mot de passe oublié")
window.geometry("950x550+180+50")


path = "logo.png"
logo=Canvas(window, width=950,height=550,bg="black")
logo.place(x=0,y=10)

image = Image.open(path)
image = image.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

panel = tk.Label(logo, image = img)
panel.place(x=20,y=10)

def changermdp():

    if ideEntry.get() == "" or mdpEntry.get() == "" or telEntry.get() == "":
        messagebox.showinfo('Error', 'Ne peut pas etre vide')
    else:
        try:
            con=pymysql.connect(host="localhost", user="root", password="mysql", database="marketnet")
            cur=con.cursor()
            updateStatement = "UPDATE utilisateurs set password =%s where telephone=%s and username=%s"
            data=(mdpEntry.get(),telEntry.get(),ideEntry.get())
            cur.execute(updateStatement, data)
            cur.execute("select * from utilisateurs where telephone=%s and username=%s",(telEntry.get(),ideEntry.get()))
            row= cur.fetchone()
            if row==None:
                messagebox.showinfo('Error', 'mauvais telephone ou identifiant')
            else:
                messagebox.showinfo('Updated', 'Votre password a été bien modifé')
                print(row)
        except Exception as es:
            messagebox.showinfo('Error', 'Une erreur est apparue ...')


def retour():
    window.destroy()
    import Gui 

ide= Label(logo, text="Username",bg="black", font=('arial',15,'bold'), fg="#fff")
ide.place(x=430,y=140)

mdp= Label(logo, text="Nouveau Password",bg="black", font=('arial',15,'bold'), fg="#fff")
mdp.place(x=400,y=200)

tel= Label(logo, text="Entre le numero de telephone",bg="black", font=('arial',15,'bold'), fg="#fff")
tel.place(x=350,y=260)

ideEntry=Entry(logo, width=50, relief=FLAT, font=('arial',12))
ideEntry.place(x=260,y=170)

mdpEntry=Entry(logo, width=50, show="*", relief=FLAT, font=('arial',12))
mdpEntry.place(x=260,y=230)

telEntry=Entry(logo, width=50, relief=FLAT, font=('arial',12))
telEntry.place(x=260,y=290)


nouveaucompte=Button(logo,text="Valider",command=changermdp, bg="green", fg="white", relief=FLAT, font=('arial',12), width = 15  )
nouveaucompte.place(x=310, y=350)

mdpoublie=Button(logo,text="Retour",command=retour, bg="blue", fg="white", relief=FLAT, font=('arial',12), width = 15 )
mdpoublie.place(x=490, y=350)

window.mainloop()        

