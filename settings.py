class Settings():
    def __init__(self):
        self.start_game=False
        #dimensioner
        self.width=600
        self.height=800
        self.delta=self.width/20
        self.font_size=32

        self.frequency=10
        self.fr=60
        self.num_of_aliens=10

        #farver
        self.white=(255,255,255)
        self.black=(0,0,0)
