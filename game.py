import pygame
from ship import Ship
from game_stats import GameStats
from game_config import GameConfig
from aliens import Aliens

def run_game():
    # init game
    pygame.init()

    # instantiate config
    g_conf=GameConfig()

    # set screen
    screen=pygame.display.set_mode((g_conf.width,g_conf.height))

    # set the clock
    clock=pygame.time.Clock()

    # get the scoreboard
    board=GameStats(g_conf,screen)

    # get the game-actors
    ship=Ship(g_conf,screen)
    aliens=Aliens(g_conf,screen)





if __name__ == '__main__':
    run_game()


