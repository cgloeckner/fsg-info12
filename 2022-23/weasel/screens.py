import pygame

def out_of_game_screen(bezeichnung, block=0):
    titleaktiv = True
    Y= 960
    X= 960
    clock = pygame.time.Clock()
    screen=pygame.display.set_mode((X,Y))
    bild = pygame.transform.scale(pygame.image.load(f"Bilder/{bezeichnung}_screen.png"),(960,960))
    
    if block > 0:
        blockscreen = True
    else:
        blockscreen = False
    
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
        if blockscreen:
            print(f"blocking screen for {block} seconds")
            block_screen(clock, block)
            blockscreen = False

def block_screen(clock, seconds):
    i = 0
    while i < seconds:
        clock.tick(1)
        i += 1
    # clear pygame event queue
    pygame.event.get()
    clock.tick(60)


        


