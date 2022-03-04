import pygame
class GameStats():
    def __init__(self,settings,screen):
        self.score=0
        self.screen=screen
        self.conf=settings
        self.myfont = pygame.font.SysFont('arial', self.conf.font_size)

    def blitText(self):
        text=self.myfont.render(f"score: {self.score}",self.conf.white,self.conf.black)
        self.screen.blit(text, text.get_rect())


