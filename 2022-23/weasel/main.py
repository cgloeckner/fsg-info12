from subprocess import call 
import pygame 
from screens import out_of_game_screen
import wieselrun


spiel_status = 'title'
spielaktiv = True

while spielaktiv:
        if spiel_status == 'title':
            out_of_game_screen('title')
            spiel_status = 'spielen'
        
        elif spiel_status == 'win':
            out_of_game_screen('win', 3)
            spiel_status = 'spielen'

        elif spiel_status == 'gameover':
            out_of_game_screen('game_over', 3)
            spiel_status = 'spielen'

        elif spiel_status == 'spielen':
            spiel_status = wieselrun.run()

        else:
             pygame.quit()
             quit()


        
