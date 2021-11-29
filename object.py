from pico2d import *
import random
import main_state
import game_framework
from boy import Will
import server

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

#will = Will()

class Hanari:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(300, 400), random.randint(100, 300)
        self.random = random.randint(0,1)
        self.now_max_frame = 5
        self.walk1 = {}
        self.walk2 = {}
        self.broken ={}
        self.attackUp, self.attackLeft, self.attackRight, self.attackDown = {}, {}, {}, {}
        self.state = 'walk'
        if Hanari.image ==None:
            self.walk1 = load_image('resource/background/object/Dungeon1_Breakable_1.png')
            self.walk2 = load_image('resource/background/object/Dungeon1_Breakable_2.png')
            self.broken = load_image('resource/background/object/Dungeon1_Breakable_Rest.png')
    def update(self, will):
        # global now_max_frame
        if main_state.collide(will,self)==True:
            self.state = 'break'
        #self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.now_max_frame

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 10, self.y + 15
    def draw(self):
        #self.walk1.draw(100,190)
        if self.state =='walk':
            if self.random ==1:
                self.walk1.clip_draw(0, 0, 26, 35, self.x, self.y )
            else:
                self.walk2.clip_draw(0, 0, 26, 35, self.x, self.y)
        elif self.state == 'break':
            self.broken.clip_draw(0, 0, 26, 35, self.x, self.y)
            # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)
            draw_rectangle(*self.get_bb())

class Sword:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(300, 900), random.randint(100, 400)
        self.now_max_frame = 3
        self.walk1 = {}
        self.frame=0
        self.broken ={}
        self.attackUp, self.attackLeft, self.attackRight, self.attackDown = {}, {}, {}, {}
        self.state = 'walk'
        if Hanari.image ==None:
            self.walk1 = load_image('resource/background/object/Dungeon1_BreakableStuff_8.png')
            self.broken[0] = load_image('resource/background/object/Dungeon1_BreakableStuff_9.png')
            self.broken[1] = load_image('resource/background/object/Dungeon1_BreakableStuff_Particle_3.png')
            self.broken[2] = load_image('resource/background/object/Dungeon1_BreakableStuff_Particle_4.png')
    def update(self, will):
        # global now_max_frame
        if main_state.collide(will,self)==True:
            self.state = 'break'
            if self.state == 'break':
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.now_max_frame
                if self.frame ==2:
                    self.frame =2

    def get_bb(self):
        return self.x - 10, self.y - 20, self.x + 10, self.y + 20
    def draw(self):
        #self.walk1.draw(100,190)
        if self.state =='walk':
            self.walk1.clip_draw(0, 0, 17, 29, self.x, self.y )
        elif self.state == 'break':
            self.broken[int(self.frame)].clip_draw(0, 0, 17, 29, self.x, self.y)
            # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)
            draw_rectangle(*self.get_bb())
class Door:
    image = None
    def __init__(self,state):
        if state == 'up':
            self.x, self.y = 600,550
            self.now_radian = 0.0
        elif state == 'down':
            self.x, self.y = 600, 50
            self.now_radian = 3.14
        elif state == 'left':
            self.x, self.y = 100, 300
            self.now_radian = 1.57
        elif state =='right':
            self.x, self.y = 1100, 300
            self.now_radian = 4.71
        self.now_max_frame = 11
        self.frame=0
        self.state = 'walk'
        if Door.image ==None:
            self.walk1 = load_image('resource/background/door.png')

    def update(self, will):
        # global now_max_frame
        if main_state.collide(will,self)==True and will.doing_count['key_f']:
            self.state = 'break'
        if self.state == 'break':
            self.frame = ((self.frame +1) % self.now_max_frame)
            delay(0.05)
            if self.frame >= 10:
                self.frame = 10
                self.state = 'walk'
                if server.grass_level == 0:
                    server.grass_level = 1
                elif server.grass_level == 1:
                    server.grasslevel += 1
                    server.grass_level = 0
                print(server.grass_level)
                server.grass.enter()

                main_state.exit()
                game_framework.run(main_state)

    def get_bb(self):
        return self.x - 75, self.y - 75, self.x + 75, self.y + 75
    def draw(self):
        #self.walk1.draw(100,190)
        if self.now_radian >0:
            self.walk1.clip_composite_draw(130*self.frame, 0, 130, 130, self.now_radian,'',self.x, self.y,195,195)
            # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)
        else:
            self.walk1.clip_draw(130 * self.frame, 0, 130, 130, self.x, self.y,195,195)
        draw_rectangle(*self.get_bb())


