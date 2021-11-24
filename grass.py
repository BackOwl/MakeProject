from pico2d import *
import game_world
import enemy
import server


class Grass:
    def __init__(self):
        self.image0 = load_image('resource/background/background_Level0.png')
        self.image1 = load_image('resource/background/backgroundWalls_Level0.png')
        self.level = 0

    def update(self, mx=0, my=0):
        pass

    def enter(self):
        if self.level ==0:
            server.Hanari_count =0
            server.slime_count =0
            server.golem_count =0
            server.sword_count =0
        elif self.level == 1:
            server.Hanari_count = 0
            server.slime_count = 0
            server.golem_count = 0
            server.sword_count = 0


    def draw(self):
        self.image0.clip_draw(0, 0, 580, 360, 600, 300, 1200, 600)
        # self.image1.draw(600, 340)
        self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)

    # fill here
    def get_bb(self):
        return 0, 0, 0, 0

class Level2:
    def __init__(self):
        self.image0 = load_image('resource/background/Dungeon4_Level0_Background.png')
        self.image1 = load_image('resource/background/backgroundWalls_Level2.png')
        self.level =0

    def update(self, mx=0, my=0):
        pass

    def draw(self):
        self.image0.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
        # self.image1.draw(600, 340)
        self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)

    # fill here
    def enter(self):
        if self.level ==0:
            server.Hanari_count =0
            server.slime_count =0
            server.golem_count =0
            server.sword_count =0
        elif self.level == 1:
            server.Hanari_count = 0
            server.slime_count = 0
            server.golem_count = 0
            server.sword_count = 0
    def get_bb(self):
        return 0, 0, 0, 0
class Level3:
    def __init__(self):
        self.image0 = load_image('resource/background/background_Level_0_Walls.png')
        self.image1 = load_image('resource/background/background_Level0.png')
        self.level=0

    def update(self, mx=0, my=0):
        pass

    def draw(self):
        # self.image1.draw(600, 340)
        self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
        self.image0.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)

    # fill here
    def enter(self):
        if self.level ==0:
            server.Hanari_count =0
            server.slime_count =0
            server.golem_count =0
            server.sword_count =0
        elif self.level == 1:
            server.Hanari_count = 0
            server.slime_count = 0
            server.golem_count = 0
            server.sword_count = 0
    def get_bb(self):
        return 0, 0, 0, 0

