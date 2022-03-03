from random import randint
from alien import Alien
class Aliens():

    def __init__(self, screen,settings):
        self.screen=screen
        self.list_of_aliens=self.init_targets()
        self.s=settings

    def init_targets(self):
        #screen, settings, **kwargs
        aliens = []
        for tal in range(self.s.num_of_aliens):
            speed = randint(1, 4)
            alien=Alien(self.screen,self.s,{"name":f"alien_{tal}","speed":speed})
            aliens.append(alien)
        return aliens