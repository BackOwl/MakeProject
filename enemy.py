from pico2d import *
import random
class BabySlime:
    def __init__(self):
        self.x, self.y = random.randint(100, 400), 90
        self.frame = 0
        self.now_max_frame = 5
        self.walk ={}
        self.attackUp,self.attackLeft,self.attackRight,self.attackDown={},{},{},{}
        self.state = 'walk'

        for i in range(0, 5):
            self.walk[i] = load_image('resource/enemy/orangeslime/forest_babyslime_walk_%d.png' %(i+1))
        for i in range(0, 9):
            self.attackUp[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Up_%d.png' %(i+1))
            self.attackDown[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Down_%d.png' % (i + 1))
            self.attackRight[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Right_%d.png' % (i + 1))
            self.attackLeft[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Left_%d.png' % (i + 1))


    def update(self):
        #global now_max_frame

        self.frame = (self.frame + 1) % self.now_max_frame

    def draw(self):
        self.walk[self.frame].clip_draw(0,0, 35, 35, self.x, self.y)
        #self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)

class Stone:
    def __init__(self):
        self.x, self.y = random.randint(100, 400), 90
        self.frame = 0
        self.now_max_frame = 7
        self.walk ={}
        self.attackUp, self.attackLeft, self.attackRight, self.attackDown = {}, {}, {}, {}
        self.walkUp, self.walkLeft, self.walkRight, self.walkDown = {}, {}, {}, {}
        self.state = 'walk'
        for i in range(0, 7):
            self.walkUp[i] = load_image('resource/enemy/stone/enemies_golem butler_ floating_ up_0%d.png' % i)
            self.walkDown[i] = load_image('resource/enemy/stone/enemies_golem butler _floating_ down_0%d.png' % i)
            self.walkRight[i] = load_image('resource/enemy/stone/enemies_golem butler_floating_ right_0%d.png' % i)
            self.walkLeft[i] = load_image('resource/enemy/stone/enemies_golem butler_floating_ left_0%d.png' % i)

        for i in range(0, 8):
            self.attackUp[i] = load_image('resource/enemy/stone/enemies_golem butler_attack_up_%d.png' %(i+1))
            self.attackDown[i] = load_image('resource/enemy/stone/enemies_golem butler_attack_down_%d.png' % (i +1))
            self.attackRight[i] = load_image('resource/enemy/stone/enemies_golem butler_attack_right_%d.png' % (i +1))
            self.attackLeft[i] = load_image('resource/enemy/stone/enemies_golem butler_attack_left_%d.png' % (i +1))

    def update(self):
        #global now_max_frame
        self.frame = (self.frame + 1) % self.now_max_frame

    def draw(self):
        self.walkLeft[self.frame].clip_draw(0,0, 55, 55, self.x, self.y)
        #self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)

#'''
open_canvas(600, 340)

babyslime = BabySlime()
stone = Stone()
running = True
while running:
    clear_canvas()
    babyslime.update()
    babyslime.draw()
    stone.update()
    stone.draw()

    update_canvas()

    delay(0.1)

close_canvas()
#'''