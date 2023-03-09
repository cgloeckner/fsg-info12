import pygame

def out_of_game_screen(bezeichnung):
    titleaktiv = True
    Y= 960
    X= 960
    clock = pygame.time.Clock()
    screen=pygame.display.set_mode((X,Y))
    bild = pygame.transform.scale(pygame.image.load(f"Bilder/{bezeichnung}_screen.png"),(960,960))
    
    while titleaktiv: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                titleaktiv = False 

        screen.blit(bild,(0,0))
        pygame.display.flip()
        clock.tick(60)

        


