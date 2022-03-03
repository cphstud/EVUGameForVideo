import pygame
from ship import Ship
from game_stats import GameStats
from game_config import GameConfig
from game_logic import GameLogic
from game_util import GameUtil
from aliens import Aliens

def run_game():
    # init game
    pygame.init()

    # instantiate config
    g_conf=GameConfig()
    g_logic=GameLogic(g_conf)

    # set screen
    screen=pygame.display.set_mode((g_conf.width,g_conf.height))
    clock=pygame.time.Clock()
    g_util=GameUtil(g_conf,screen)
    g_stats=GameStats(g_conf,screen)

    # set the clock
    clock=pygame.time.Clock()

    # get the scoreboard
    board=GameStats(g_conf,screen)

    # get the game-actors
    ship=Ship(g_conf,screen)
    aliens=Aliens(g_conf,screen)

    # variables
    frame_counter=0
    alien_counter=0

    # run the main loop

    while True:
        frame_counter+=1
        g_logic.check_events()

        if g_conf.start_game==False:
            # tegne en startknap
            screen.fill(g_conf.white)
            g_util.blit_btn()
        else:
            g_util.blit_bg()
            ship.move_ship(pygame.mouse.get_pos())
            ship.blitme()
            if (frame_counter % g_conf.frequency == 0):
                alien_counter+=1
                if alien_counter==len(aliens.list_of_aliens):
                    alien_counter=0
                    aliens=Aliens(g_conf,screen)

            for alien in aliens.list_of_aliens[:alien_counter]:
                alien.move_down()
                if ship.collide(alien):
                    g_stats.score+=1
                    alien.kill()
                else:
                    alien.blitme()
        g_stats.show_score()
        clock.tick(g_conf.fr)
        pygame.display.update()

if __name__ == '__main__':
    run_game()


