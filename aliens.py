from random import randint
from alien import Alien

class Aliens():

    def __init__(self, settings, screen):
        self.screen=screen
        self.conf=settings
        self.list_of_aliens=self.init_targets()

    def init_targets(self):
        #screen, settings, **kwargs
        aliens = []
        for tal in range(self.conf.num_of_aliens):
            speed = randint(1, 4)
            alien=Alien(self.screen,self.conf,name=f"alien_{tal}",mspeed=speed)
            aliens.append(alien)
        return aliens