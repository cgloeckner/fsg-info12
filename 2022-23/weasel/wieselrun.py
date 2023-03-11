import pygame,time,sys
from random import randrange 
from tilemap import karte    
from screens import out_of_game_screen

pygame.init()

#Größe des Spielfensters 
Y=960
X=960
zeitlimit = int(60 * 60 * 3) # fps * seconds * minutes
screen=pygame.display.set_mode((X,Y))

clock = pygame.time.Clock()

#Beispielfarben, falls diese benötigt werden, schon vorgeben
Rot=(255,0,0)
Grün=(0,255,0)
Schwarz=(0,0,0)
Weiß=(255,255,255)

#schriftart vorgeben
schriftart = pygame.font.SysFont(pygame.font.get_default_font(), 42)


def ladeFrames(richtung):
    l = ["", "", ""]
    l[0] = pygame.transform.scale(pygame.image.load(f"Bilder/erschrecken-{richtung}.png"),(64,64))
    l[1] = pygame.transform.scale(pygame.image.load(f"Bilder/erschrecken-{richtung}.png"),(64,64))
    l[2] = pygame.transform.scale(pygame.image.load(f"Bilder/Wiesel-{richtung}.png"),(64,64))
    return l


def ladenBewegungFrames(richtung):
    l= ["","","","","","","",""]
    l[0] = pygame.transform.scale(pygame.image.load(f"Bilder/{richtung}1.png"),(64,64))
    l[1] = pygame.transform.scale(pygame.image.load(f"Bilder/{richtung}1.png"),(64,64))
    l[2] = pygame.transform.scale(pygame.image.load(f"Bilder/{richtung}2.png"),(64,64))
    l[3] = pygame.transform.scale(pygame.image.load(f"Bilder/{richtung}2.png"),(64,64))
    l[4] = pygame.transform.scale(pygame.image.load(f"Bilder/{richtung}3.png"),(64,64))
    l[5] = pygame.transform.scale(pygame.image.load(f"Bilder/{richtung}4.png"),(64,64))
    l[6] = pygame.transform.scale(pygame.image.load(f"Bilder/{richtung}5.png"),(64,64))
    l[7] = pygame.transform.scale(pygame.image.load(f"Bilder/{richtung}6.png"),(64,64))
    return l


def naechsterBewegungsFrame():
    global frame
    if frame >= 35:
        frame = 25
    frame += 1


def zeichneBewegungsFrames(frameset):
    screen.blit(frameset[(frame//5)],(spieler_x-32,spieler_y-32))


def zeichneStandFrames(frameset):
    screen.blit(frameset[stand_frame//8],(spieler_x-32,spieler_y-32))

#zufällige Aneinanderreihung der einzelnen Level
def random_map ():
    nummer = [1]
    while len(nummer) < 10 :
        random_zahl = randrange(2,11)
        while random_zahl in nummer:
            random_zahl = randrange(2,11)
        nummer.append(random_zahl)
    return nummer

def run():
    global frame, spieler_x, spieler_y, stand_frame
    frame = 0
    spiellaeuft = True

    level = 0

    

    spieler_x=6*64
    spieler_y=9*64
    spieler_bewegung_h=0
    spieler_bewegung_v=0

    tile_kollision_position = []
    tile_kollision_position_pfeil = []
    tile_kollision_position_schilf_blume = []
    objekt_hitbox_liste = []
    schilf_blume_hitbox_liste = []

    letzte_richtung = 0
    stand_frame = 0

    nummer = random_map()

    # fps * seconds * minutes
    zeit_übrig = zeitlimit


    #verschiedene Orientierungen des Spielers und dessen Grafik, zusammen mit stoppen/erschrecken Animation
    spielfigur_rechts = ladeFrames("rechts")
    spielfigur_links = ladeFrames("links")
    spielfigur_oben = ladeFrames("oben")
    spielfigur_unten = ladeFrames("unten")
    bewegung_rechts = ladenBewegungFrames("rechts")
    bewegung_links = ladenBewegungFrames("links")
    bewegung_oben = ladenBewegungFrames("oben")
    bewegung_unten = ladenBewegungFrames("unten")


    while spiellaeuft:
        #Liste der Eingaben erstellen 
        for event in pygame.event.get():
            #Befehl für das Schließen des Spiels 
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()

            geschwindigkeit = 4

            #Überprüfen ob Spieler mit Schilf/Blume kollidiert 
            for objekt in schilf_blume_hitbox_liste :
                if player_hitbox.colliderect(objekt):
                            geschwindigkeit /= 2 
                            if geschwindigkeit < 2:
                                geschwindigkeit = 2 
            #Spielersteuerung
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    spieler_bewegung_v= - geschwindigkeit
                elif event.key==pygame.K_s:
                    spieler_bewegung_v= + geschwindigkeit
                elif event.key==pygame.K_a:
                    spieler_bewegung_h= - geschwindigkeit
                elif event.key==pygame.K_d:
                    spieler_bewegung_h= + geschwindigkeit
            #Wenn man a und d oder w und s gleichzeitig drückt, bleibt man stehen 
                elif event.key==pygame.K_w and event.key==pygame.K_s:
                    spieler_bewegung_v = 0
                elif event.key==pygame.K_a and event.key==pygame.K_d:
                    spieler_bewegung_h = 0
            #Wenn man die Taste lostlässt, bleibt man stehen
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_w or event.key==pygame.K_s:
                    spieler_bewegung_v = 0
                if event.key==pygame.K_a or event.key==pygame.K_d:
                    spieler_bewegung_h = 0

        #Spieltwelt zeichnen und Objekte, die Kollision besitzten oder ein Pfeil sind, eine Hitbox geben 
        tile_x = 0
        tile_y = 0
        spielwelt_stelle = 0
        spielwelt,tile_kollision = karte(f'Raum {nummer[level]}')
        while tile_y < 15:
            tile_x = 0
            while tile_x < 15:
                screen.blit(spielwelt[spielwelt_stelle],(tile_x*64,tile_y*64))
                position = (tile_x,tile_y)
                
                #Liste für die Koordinaten und Hitboxen der Objekte
                if tile_kollision[spielwelt_stelle] in ['a','i','j','k','l','m','n','o','q'] and position not in tile_kollision_position:
                    tile_kollision_position.append(position)
                    objekt_hitbox_liste.append(pygame.Rect((tile_x*64) ,(tile_y*64)  ,64,64))

                #Liste für die Koordinaten und Hitboxen der Pfeile
                if tile_kollision[spielwelt_stelle] in ['s','t'] and position not in tile_kollision_position_pfeil:
                    position_pfeil = (tile_x,tile_y)
                    tile_kollision_position_pfeil.append(position_pfeil)

                #Liste für die Koordinaten und Hitboxen von Schilf und Blumen    
                if tile_kollision[spielwelt_stelle] in ['p','r'] and position not in tile_kollision_position_schilf_blume:
                    position_schilf_blume = (position)
                    tile_kollision_position_schilf_blume.append(position_schilf_blume)
                    schilf_blume_hitbox_liste.append(pygame.Rect((tile_x*64) ,(tile_y*64)  ,64,64))

                spielwelt_stelle += 1
                tile_x += 1
            tile_y += 1

        #Erstellen der Spielerhitbox und merken der Tile-Koordinaten     
        player_tilepos_x = (spieler_x + spieler_bewegung_h) // 64
        player_tilepos_y = (spieler_y + spieler_bewegung_v) // 64
        player_hitbox = pygame.Rect(spieler_x-24, spieler_y-22,48,48)

        #Hitbox des Spielers anzeigen, wenn gewollt
        #pygame.draw.rect(screen, Weiß, player_hitbox)
        
        #Kollision mit Objekten überprüfen
        for objekt in objekt_hitbox_liste: 
            #Hitbox der Objekte anzeigen, wenn gewollt
            #pygame.draw.rect(screen, Weiß,objekt)
            if player_hitbox.colliderect(objekt):
                spieler_bewegung_h = 0
                spieler_bewegung_v = 0
                spieler_x = player_tilepos_x * 64 +32
                spieler_y = player_tilepos_y * 64 +32

        #Kollision mit einem Pfeil überprüfen                                
        if (player_tilepos_x, player_tilepos_y) in tile_kollision_position_pfeil:
            level += 1 
            spieler_y = 960
            tile_kollision_position.clear()
            tile_kollision_position_pfeil.clear()
            objekt_hitbox_liste.clear()
            tile_kollision_position_schilf_blume.clear()
            schilf_blume_hitbox_liste.clear()

        #Merken der Koordinaten des Spielers
        if spieler_bewegung_h != 0:
            spieler_x+=spieler_bewegung_h
        if spieler_x < 0 + 32:
            spieler_x = 32
        if spieler_x > X -32:
            spieler_x = X -32
        if spieler_bewegung_v != 0:
            spieler_y+=spieler_bewegung_v
        if spieler_y < 0 + 32:
            spieler_y = 32
        if spieler_y > Y - 32:
            spieler_y = Y -32


        #Timer einbauen
        min_gesamt = (zeit_übrig //60)//60
        sekunden_gesamt = (zeit_übrig//60) - (60 * (min_gesamt))
        zeit_übrig -= 1
        if sekunden_gesamt < 10:
            sekunden_gesamt = str('0') + str(sekunden_gesamt)
        if zeit_übrig > -1:
            timer_vorne = schriftart.render('Timer ' + str(min_gesamt) +':'+ str(sekunden_gesamt),True,Schwarz)
            timer_hinten = schriftart.render('Timer ' + str(min_gesamt) +':'+ str(sekunden_gesamt),True,Weiß)
            screen.blit(timer_vorne,(0,0)) and screen.blit(timer_hinten,(3,0))
        else:
            return "gameover"

        #gucken ob eine Taste gedückt wird (für animation) und diese speichern
        taste = pygame.key.get_pressed()

        if spieler_bewegung_h != 0 or spieler_bewegung_v != 0:
            # bewegt sich
            naechsterBewegungsFrame()
            stand_frame = 0

            if taste[pygame.K_d]:
                zeichneBewegungsFrames(bewegung_rechts)
                letzte_richtung = 1
            elif taste[pygame.K_a]:
                zeichneBewegungsFrames(bewegung_links)
                letzte_richtung = 2
            elif taste[pygame.K_w]:
                zeichneBewegungsFrames(bewegung_oben)
                letzte_richtung = 3
            elif taste[pygame.K_s]:
                zeichneBewegungsFrames(bewegung_unten)
                letzte_richtung = 4

        else:
            # steht
            # Stand-Animation ignorieren
            if stand_frame >= 16:
                stand_frame = 16

            if letzte_richtung == 1:
                if stand_frame >= 16:
                    stand_frame = 16

                zeichneStandFrames(spielfigur_rechts)

                stand_frame += 1
                frame = 0

            elif letzte_richtung == 2:
                if stand_frame >= 16:
                    stand_frame = 16

                zeichneStandFrames(spielfigur_links)

                stand_frame += 1
                frame = 0

            elif letzte_richtung == 3:
                if stand_frame >= 16:
                    stand_frame = 16

                zeichneStandFrames(spielfigur_oben)

                stand_frame += 1
                frame = 0

            elif letzte_richtung == 4:
                if stand_frame >= 16:
                    stand_frame = 16

                zeichneStandFrames(spielfigur_unten)

                stand_frame += 1
                frame = 0

            else:
                #stehen
                screen.blit(spielfigur_rechts[2],(spieler_x - 32 ,spieler_y - 32))
                frame = 0
        #Anzahl der zu spielenden Level begrenzen
        if level > 6:
            return "win"

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run()