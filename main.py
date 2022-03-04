import pygame
from settings import Settings
from game_util import GameUtil
from game_stats import GameStats
from game_controller import GameController
from aliens import Aliens
from ship import Ship

# init game
pygame.init()

# instantiate settings
s=Settings()
# set screen
screen=pygame.display.set_mode((s.width,s.height))
g_util=GameUtil(screen,s)
g_controller=GameController(s)
g_stat=GameStats(s,screen)

# set clock
clock=pygame.time.Clock()

# loading targets into list
aliens=Aliens(s,screen)
ship=Ship(s,screen)

# variabler
alien_counter=1
frame_counter=0


while True:
    frame_counter+=1
    # main loop

    # check events
    g_controller.check_events()

    # alien-counter should count "slower", dvs hver 20.  gang f.eks
    if (frame_counter % s.frequency == 0):
        alien_counter+=1
        if alien_counter==len(aliens.list_of_aliens):
            #out of bounds. Re-set targets somehow
            alien_counter=1
            aliens=Aliens(s,screen)

    if s.start_game==True:
        ship.move_ship(pygame.mouse.get_pos())
        g_util.blitBg()
        # adjust stuff that moves
        for alien in aliens.list_of_aliens[:alien_counter]:
            if ship.shipCollision(alien.alien_rect):
                g_stat.score+=1
                alien.killme()
            else:
                alien.alien_rect.centery+=alien.speed
                screen.blit(alien.alien_img,alien.alien_rect)

        # paint stuff
        ship.blitme()

    else:
        # tegne en startknap
        screen.fill(s.white)
        g_util.blitBtn()

    g_stat.blitText()
    pygame.display.update()
    clock.tick(s.fr)
