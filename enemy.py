from pico2d import *
import random
class Slime:
    def __init__(self):
        self.x, self.y = random.randint(100, 400), 90
        self.frame = 0
        self.image ={}
        #self.image0 = load_image('resource/enemy/orangeslime/forest_babyslime_walk_1.png')
        #self.image1 = load_image('resource/Will/Will_Idle35.35.png')
        self.image[0] = load_image('resource/enemy/orangeslime/forest_babyslime_walk_1.png')
        self.image[1] = load_image('resource/enemy/orangeslime/forest_babyslime_walk_2.png')
        self.image[2] = load_image('resource/enemy/orangeslime/forest_babyslime_walk_3.png')
        self.image[3] = load_image('resource/enemy/orangeslime/forest_babyslime_walk_4.png')
        self.image[4] = load_image('resource/enemy/orangeslime/forest_babyslime_walk_5.png')

    def update(self):
        #global now_max_frame
        self.now_max_frame =5
        self.frame = (self.frame + 1) % self.now_max_frame

    def draw(self):
        self.image[self.frame].clip_draw(0,0, 35, 35, self.x, self.y)
        #self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)


open_canvas(600, 340)

slime = Slime()
running = True
while running:
    slime.update()
    slime.draw()

    update_canvas()

    delay(0.1)