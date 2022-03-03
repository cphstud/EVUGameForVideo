import pygame
class GameStats():
    def __init__(self,settings,screen):
        self.screen=screen
        self.conf=settings
        self.score=0
        self.round=1
        self.font=pygame.font.SysFont("arial",32)

    def show_score(self):
        text=self.font.render(f"score: {self.score}")
        self.screen.blit(text,text.get_rect())


