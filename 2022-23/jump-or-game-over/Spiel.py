import pygame
import sys
import random

pygame.init()
hintergrund = pygame.image.load("Grafiken/hintergrund.jpg")
screen = pygame.display.set_mode([1920,696])
clock = pygame.time.Clock()
pygame.display.set_caption("Game")

gruen = (0,255,0)
rot = (255,0,0)
schwarz = (0,0,0)
gelb = (255,255,0)
blau = (0,0,255)
weiss = (255,255,255)

sprung = pygame.image.load("Grafiken/springen.png")
rechtsGehen = [pygame.image.load("Grafiken/gehen-rechts.png"),pygame.image.load("Grafiken/rechts.png")]
linksGehen = [pygame.image.load("Grafiken/gehen-links.png"),pygame.image.load("Grafiken/links.png")]
stehen = pygame.image.load("Grafiken/stehen-bloed-gucken.png")

class spieler:
    def __init__(self,x,y,geschw,breite,hoehe,sprungvar,richtg,schritteRechts,schritteLinks):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.sprungvar = sprungvar
        self.richtg = richtg
        self.schritteRechts = schritteRechts
        self.schritteLinks = schritteLinks
        self.sprung = False
    def laufen(self,liste):
        if liste[0]:
            self.x -= self.geschw
            self.richtg = [1,0,0,0]
            self.schritteLinks += 1
        if liste[1]:
            self.x += self.geschw
            self.richtg = [0,1,0,0]
            self.schritteRechts += 1
    def resetSchritte(self):
        self.schritteLinks = 0
        self.schritteRechts = 0
    def stehen(self):
        self.richtg = [0,0,1,0]
        self.resetSchritte()
    def sprungSetzen(self):
        if self.sprungvar == -18:
            self.sprung = True
            self.sprungvar = 17

    def springen(self):
        if self.sprung:
            self.richtg = [0,0,0,1]
            if self.sprungvar >= -17:
                n = 1
                if self.sprungvar < 0:
                    n = -1
                self.y -= (self.sprungvar**2)*0.17*n
                self.sprungvar -= 1
            else:
                self.sprung = False
    def spZeichnen(self):
        if self.schritteRechts == 15:
            self.schritteRechts = 0
        if self.schritteLinks == 15:
            self.schritteLinks = 0
        if self.richtg[0]:
            screen.blit(linksGehen[self.schritteLinks//8], (self.x,self.y))
        if self.richtg[1]:
            screen.blit(rechtsGehen[self.schritteRechts//8], (self.x,self.y))
        if self.richtg[2]:
            screen.blit(stehen, (self.x,self.y))
        if self.richtg[3]:
            screen.blit(sprung, (self.x,self.y))


class monster:
    def __init__(self,x,y,radius,farbe,geschw):
        self.x = x
        self.y = y
        self.radius = radius
        self.farbe = farbe
        self.geschw = geschw
    def fliegen(self):
        self.x -= self.geschw
    def zeichne(self):
        pygame.draw.circle(screen, self.farbe, (self.x, self.y), self.radius, 0)


def kollosion():
    global monstern, verloren
    spielerArea=pygame.Rect(spieler1.x,spieler1.y+15,spieler1.breite+100,spieler1.hoehe+95)
    for m in monstern:
        monsterArea = pygame.Rect(m.x-m.radius,m.y-m.radius,m.radius*2,m.radius*2)
        if spielerArea.colliderect(monsterArea):
            verloren = True

def zeichnen():
    screen.blit(hintergrund, (0,0))
    spieler1.spZeichnen()
    #pygame.draw.rect(screen, (0, 0, 255),[spieler1.x,spieler1.y+15,spieler1.breite+100,spieler1.hoehe+95],2) macht Trefferbereich Spieler sichtbar
    for m in monstern:
        m.zeichne()
    if verloren:
        screen.fill(schwarz)
        schrift = pygame.font.SysFont('Arial', 35, True, True)
        text = schrift.render("Du hast verloren", True, (rot))
        einfuerung = schrift.render("Tutorial: w drücken", True, (blau))
        neustart = schrift.render("Neustart: Leertaste drücken", True, (weiss))
        if anzahlM >= 1:
            scoreAusgabe = schrift.render("Score:" + str(score), True, (gruen))
        else:
            scoreAusgabe = schrift.render("Score:" + "0", True, (rot))
        hScore = schrift.render("Highscore:"+ str(hoesterPunktestand), True, (gelb))
        screen.blit(text, [700, 300])
        screen.blit(scoreAusgabe, [700, 400])
        screen.blit(hScore, [700, 450])
        screen.blit(neustart, [700, 500])
        screen.blit(einfuerung, [700, 550])
    pygame.display.update()



def tutorial():
    schrift = pygame.font.SysFont('Arial', 35, True, True)
    anweisungen = schrift.render("Ziel: weiche den Monsterkugeln aus", True, (blau))
    weiter = schrift.render("Zum beginnen Leertaste drücken", True, (blau))
    steuerung = schrift.render("Steuerung:", True, (blau))
    rechtsLinks = schrift.render("Rechts/Links: rechte Pfeiltaste/linke Pfeiltaste", True, (blau))
    ausweichen = schrift.render("Springen: obere Pfeiltaste", True, (blau))
    anhalten = schrift.render("Pause: p drücken", True, (blau))
    screen.blit(hintergrund, (0,0))
    screen.blit(anweisungen, [700, 100])
    screen.blit(weiter, [700, 600])
    screen.blit(steuerung, [700, 300])
    screen.blit(rechtsLinks, [700, 340])
    screen.blit(ausweichen, [700, 380])
    screen.blit(anhalten, [700, 420])
    pygame.display.update()
    lesen = True
    while lesen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            lesen = False

def highScore():
    global hoesterPunktestand
    if hoesterPunktestand < score and anzahlM >= 1:
      hoesterPunktestand = score


tutorial()

linkeWand = pygame.draw.rect(screen, (0,0,0), (0,0,2,696), 0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (1800,0,2,696), 0)
hoesterPunktestand = 0

spiel = True
while spiel:
    spieler1 = spieler(300,330,10,96,128,-18,[0,0,1,0],0,0)
    monstern = []
    spawnZeit = 300
    speed = 7
    farbe = gruen
    n = 270
    score = 0
    anzahlM = 0
    verloren = False
    go = True
    pause = False
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        spielerRechteck = pygame.Rect(spieler1.x,spieler1.y,96,128)
        gedrueckt = pygame.key.get_pressed()

        if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
            spieler1.laufen([0,1])
        elif gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
            spieler1.laufen([1,0])
        else:
            spieler1.stehen()

        if gedrueckt[pygame.K_UP]:
            spieler1.sprungSetzen()
        spieler1.springen()

        if pygame.key.get_pressed()[pygame.K_p]:
            pause = True
            schrift = pygame.font.SysFont('Arial', 35, True, True)
            screen.blit(schrift.render("Weiter: w drücken", True, (schwarz)), [730, 500])
            schrift = pygame.font.SysFont('Arial', 130, True, True)
            screen.blit(schrift.render("Pause", True, (schwarz)), [700, 300])
            pygame.display.update()
            while pause:
                pygame.event.get()
                if pygame.key.get_pressed()[pygame.K_w]:
                    pause = False


        if len(monstern) <= 4 and n>=spawnZeit:
            monstern.append(monster(1920,500,7,farbe,speed))
            if anzahlM <= 10:
                spawnZeit = random.randint(249, 301)
                speed = random.randint(5, 9)
                farbe = gruen
            elif anzahlM <= 30:
                spawnZeit = random.randint(149, 201)
                speed = random.randint(7, 13)
                farbe = gelb
            else:
                spawnZeit = random.randint(49, 101)
                speed = random.randint(13, 17)
                farbe = rot
            n=0

        for m in monstern:
            if m.x >= 0:
                m.fliegen()
            else:
                monstern.remove(m)
                anzahlM += 1
        kollosion()
        zeichnen()
        clock.tick(60)
        n += 1
        score += 1
        if verloren:
            go = False



    read = True
    while read:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        highScore()
        zeichnen()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            read = False
        if pygame.key.get_pressed()[pygame.K_w]:
            read = False
            tutorial()