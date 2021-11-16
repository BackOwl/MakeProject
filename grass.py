from pico2d import *

class Grass:
    def __init__(self):
        self.image0 = load_image('resource/background/background_Level0.png')
        self.image1 = load_image('resource/background/backgroundWalls_Level0.png')

    def update(self):
        pass


    def draw(self):
        self.image0.clip_draw(0, 0, 580, 360, 600, 300, 1200, 600)
        # self.image1.draw(600, 340)
        self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)

    # fill here
    def get_bb(self):
        return 0, 0, 0, 0

