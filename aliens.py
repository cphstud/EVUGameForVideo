from random import randint
class Aliens():

    def __set__(self, settings):
        self.list_of_aliens=self.init_targets()
        self.s=settings

    def init_targets(self):
        aliens = []
        for tal in range(self.s.num_of_aliens):
            xpos = randint(self.s.delta, self.s.width - self.s.delta)
            ypos = 0
            speed = randint(1, 4)
            alien_rect = alien_img.get_rect(center=(xpos, ypos))
            alien = {"image": alien_img, "rect": alien_rect, "name": f"alien_{tal}", "counter": 0, "speed": speed}
            aliens.append(alien)
        return aliens