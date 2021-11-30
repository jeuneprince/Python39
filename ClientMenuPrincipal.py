from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pymysql


window = Tk()
window.title("Faire des achats")
window.geometry("950x550+180+50")


path = "logo.png"
pantalon="pantalon.jpg"
short="short.jpg"
tshirt="tshirt.jpg"
accessoire="accessoire.jpg"
file4 = "deconnexion.png"

logo=Canvas(window, width=950,height=550,bg="black")
logo.place(x=0,y=10)

image = Image.open(path)
image = image.resize((120, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

image_dec = Image.open(file4)
image = image_dec.resize((30, 30), Image.ANTIALIAS)
img_dec = ImageTk.PhotoImage(image)

image_pant = Image.open(pantalon)
image = image_pant.resize((180, 150), Image.ANTIALIAS)
img_pant = ImageTk.PhotoImage(image)

image_short = Image.open(short)
image = image_short.resize((180, 150), Image.ANTIALIAS)
img_short = ImageTk.PhotoImage(image)

image_shirt = Image.open(tshirt)
image = image_shirt.resize((180, 150), Image.ANTIALIAS)
img_shirt = ImageTk.PhotoImage(image)

image_accessoire = Image.open(accessoire)
image = image_accessoire.resize((180, 150), Image.ANTIALIAS)
img_accessoire = ImageTk.PhotoImage(image)


def my_fun(k):
    if k ==0:
        window.destroy()
        import Pantalon
    elif k ==1:
        window.destroy()
        import Short
    elif k ==2:
        window.destroy()
        import Chemise
    elif k ==3:
        window.destroy()
        import Accesoire
        


panel = tk.Label(logo, image = img)
panel.place(x=20,y=10)



def deconnexion():
    window.destroy()
    import Gui
    
def categorie():
    
    try:
        con=pymysql.connect(host="localhost", user="root", password="mysql", database="marketnet")
        cur=con.cursor()
        cur.execute("select nom from categories")
        records= list(cur.fetchall())
        print_record = ''
        ligne = 200
        colonne = 200
        for record in range(len(records)):
            print_record += str(record) + "\n"
            button= Button(logo, text=(records[record]),command=lambda k=record: my_fun(k), bg="green", fg="white", relief=FLAT, font=('arial',12), width = 20)
            button.place(x=(ligne*record)+30 ,y=colonne)   
    except Exception as es:
        messagebox.showinfo('Error', 'Une erreur est apparue ...')

panelpant = tk.Label(logo, image = img_pant)
panelpant.place(x=30,y=250)

panelshort = tk.Label(logo, image = img_short)
panelshort.place(x=230,y=250)

panelshirt = tk.Label(logo, image = img_shirt)
panelshirt.place(x=430,y=250)

panelaccessoire = tk.Label(logo, image = img_accessoire)
panelaccessoire.place(x=630,y=250)

deconnexion=Button(logo,text="Deconnexion",command=deconnexion, bg="black", fg="white", relief=FLAT, font=('arial',12), width = 30, height = 40 )
deconnexion.place(x=900, y=10)
deconnexion.configure(image=img_dec)

categorie()

window.mainloop()

