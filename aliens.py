from random import randint
from alien import Alien

class Aliens():
    def __init__(self, settings,screen):
        self.conf=settings
        self.screen=screen
        self.list_of_aliens=self.init_targets()

    def init_targets(self):
        aliens = []
        for tal in range(self.conf.num_of_aliens):
            xpos = randint(self.conf.delta, self.conf.width - self.conf.delta)
            ypos = 0
            speed = randint(1, 4)
            alien=Alien(self.screen,self.conf,xpos=xpos,ypos=ypos,speed=speed)
            aliens.append(alien)
        return aliens
