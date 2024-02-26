import pygame
import math

pygame.init()

# Fenster und Schrift
screen = pygame.display.set_mode((800, 600))

ui_font = pygame.font.SysFont(pygame.font.get_default_font(), 40)

def vorbereitung():

    global ani, index, clock, timer_ms, timer_s, frame_ms, game_over, xx, l_figure, s_figure, m_figure, g_figure, w_figure, buchstaben_ausgabe
    global ss_figure, spieler_position, logo_position, gameover_position, winner_position, start_position, timer_position, positionen, eingabewort
    global STEIN_BREITE, ANI_DAUER, SPEED

    STEIN_BREITE = 180 # in Pixeln

    # Bilder laden und Positionen bestimmen
    l_figure = pygame.image.load("logo.png")
    s_figure = pygame.image.load("stein.png")
    m_figure = pygame.image.load("maus.png")
    g_figure = pygame.image.load("gameover.jpg")
    w_figure = pygame.image.load("winner.jpg")
    ss_figure = pygame.image.load("start.jpg")
    spieler_position = pygame.math.Vector2(300-STEIN_BREITE, 350)
    logo_position = pygame.math.Vector2(50, 50)
    gameover_position = pygame.math.Vector2(0, 0)
    winner_position = pygame.math.Vector2(0, 0)
    start_position = pygame.math.Vector2(0, 0)
    timer_position = pygame.math.Vector2(50, 500)

    # Wortauswahl
    from random import randrange
    auswahl = randrange(1, 11)

    game_over = 15

    if auswahl == 1:
        eingabewort = "erdbeere"
    elif auswahl == 2:
        eingabewort = "kaffeebecher"
    elif auswahl == 3:
        eingabewort = "osterferien"
    elif auswahl == 4:
        eingabewort = "finanzdienstleistungsunternehmen"
        game_over = 30
    elif auswahl == 5:
        eingabewort = "deutschland"
    elif auswahl == 6:
        eingabewort = "exzellent"
    elif auswahl == 7:
        eingabewort = "projizieren"
    elif auswahl == 8:
        eingabewort = "kennzeichen"
    elif auswahl == 9:
        eingabewort = "veranstaltungsinformationsdienst"
        game_over = 30
    elif auswahl == 10:
        eingabewort = "kumulieren"

    # Steinpositionen
    positionen = []
    x = 300
    y = 300
    for buchstabe in eingabewort:
        v = pygame.math.Vector2(x, y)
        x = x + 2*STEIN_BREITE
        positionen.append(v)

    # Oberfläche der Buchstaben
    index_b = 0
    buchstaben_ausgabe = []
    while index_b < len(eingabewort):
        b = eingabewort[index_b]
        surface = ui_font.render(b, False, "white")
        index_b = index_b + 1
        buchstaben_ausgabe.append(surface)

    # Variablen
    ani = -1
    index = 0
    clock = pygame.time.Clock()
    timer_ms = 0
    timer_s = 0
    frame_ms = 0
    xx = 0
    ANI_DAUER = 500 # in ms
    SPEED = STEIN_BREITE/(ANI_DAUER//2)



    aktuelle_position = eingabewort[index]
    pygame.display.set_caption(f"Tippe: {aktuelle_position}, verbleibende Zeit: {game_over-timer_s}s")

# Erkennung des richtigen Tastendrucks
def tastendruck(taste):

    global ani
    global index, xx
    aktuelle_position = eingabewort[index]
    if taste == ord(aktuelle_position):
        if ani == -1: #Animation startet nicht, nachdem bereits gestartet
            ani = 0 # Animation beginnt
    if taste == ord(aktuelle_position): # Übereinstimmung der beiden Zahlen des Unicodes
        index = index + 1
        if index <= len(eingabewort)-1:
            aktuelle_position = eingabewort[index]
            pygame.display.set_caption(f"Tippe: {aktuelle_position}, Zeit: {game_over-timer_s}s")
        else:
            xx = 3

# Animation des Sprungs
def sprung():
    global ani
    global frame_ms
    if ani == -1:
        return

    ani = ani + frame_ms
    if ani >= ANI_DAUER:
        ani = -1 #Animation stoppt

        #--- Bugfix Hr Glöckner
        spieler_position.y = 350
        i = 0
        for pos in positionen:
            pos.x = (i-index+1) * 2 * STEIN_BREITE # Verschiebung der Steine
            i += 1
        # ---

    elif ani > ANI_DAUER//2:
        spieler_position.y = spieler_position.y + int(frame_ms * SPEED) # Figur bewegt sich nach oben
    else:
        spieler_position.y = spieler_position.y - int(frame_ms * SPEED) # Figur bewegt sich nach unten

    for pos in positionen:
        pos.x = pos.x - frame_ms * SPEED

# Hauptprogramm
def spiel():
    global xx, timer_ms, frame_ms, timer_s, positionen
    # Timer
    frame_ms = clock.tick(60)

    # Timer aktualisieren
    timer_ms = timer_ms + frame_ms
    timer_s = timer_ms // 1000
    if timer_s >= game_over:
        xx = 2
    screen.fill("green") # Hintergrundfarbe
    surface = ui_font.render(f'{timer_s}s', False, "white") # Oberfläche Timer
    screen.blit(surface, timer_position) # Timer importieren

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.KEYDOWN:
           tastendruck(event.key) # Taste wird gedrückt

    sprung()

    # Steine, Logo, Tier und Buchstaben importieren
    screen.blit(l_figure,logo_position)
    for pos in positionen:
        screen.blit(s_figure, pos)
    screen.blit(m_figure,spieler_position)
    index_k = 0
    while index_k < len(eingabewort):
        p = pygame.Vector2(positionen[index_k])
        s = buchstaben_ausgabe[index_k]
        index_k = index_k + 1
        p.x += STEIN_BREITE // 2 # Buchstabe in der Mitte des Steins
        p.y += 60 // 2
        screen.blit(s, p)

# Bildschirme
def gameover():
    global xx
    screen.blit(g_figure, gameover_position) # importieren
    surface = ui_font.render(f'Eingabewort: {eingabewort}', False, "white") # Oberfläche
    screen.blit(surface, timer_position) # importieren
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Tastendruck
            xx = 0

def start():
    global xx
    screen.blit(ss_figure, start_position) # importieren
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Tastendruck
            vorbereitung()
            xx = 1

def winner():
    global xx
    screen.blit(w_figure, winner_position) # importieren
    surface = ui_font.render(f'Eingabewort: {eingabewort}', False, "white") # Oberfläche
    screen.blit(surface, timer_position) # importieren
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Tastendruck
            xx = 0

vorbereitung()
# Spiel am Laufen halten und richtigen Bildschirm anzeigen
running = True
while running:
    if xx == 0:
        start()
    elif xx == 1:
        spiel()
    elif xx == 2:
        gameover()
    elif xx == 3:
        winner()
    pygame.display.flip()

# pygame beenden
pygame.quit()

