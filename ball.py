import random
from pico2d import *
import game_world
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
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('bird100x100x14.png')
        self.x, self.y= random.randint(0, 1600-1), random.randint(100,200)
        self.dir = 1
        self.big = random.randint(50,100)
        self.fall_speed = self.y %100
        self.frame = 0

    def get_bb(self):
        pass
    #return 0,0,0,0

    def draw(self):
        #self.image.draw(self.x, self.y)
        self.image.clip_draw(int(self.frame) * 100, 0, 100,  100, self.x, self.y, self.big,self.big)
        # fill here for draw

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir*self.fall_speed * game_framework.frame_time
        if self.x < self.big or self.x > 1600 - self.big:
            self.dir *=-1

    #fill here for def stop


# fill here
# class BigBall