import pygame
from random import randint
class Alien():
    def __init__(self,screen, settings, **kwargs):
        self.screen=screen
        self.conf=settings
        self.xpos=randint(self.conf.delta, self.conf.width-self.conf.delta)
        self.ypos=0
        self.counter=0
        self.speed=kwargs['speed']
        self.name=kwargs['name']
        self.img=pygame.image.load("ressources/alien.bmp")
        self.rect=self.img.get_rect()


    def move_down(self):
       pass


    def blitme(self):
        self.screen.blit(self.img,self.rect)
