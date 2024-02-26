import tkinter as tk
import random
import sys

laeuft = True
punkte = 0

#dann wird die Punktzahl um 1 erhöht
def func1():    #dieses Unterprogramm wird aufgerufen, wenn eine Frage richtig beantwortet wird
    global punkte
    punkte += 1#die Punktzahl um 1 erhöht
    score.config(text=str(punkte))
#folgendes Unterprogrammwird genutz um nach der Beantwortung einer Frage das Fenster zu schließen

def func2(root):#dieses Unterprogramm wird genutzt, wenn die Frage richtig oder falsch war um das Fenster zu schließen
    root.destroy()#das Fenster wird zerstört

#in diesem Unterprogramm läuft das Spiel
def fragen(f, a, b, c, d):#aus einer Liste werden Frage und Antworten ausgelesen
    global punkte, root2
    root2 = tk.Tk()#das Fenster 'root2' wird erstellt
    root2.geometry("1000x600")#Fenster mit der Größe 1000x600

    label2 = tk.Label(root2, text=f)#die Frage wird angezeigt
    label2.pack()

    y_Koordinate = [200, 300, 400, 500]#die y-Koordinaten der antworten werden zufällig aus der Liste ausgewählt
    d1 = random.choice(y_Koordinate)   #durch den Befehl 'random.choice' wird zufällig aus der Liste ausgewählt
    y_Koordinate.remove(d1)
    c1 = random.choice(y_Koordinate)
    y_Koordinate.remove(c1)
    b1 = random.choice(y_Koordinate)
    y_Koordinate.remove(b1)
    a1 = random.choice(y_Koordinate)

    #die Antworten werden als Buttons realisiert
    bt1 = tk.Button(root2, text=d, command=lambda: [func1(), func2(root2)])#dabei ist 'd' immer die richtige Antwort, deshalb wird func1 und func2 aufgerufen
    bt1.place(x=500, y=d1)                                                 #da 'd' immer die richtige Antwort ist müssen die Fragen zufällig geordnet sein
    bt2 = tk.Button(root2, text=c, command=lambda: func2(root2))#antworten a bis c sind falsch, deshalb wird nur func2 aufgerufen
    bt2.place(x=500, y=c1)
    bt3 = tk.Button(root2, text=b, command=lambda: func2(root2))
    bt3.place(x=500, y=b1)
    bt4 = tk.Button(root2, text=a, command=lambda: func2(root2))
    bt4.place(x=500, y=a1)

    bt5 = tk.Button(root2, text="Quiz beenden", command=abbruch)#mit dem Button "Quiz beenden" kann man das Quiz bennden und man kommt zum Endscreen
    bt5.place(x=20, y=550)

    global score
    score = tk.Label(root2, text="Punktzahl: "+str(punkte))#mit hilfe von 'score' wird die Punktzahl des Spilers wird angezeigt
    score.pack(pady=20)

    root2.mainloop()#'mainloop' hat die Wirkung, dass der Zustand des beschriebenen Fensters andauernd abgefragt wird

def Start(): #in diesem Unterprogram ist der Startscreen integriert
    root1 = tk.Tk()#es wird ein fenster erstellt
    root1.geometry("1000x600")#mit der Größe 1000x600
    label1 = tk.Label(root1, text="Willkommen zum Quiz")#dieser Text wird angezeigt
    label1.pack()
    schaltf1 = tk.Button(root1, text="Starte Quiz", command=root1.destroy)#der Button 'schaf1' hat die Funktion, dass der Startscreen zerstört wird
    schaltf1.place(x=500, y=300)

    root1.mainloop()

def Ende():     #in diesem Unterprogram ist der Endscreen integriert
    global punkte
    root3 = tk.Tk()
    root3.geometry("1000x600")
    Text1 = tk.Label(root3, text="Vielen dank fürs Spielen")
    Text1.place(x=400, y=100)
    Text2 = tk.Label(root3, text="Ihre Punktzahl:")
    Text2.place(x=400, y=200)
    Text4 = tk.Label(root3, text=str(punkte))
    Text4.place(x=500, y=200)
    bt6 = tk.Button(root3, text="Quiz beenden", command=root3.destroy)
    bt6.place(x=450, y=500)

    lade_punkte()

    Text5 = tk.Label(root3, text="bisheriger Highscore: " + str(lade_punkte()))
    Text5.place(x=400, y=450)

    if lade_punkte() < str(punkte):#wenn ein neuer Highscore erziehlt wurde, wird das Unterprogramm 'speicher_punkte' aufgerufen
        speicher_punkte(punkte)

    root3.mainloop()

def speicher_punkte(punkte): #in diesem Unterprogramm wird der Highscore gespeichert
    file = open('highscore.txt', "w")#eine Textdatei mit dem namen 'highscore' wird geöffnet
    file.write(str(punkte))#in diese Datei wird der Highscore geschrieben
    file.close()#die Textdatei wird geschlossen

def lade_punkte():  #der bestehende Highscore wird aus der Textdatei exportiert
    file = open('highscore.txt', "r")#datei wird geöffnet
    highscore = file.read()#die Datei wird eingelesen
    file.close()#Datei wird geschlossen
    return str(highscore)#der eingelesene Highscore wird an das Program gegeben

def abbruch():
    global laeuft, root2
    laeuft = False
    root2.destroy()

Start()

Quiz_Fragen_Antworten = [ #in dieser Liste sind alle Fragen und die dazugehörigen Antworten gespeichert
    ("Was ist die Hauptstadt von Deutschland?", "Dresden", "Hamburg", "Leipzig", "Berlin"),
    ("Wie heißt der höchste Berg Deutschlands?", "Mount Everest", "Brocken", "Matterhorn", "Zugspitze"),
    ("Was ist der Gefrierpunkt von Wasser?", "-100°C", "100°C", "-200°C", "0°C"),
    ("Was ist der Name des ersten Kanzler der BRD?", "Olaf Scholz", "Angela Merkel", "Willy Brandt", "Konrad Adenauer"),
    ("Wie viele Einwohner hat Deutschland?","54.000.000","67.000.000","91.000.000","84.000.000"),
    ("Welcher Fluss fließt durch Paris?","Themse","Donau","Rhein","Sein"),
    ("Wann wurde die Bundesrepublik Deutschland gegründet?","1946","1952","1947","1949"),
    ("Was ist der größte Ozean?","Atlantischer Ozean","Indischer Ozean","Persischer Golf","Pazifischer Ozean"),
    ("Wie viel Bit sind in einem Byte?","5","6","4","8")]

x = len(Quiz_Fragen_Antworten) #Anzahl der Fragen wird in der Variablen x definiert

while x != 0 and laeuft: #solange die Anzahl der fragen nicht 0 ist, läuft das Program weriter
    wahl = random.choice(Quiz_Fragen_Antworten)#es werden die Fragen zufällig ausgewählt
    fragen(wahl[0], wahl[1], wahl[2], wahl[3], wahl[4])
    Quiz_Fragen_Antworten.remove(wahl)#wurde eine Frage ausgewählt, wird sie aus der Liste aussortiert
    x -= 1#die Anzahl der Fragen in der Variablen x wird ebenfalls um 1 veringert

Ende()

