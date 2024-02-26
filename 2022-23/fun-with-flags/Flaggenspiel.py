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

    if land == "EN":
        imgCode = "gb-eng"
    elif land == "EL":
        imgCode = "gr"
    else:
        imgCode = land.lower()
    
    # Bild laden
    flagImg = Image.open(f"flag-icons-main/flags/4x3/{imgCode}.png")
    # Größe anpassen, damit die Grafik ins Fenster passt
    flagImg = flagImg.resize((680, 530), Image.LANCZOS)
    # In Tk-kompatibles Format umwandeln
    flagImg = ImageTk.PhotoImage(flagImg)
    # Label erzeugen und im Fenster platzieren
    label = Label(image = flagImg)
    label.place(x = 10, y = 10)

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
        return (True, richtig)
    else:
        return (False, richtig)



# hier beginnt der Kern des spieles, anzahl der Runden festlegen, Punkte zählen
a = int(input("Wie viele Runden wollen Sie spielen? "))
n = a
i = 0

while a > 0:
    richtigGeantwortet = spielen()
    if  richtigGeantwortet[0]:
        i += 1
        print("Richtige Antwort, +1 Punkt. Demnach haben Sie insgesamt", i ,"Punkt(e).")
    else:
        print("Falsche Antwort, +0 Punkte. Demnach haben Sie insgesamt", i ,"Punkt(e).")
        print(f"Richtig wäre gewesen {richtigGeantwortet[1]}.")
    a -= 1

if i >= ( 9 / 10 ) * n:
    print("Herzlichen Glückwunsch! Sie haben", i, "richtige Antworten")
elif i > ( 1 / 3 ) * n and i < ( 9 / 10 ) * n :
    print(i, "von", n, "richtigen Antworten. Weiter so!")
else:
    print("Fehler sind menschlich!", i, "von", n, "richtigen Antworten - Nächstes Mal wird besser!")


verbindung.close()# wichtig! Verbindung zu Datenbank wieder schließen