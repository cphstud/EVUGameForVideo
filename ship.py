import pygame


class Ship():
    def __init__(self,settings,screen):
        self.screen=screen
        self.conf=settings
        self.ship_img = pygame.image.load("ressources/ship.bmp")
        self.rect=self.ship_img.get_rect()

    def shipCollision(self,other):
        retVal=0
        if (self.rect.colliderect(other)):
            retVal=1
        return retVal

    def move_ship(self,movement):
        self.rect.center=movement

    def blitme(self):
        self.screen.blit(self.ship_img,self.rect)
