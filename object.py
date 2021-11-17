from pico2d import *
import random
import main_state
import game_framework
from boy import Will

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

