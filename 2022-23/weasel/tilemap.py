import pygame 
import textwrap

wasser = pygame.transform.scale(pygame.image.load("Bilder/wasser.png"),(64,64))
sand = pygame.transform.scale(pygame.image.load("Bilder/sand.png"),(64,64))
sand_wasser = pygame.transform.scale(pygame.image.load("Bilder/sand_wasser_uebergang.png"),(64,64))
gras = pygame.transform.scale(pygame.image.load("Bilder/gras.png"),(64,64))
sand_gras = pygame.transform.scale(pygame.image.load("Bilder/sand_gras_uebergang.png"),(64,64))
bruecke_links = pygame.transform.scale(pygame.image.load("Bilder/bruecke_links.png"),(64,64))
bruecke_rechts = pygame.transform.scale(pygame.image.load("Bilder/bruecke_rechts.png"),(64,64))
baum_gras = pygame.transform.scale(pygame.image.load("Bilder/baum_gras.png"),(64,64))
baum_sand = pygame.transform.scale(pygame.image.load("Bilder/baum_sand.png"),(64,64))
baumstamm = pygame.transform.scale(pygame.image.load("Bilder/baumstamm.png"),(64,64))
wald = pygame.transform.scale(pygame.image.load("Bilder/wald.png"),(64,64))
stein_gras = pygame.transform.scale(pygame.image.load("Bilder/stein_gras.png"),(64,64))
stein_sand = pygame.transform.scale(pygame.image.load("Bilder/stein_sand.png"),(64,64))
gebirge = pygame.transform.scale(pygame.image.load("Bilder/gebirge.png"),(64,64))
schilf =pygame.transform.scale(pygame.image.load("Bilder/schleim.png"),(64,64))
sand_wasser_ecke = pygame.transform.scale(pygame.image.load("Bilder/sand_wasser_ecke.png"),(64,64))
wasserfall = pygame.transform.scale(pygame.image.load("Bilder/wasserfall.png"),(64,64))
blumen = pygame.transform.scale(pygame.image.load("Bilder/blumen.png"),(64,64))
pfeil_gras = pygame.transform.scale(pygame.image.load("Bilder/pfeil_gras.png"),(64,64))
pfeil_sand = pygame.transform.scale(pygame.image.load("Bilder/pfeil_sand.png"),(64,64))


def karte(dateiname):
    tiles = {
        'a': wasser,
        'b': sand,
        'c': sand_wasser,
        'd': sand_wasser_ecke,
        'e': gras,
        'f': sand_gras, 
        'g': bruecke_links,
        'h': bruecke_rechts,
        'i': baum_gras,
        'j': baum_sand,
        'k': baumstamm,
        'l': wald,
        'm': stein_gras,
        'n': stein_sand,
        'o': gebirge,
        'p': schilf,
        'q': wasserfall,
        'r': blumen,
        's': pfeil_gras,
        't': pfeil_sand
    }
    with open(dateiname,'r') as datei:
        zeilen = datei.readlines()
    felder_bezeichnungen = []
    felder = []
    for zeile in zeilen:
        liste = textwrap.wrap(zeile,2)
        for zeichen in liste:
            try: 
                tile = zeichen[0]
                rotation = int(zeichen[1])
                feld = tiles[tile]
                feld = pygame.transform.rotate(feld,rotation*90)
                felder.append(feld)
                felder_bezeichnungen.append(tile)
            except:
                pass
    return felder,felder_bezeichnungen 









