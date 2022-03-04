import pygame


class Alien():
    def __init__(self,screen,settings,**kwargs):
        self.xpos=kwargs.get("xpos")
        self.ypos=kwargs.get("ypos")
        self.speed=kwargs.get("speed")
        self.screen=screen
        self.conf=settings
        self.alien_img=pygame.image.load("ressources/alien.bmp")
        self.alien_rect=self.alien_img.get_rect(center=(self.xpos,self.ypos))


    def killme(self):
        self.alien_rect.centerx = self.conf.width + 200

    def blitme(self):
        self.screen.blit(self.alien_img,self.alien_rect)