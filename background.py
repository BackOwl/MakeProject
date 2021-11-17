from pico2d import *
import random
import game_framework

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

class greenwater:
    image = None
    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.now_max_frame = 5
        self.level1 = {}
        self.level2 = {}
        if greenwater.image ==None:
            for i in range(0, 16):
                self.level1[i] = load_image('resource/background/main/Main_menu_1_%d.png' % (i + 1))
                self.level2[i] = load_image('resource/background/main/Main_menu_2_%d.png' % (i + 1))
    def update(self, mx= 0, my=0):
        # global now_max_frame
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
    def draw(self):
        self.level2[int(self.frame)].clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)
        self.level1[int(self.frame)].clip_draw(0, 0, 640, 360, 600, 300, 1200, 600)

        # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)

