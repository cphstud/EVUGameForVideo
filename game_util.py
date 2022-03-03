import pygame

class GameUtil():
    def __init__(self,settings,screen):
        self.screen=screen
        self.conf=settings
        self.startbtn=pygame.image.load("ressources/start.jpg")
        self.bg=pygame.image.load("ressources/bluebg.png")

    def blit_btn(self):
        self.screen.blit(self.startbtn,(self.conf.width/2,self.conf.height/2))

    def blit_bg(self):
        self.screen.blit(self.bg,(0,0))
