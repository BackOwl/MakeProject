from pico2d import *
import random
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

class BabySlime:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(300, 400), random.randint(100, 300)
        self.frame = 0
        self.now_max_frame = 5
        self.walk = {}
        self.attackUp, self.attackLeft, self.attackRight, self.attackDown = {}, {}, {}, {}
        self.state = 'walk'
        if BabySlime.image ==None:
            for i in range(0, 5):
                self.walk[i] = load_image('resource/enemy/orangeslime/forest_babyslime_walk_%d.png' % (i + 1))
            for i in range(0, 9):
                self.attackUp[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Up_%d.png' % (i + 1))
                self.attackDown[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Down_%d.png' % (i + 1))
                self.attackRight[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Right_%d.png' % (i + 1))
                self.attackLeft[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Left_%d.png' % (i + 1))

    def update(self, mx= 0, my=0):
        # global now_max_frame
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.now_max_frame
        self.x, self.y, self.state = check_attack(mx, my, self.x, self.y, 30, 10)
        self.attack_state = check_state(mx, my, self.x, self.y, self.state)
    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
    def draw(self):
        if self.state == True:
            self.walk[int(self.frame)].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
        else:
            if self.attack_state =='Up':
                self.attackUp[int(self.frame)].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
            elif self.attack_state == 'Down':
                self.attackDown[int(self.frame)].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
            elif self.attack_state == 'Right':
                self.attackRight[int(self.frame)].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
            elif self.attack_state == 'Left':
                self.attackLeft[int(self.frame)].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
        # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)
        draw_rectangle(*self.get_bb())

