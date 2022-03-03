class GameConfig():
    def __init__(self):
        self.width=600
        self.height=800
        self.delta=self.width/25
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.green=(0,128,0)
        self.blue=(0,191,255)

    def get_width(self):
        return self.width
