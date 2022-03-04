import sys
import pygame


class GameController():
    def __init__(self,settings):
        self.conf=settings

    def check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.conf.start_game=not self.conf.start_game


