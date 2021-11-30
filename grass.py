from pico2d import *
import game_world
import enemy
import server


class Grass:
    def __init__(self):
        self.image0 = load_image('resource/background/background_Level003.png')
        self.image1 = load_image('resource/background/backgroundWalls_Level0.png')
        server.Hanari_count = 5
        server.slime_count = 0
        server.golem_count = 0
        server.sword_count = 1
        self.image_level2_0 = load_image('resource/background/Dungeon1_Level0_LowerDetail_7.png')
        self.tile1 = load_image('resource/background/background_Level05.png')
        self.tile2 = load_image('resource/background/background_Level00.png')

    def update(self, mx=0, my=0):
        pass

    def enter(self):
        if server.grass_level ==0:
            server.Hanari_count =5
            server.slime_count =2
            server.golem_count =3
            server.sword_count =1
        elif server.grass_level == 1:
            server.Hanari_count = 0
            server.slime_count = 0
            server.golem_count = 0
            server.sword_count = 0
            server.clampy = 250


    def draw(self):
        if server.grass_level == 0:
            self.image0.clip_draw(0, 0, 509, 294, 600, 300, 1018, 488)
            self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)


        elif server.grass_level == 1:
            self.tile2.clip_draw(0, 0, 509, 294, 600, 300, 1100, 600)
            self.tile1.clip_draw(0, 0, 509, 294, 600, 300, 1100, 600)
            self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)


    # fill here
    def get_bb(self):
        return 0, 0, 0, 0

class Level2:
    def __init__(self):
        self.image0 = load_image('resource/background/Dungeon4_Level0_Background.png')
        self.image1 = load_image('resource/background/backgroundWalls_Level2.png')

    def update(self, mx=0, my=0):
        pass

    def draw(self):
        if server.grass_level == 0:
            self.image0.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
            self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
        elif server.grass_level == 1:
            self.image0.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
            self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)

    # fill here
    def enter(self):
        if server.grass_level ==0:
            server.Hanari_count =0
            server.slime_count =0
            server.golem_count =0
            server.sword_count =0
            server.clampy = 100
        elif server.grass_level == 1:
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

    def update(self, mx=0, my=0):
        pass

    def draw(self):
        if server.grass_level == 0:
            self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
            self.image0.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
        elif server.grass_level == 1:
            self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
            self.image0.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)

    # fill here
    def enter(self):
        if server.grass_level ==0:
            server.Hanari_count =0
            server.slime_count =0
            server.golem_count =0
            server.sword_count =0
        elif server.grass_level == 1:
            server.Hanari_count = 0
            server.slime_count = 0
            server.golem_count = 0
            server.sword_count = 0
    def get_bb(self):
        return 0, 0, 0, 0

