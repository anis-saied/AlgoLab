# Programme aide memoire Tkinter
# Rappelle l'utilisation des widgets suivants:
# Radio, Checkbutton, Scale, Canvas et aussi Label, Button, Entry

from tkinter import *

#Fonction commandee par les boutons radio
def changer_couleur():
    texte_radio.config(fg=couleur.get())
    

#Fonction commandee par le bouton du cadre "Entry, Button, Label"
#On efface l'entree et on modifie le Label de droite
def afficher():
    affiche.config(text=entrer.get())
    entrer.delete(0,END)    #Index de debut et de fin
    

#Fonction commandee par le widget Scale
#L'appel a la fonction envoie automatiquement en parametre la valeur (string) donnee par l'echelle
#On peut aussi recuperer cette valeur par get()
def taille(x):
    info="arial "+x
    texte_scale.config(font=info)
    

#Fonction commandee par les cases a cocher
#On recupere le contenu des variables Tkinter par la methode get()
def cocher():
    texte_coche.config(bg=var_bg.get(),fg=var_fg.get())
    


cadre=Tk()
cadre.title("AIDE MEMOIRE TKINTER")


#Entree, sortie, boutons
fen_entrer=Frame(cadre,bd=4,relief=RAISED)
fen_entrer.pack(fill=BOTH, expand=1)
Label(fen_entrer, text="ENTRY BUTTON LABEL",font="arial 20 bold").grid(row=0,column=0)
entrer=Entry(fen_entrer,font="arial 20 bold")
entrer.grid(row=1,column=0)
action=Button(fen_entrer,text="AFFICHER A DROITE",width=20,font="arial 20 bold",command=afficher)
action.grid(row=1,column=1)
affiche=Label(fen_entrer,text="",width=20,font="arial 20 bold",bg='white')
affiche.grid(row=1,column=2)


#Boutons radio
#Un seul bouton peut etre choisi
#Tous les boutons du meme groupe doivent porter le meme nom( ici 'radio') et etre associes a la meme variable
#On a donc besoin d'une variable Tkinter (ici 'couleur', du type String)
fen_radio=Frame(cadre,bd=4,relief=RAISED)
fen_radio.pack(fill=BOTH, expand=1)
Label(fen_radio, text="BOUTONS RADIO",font="arial 20 bold").grid(row=0,column=0,columnspan=3)
couleur=StringVar() #variable tkinter associee aux boutons radio
radio=Radiobutton(fen_radio,text='ROUGE',variable=couleur,value='red',bg='gray',command=changer_couleur)
radio.grid(row=1,column=0,sticky=E+W+N+S)
radio=Radiobutton(fen_radio,text='BLEU',variable=couleur,value='blue',bg='gray',command=changer_couleur)
radio.grid(row=1,column=1,sticky=E+W+N+S)
radio=Radiobutton(fen_radio,text='VERT',variable=couleur,value='green',bg='gray',command=changer_couleur)
radio.grid(row=1,column=2,sticky=E+W+N+S)
radio.select()  #selectionne un bouton, donc ici le dernier
texte_radio=Label(fen_radio,text="OPTION ISN",bg='white',font="arial 20 bold")
texte_radio.grid(row=1,column=3,sticky=E+W+N+S)
radio.invoke() #lance la fonction commandee par le groupe


#Cases a cocher
#Un nombre quelconque de boutons peuvent etre coches
#Il y a donc une variable par bouton, et une fonction par bouton
#Onvalue donne la valeur de la variable si la case est cochee, Offvalue.....
#Par defaut la variable vaut 0 ou 1
fen_coche=Frame(cadre,bd=4,relief=RAISED)
fen_coche.pack(fill=BOTH, expand=1)
Label(fen_coche, text="CASES A COCHER",font="arial 20 bold").grid(row=0,column=0,columnspan=3)
var_fg = StringVar()
var_bg = StringVar()
coche_fg = Checkbutton(fen_coche, text="Texte rouge", variable=var_fg, onvalue="red", offvalue="black",command=cocher)
coche_fg.grid(row=1,column=0)
coche_bg = Checkbutton(fen_coche, text="Fond jaune", variable=var_bg, onvalue="yellow", offvalue="white" ,command=cocher)
coche_bg.grid(row=1,column=2)
texte_coche=Label(fen_coche,text="OPTION ISN",bg='white',fg='black',font="arial 20 bold")
texte_coche.grid(row=1,column=3)
coche_fg.deselect()
coche_bg.deselect()


#Scale
fen_scale=Frame(cadre,bd=4,relief=RAISED)
fen_scale.pack(fill=BOTH, expand=1)
Label(fen_scale, text="WIDGET SCALE",font="arial 20 bold").grid(row=0,column=0)
curseur=Scale(fen_scale,length=300,orient=HORIZONTAL,label="Taille",showvalue = 1, from_ = 10,to = 40, tickinterval =5, command=taille)
curseur.grid(row=1,column=0)
texte_scale=Label(fen_scale,text="OPTION ISN",bg='white',font="arial 10")
texte_scale.grid(row=1,column=1)


cadre.mainloop()
