from pico2d import *
import game_world
import enemy
import server


class Grass:
    def __init__(self):
        self.image0 = load_image('resource/background/background_Level01.png')
        self.image1 = load_image('resource/background/backgroundWalls_Level0.png')
        self.level = 0
        server.Hanari_count = 5
        server.slime_count = 2
        server.golem_count = 3
        server.sword_count = 1
        self.image_level1_0 = load_image('resource/background/Dungeon1_Level0_LowerDetail_6.png')
        self.image_level1_1 = load_image('resource/background/Dungeon1_Level2_LowerDetail_5.png')
        self.image_level1_2 = load_image('resource/background/Dungeon1_Level2_LowerDetail_4.png')

        self.image_level2_0 = load_image('resource/background/Dungeon1_Level0_LowerDetail_7.png')
        self.image_level2_1 = load_image('resource/background/Dungeon1_Level2_LowerDetail_1.png')
        self.image_level2_2 = load_image('resource/background/Dungeon1_Level2_LowerDetail_2.png')



    def update(self, mx=0, my=0):
        pass

    def enter(self):
        if self.level ==0:
            server.Hanari_count =5
            server.slime_count =2
            server.golem_count =3
            server.sword_count =1
        elif self.level == 1:
            server.Hanari_count = 0
            server.slime_count = 0
            server.golem_count = 0
            server.sword_count = 0


    def draw(self):
        if self.level == 0:
            self.image0.clip_draw(0, 0, 509, 294, 600, 300, 1200, 600)
            self.image_level2_0.clip_draw(0, 0, 176, 159, 600, 300, 1200, 600)
            self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
            self.image_level1_0.clip_draw(0, 0, 80, 53, 800, 300)
            self.image_level1_0.clip_draw(0, 0, 80, 53, 600, 400)
            self.image_level1_0.clip_draw(0, 0, 80, 53, 680, 453)
            self.image_level1_0.clip_draw(0, 0, 80, 53, 300, 200)
            self.image_level1_2.clip_draw(0, 0, 80, 53, 300, 200)
            self.image_level1_2.clip_draw(0, 0, 80, 53, 520, 350)
            self.image_level1_1.clip_draw(0, 0, 54, 75, 600, 400)

        elif self.level == 1:
            self.image0.clip_draw(0, 0, 509, 294, 600, 300, 1200, 600)
            self.image_level2_0.clip_draw(0, 0, 176, 159, 600, 300, 1200, 600)
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
        if self.level == 0:
            self.image0.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
            self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
        elif self.level == 1:
            self.image0.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
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
        if self.level == 0:
            self.image1.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
            self.image0.clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
        elif self.level == 1:
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

