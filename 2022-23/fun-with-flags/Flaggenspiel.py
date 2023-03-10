from tkinter import Tk, Label
from PIL import ImageTk, Image
import sqlite3
from random import *

print("Herzlich Willkommen zu einem kleinen Flaggen-Quizspiel")
print("Flaggen aus Europa werden gleich in einem seperatem Fenster geöffnet.")
print("Schauen Sie sich die Flagge an und schließend Sie anschließend das Fenster mit der Flagge.\nDanach soll man die Fragen beantworten.")
print("Achtung: Ö usw. werden ausgeschrieben (d.h. ö = oe)!!! Viel Spaß")

verbindung = sqlite3.connect("laenderinfos.db")
zeiger = verbindung.cursor()
zeiger.execute("SELECT * FROM laender")
inhalt = zeiger.fetchall()


# die Funktion liefert dir die passende Antwort aus den datensatz aus einer Frage im Datensatz ist unter 0 das Kürzel, unter 1 der name
#unter 2 die hauptstadt, unter 3 die Einwohnerzahl abgespeichert, mit kuerzel ist das lÄnderkuerzel gemeint
def informationErmitteln(ziffer,kuerzel):
    sql = "SELECT * FROM laender WHERE kuerzel LIKE ?"
    zeiger.execute(sql, (kuerzel,))
    for dsatz in zeiger:
        return(dsatz[ziffer])


fragen = ["Zu welchem Land gehört diese Flagge?", "Was ist die Hauptstadt des Landes, zu dem diese Flagge gehört?", "Wie viele Einwohner hat das Land, zudem diese Flagge gehört?"]
l = ["DE","EL","EN","HU","FR","CH","FI","NO","NL","BE","SE","CY","DK","BG","CZ","EE","IE","ES","HR","LV","LT","MT","AT","PL","PT","RO","SI","SK","IS","LU"]

# wählt zufällig eine Frage und ein Land aus den Listen obendrüber aus und sucht nach der antwort nach der frage
def frageUndAntwort():
    nFrage = randint(0,2)
    frage = fragen[nFrage]
    print(frage) # muss stehen bleiben / irgendwie in die graphische oberfläche
    nLand = randint(0,29)
    land = l[nLand]


    # Fenster erzeugen
    gui = Tk(className="Quizflagge")
    # Größe des Fensters anpassen
    gui.geometry("700x550")

    img = Image.open("flag-icons-main/flags/4x3/de.png")
    at = Image.open("flag-icons-main/flags/4x3/at.png")
    be = Image.open("flag-icons-main/flags/4x3/be.png")
    bg = Image.open("flag-icons-main/flags/4x3/bg.png")
    ch = Image.open("flag-icons-main/flags/4x3/ch.png")
    cy = Image.open("flag-icons-main/flags/4x3/cy.png")
    cz = Image.open("flag-icons-main/flags/4x3/cz.png")
    de = Image.open("flag-icons-main/flags/4x3/de.png")
    dk = Image.open("flag-icons-main/flags/4x3/dk.png")
    ee = Image.open("flag-icons-main/flags/4x3/ee.png")
    el = Image.open("flag-icons-main/flags/4x3/gr.png")
    en = Image.open("flag-icons-main/flags/4x3/gb-eng.png")
    es = Image.open("flag-icons-main/flags/4x3/es.png")
    fi = Image.open("flag-icons-main/flags/4x3/fi.png")
    fr = Image.open("flag-icons-main/flags/4x3/fr.png")
    hr = Image.open("flag-icons-main/flags/4x3/hr.png")
    hu = Image.open("flag-icons-main/flags/4x3/hu.png")
    ie = Image.open("flag-icons-main/flags/4x3/ie.png")
    iS = Image.open("flag-icons-main/flags/4x3/is.png")
    lt = Image.open("flag-icons-main/flags/4x3/lt.png")
    lu = Image.open("flag-icons-main/flags/4x3/lu.png")
    lv = Image.open("flag-icons-main/flags/4x3/lv.png")
    mt = Image.open("flag-icons-main/flags/4x3/mt.png")
    nl = Image.open("flag-icons-main/flags/4x3/nl.png")
    no = Image.open("flag-icons-main/flags/4x3/no.png")
    pl = Image.open("flag-icons-main/flags/4x3/pl.png")
    pt = Image.open("flag-icons-main/flags/4x3/pt.png")
    ro = Image.open("flag-icons-main/flags/4x3/ro.png")
    se = Image.open("flag-icons-main/flags/4x3/se.png")
    si = Image.open("flag-icons-main/flags/4x3/si.png")
    sk = Image.open("flag-icons-main/flags/4x3/sk.png")


    # Bildgröße anpassen, damit das Bild ins Fenster passt
    img = img.resize((200,350), Image.ANTIALIAS)
    # Bild in ein TK-kompatibles Format umwandeln
    img = ImageTk.PhotoImage(img)
    at.img = ImageTk.PhotoImage(at)
    be.img = ImageTk.PhotoImage(be)
    bg.img = ImageTk.PhotoImage(bg)
    ch.img = ImageTk.PhotoImage(ch)
    cy.img = ImageTk.PhotoImage(cy)
    cz.img = ImageTk.PhotoImage(cz)
    dk.img = ImageTk.PhotoImage(dk)
    ee.img = ImageTk.PhotoImage(ee)
    el.img = ImageTk.PhotoImage(el)
    en.img = ImageTk.PhotoImage(en)
    es.img = ImageTk.PhotoImage(es)
    fi.img = ImageTk.PhotoImage(fi)
    fr.img = ImageTk.PhotoImage(fr)
    hr.img = ImageTk.PhotoImage(hr)
    hu.img = ImageTk.PhotoImage(hu)
    ie.img = ImageTk.PhotoImage(ie)
    iS.img = ImageTk.PhotoImage(iS)
    lt.img = ImageTk.PhotoImage(lt)
    lu.img = ImageTk.PhotoImage(lu)
    lv.img = ImageTk.PhotoImage(lv)
    mt.img = ImageTk.PhotoImage(mt)
    nl.img = ImageTk.PhotoImage(nl)
    no.img = ImageTk.PhotoImage(no)
    pl.img = ImageTk.PhotoImage(pl)
    pt.img = ImageTk.PhotoImage(pt)
    ro.img = ImageTk.PhotoImage(ro)
    se.img = ImageTk.PhotoImage(se)
    si.img = ImageTk.PhotoImage(si)
    sk.img = ImageTk.PhotoImage(sk)

    # Tk-Label erzeugen und Bild einfügen

    if land == "AT":
        label = Label(image = at.img)
        label.image = at.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "BE":
        label = Label(image = be.img)
        label.image = be.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "BG":
        label = Label(image = bg.img)
        label.image = bg.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "CH":
        label = Label(image = ch.img)
        label.image = ch.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "CY":
        label = Label(image = cy.img)
        label.image = cy.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "CZ":
        label = Label(image = cz.img)
        label.image = cz.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "DE":
        label = Label(image = img)
        label.image = img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "DK":
        label = Label(image = dk.img)
        label.image = dk.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "EE":
        label = Label(image = ee.img)
        label.image = ee.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "EL":
        label = Label(image = el.img)
        label.image = el.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "EN":
        label = Label(image = en.img)
        label.image = en.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "ES":
        label = Label(image = es.img)
        label.image = es.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "FI":
        label = Label(image = fi.img)
        label.image = fi.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "FR":
        label = Label(image = fr.img)
        label.image = fr.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "HU":
        label = Label(image = hu.img)
        label.image = hu.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "HR":
        label = Label(image = hr.img)
        label.image = hr.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "IE":
        label = Label(image = ie.img)
        label.image = ie.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "IS":
        label = Label(image = iS.img)
        label.image = iS.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "LU":
        label = Label(image = lu.img)
        label.image = lu.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "LT":
        label = Label(image = lt.img)
        label.image = lt.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "LV":
        label = Label(image = lv.img)
        label.image = lv.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "MT":
        label = Label(image = mt.img)
        label.image = mt.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "NL":
        label = Label(image = nl.img)
        label.image = nl.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "NO":
        label = Label(image = no.img)
        label.image = no.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "PL":
        label = Label(image = pl.img)
        label.image = pl.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "PT":
        label = Label(image = pt.img)
        label.image = pt.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "RO":
        label = Label(image = ro.img)
        label.image = ro.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "SE":
        label = Label(image = se.img)
        label.image = se.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "SI":
        label = Label(image = si.img)
        label.image = si.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    elif land == "SK":
        label = Label(image = sk.img)
        label.image = sk.img
        # Tk-Label im Fenster platzieren
        label.place(x=10, y=10)
    # Programm starten
    gui.mainloop()

    #print(chr(34) + land + chr(34)) #das war nur zum ausprobieren, statt den kuerzel müsste die Flagge angezeigt werden
    antwort = informationErmitteln(nFrage + 1 , land )
    return antwort

#das verbindet alles dann, und kuckt ob der spieler richtig antwortet, gibt das weiter
def spielen():
    richtig = frageUndAntwort()
    spielerantwort = str(input("Was ist deine Antwort? " ))
    if richtig == spielerantwort :
        return True
    else:
        return False



# hier beginnt der Kern des spieles, anzahl der Runden festlegen, Punkte zählen
a = int(input("Wie viele Runden wollen Sie spielen? "))
n = a
i = 0

while a > 0:
    richtigGeantwortet = spielen()
    if  richtigGeantwortet :
        i += 1
        print("Richtige Antwort, +1 Punkt. Demnach haben Sie insgesamt", i ,"Punkt(e).")
    else:
        print("Falsche Antwort, +0 Punkte. Demnach haben Sie insgesamt", i ,"Punkt(e).")
    a -= 1

if i >= ( 9 / 10 ) * n:
    print("Herzlichen Glückwunsch! Sie haben", i, "richtige Antworten")
elif i > ( 1 / 3 ) * n and i < ( 9 / 10 ) * n :
    print(i, "von", n, "richtigen Antworten. Weiter so")
else:
    print("Fehler sind menschlich!", i, "von", n, "richtigen Antworten - Nächstes Mal wird besser!")


verbindung.close()# wichtig! Verbindung zu Datenbank wieder schließen