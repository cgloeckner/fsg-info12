from subprocess import call 
import pygame 
from screens import out_of_game_screen


spiel_status = 'title'
spielaktiv = True

while spielaktiv:
        if spiel_status == 'title':
            out_of_game_screen('title')
            pygame.quit()
            spiel_status = 'spielen'

        elif spiel_status == 'spielen':    
            call(['python','wieselrun.py'])
            spiel_status = 'ende'
        else:
             pygame.quit()
             quit()


        
