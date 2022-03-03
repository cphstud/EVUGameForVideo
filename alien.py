import pygame
from random import randint
class Alien():
    def __init__(self,screen, settings, **kwargs):
        self.screen=screen
        self.conf=settings
        self.xpos=randint(self.conf.delta, self.conf.width-self.conf.delta)
        self.ypos=0
        self.counter=0
        self.speed=kwargs.get('mspeed')
        self.name=kwargs.get('name')
        self.img=pygame.image.load("ressources/alien.bmp")
        self.rect=self.img.get_rect(center=(self.xpos,self.ypos))


    def move_down(self):
        self.rect.centery+=self.speed

    def kill(self):
        self.xpos=self.conf.width+100

    def blitme(self):
        self.screen.blit(self.img,self.rect)
