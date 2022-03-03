import pygame
class Ship():
    def __init__(self,settings,screen):
        self.conf=settings
        self.screen=screen

        self.img=pygame.image.load("ressources/ship.bmp")
        self.rect=self.img.get_rect()

    def move_ship(self,movement):
        self.rect.center=movement

    def blitme(self):
        self.screen.blit(self.img,self.rect)


