import pygame

class GameUtil():
    def __init__(self,screen,settings):
        self.screen=screen
        self.conf=settings
        self.bg=pygame.image.load("ressources/bluebg.png")
        self.bg = pygame.transform.scale(self.bg, (self.conf.width, self.conf.height))
        self.startknap = pygame.image.load("ressources/start.jpg")

    def blitBg(self):
        self.screen.blit(self.bg,(0,0))

    def blitBtn(self):
        self.screen.blit(self.startknap,(self.conf.width/2,self.conf.height/2))