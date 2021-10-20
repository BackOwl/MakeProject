from pico2d import *
import random

class BabySlime:
    def __init__(self):
        self.x, self.y = random.randint(300, 400), random.randint(100, 300)
        self.frame = 0
        self.now_max_frame = 5
        self.walk = {}
        self.attackUp, self.attackLeft, self.attackRight, self.attackDown = {}, {}, {}, {}
        self.state = 'walk'

        for i in range(0, 5):
            self.walk[i] = load_image('resource/enemy/orangeslime/forest_babyslime_walk_%d.png' % (i + 1))
        for i in range(0, 9):
            self.attackUp[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Up_%d.png' % (i + 1))
            self.attackDown[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Down_%d.png' % (i + 1))
            self.attackRight[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Right_%d.png' % (i + 1))
            self.attackLeft[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Left_%d.png' % (i + 1))

    def update(self,mx,my):
        # global now_max_frame
        self.frame = (self.frame + 1) % self.now_max_frame
        self.x, self.y ,self.state = check_attack(mx,my,self.x,self.y,30,6)

    def draw(self):
        if self.state ==True:
            self.walk[self.frame].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
        else:
            self.attackUp[self.frame].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
        # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)


class Stone:
    def __init__(self):
        self.x, self.y = random.randint(100, 200), random.randint(100, 300)
        self.frame = 0
        self.now_max_frame = 7
        self.walk = {}
        self.attackUp, self.attackLeft, self.attackRight, self.attackDown = {}, {}, {}, {}
        self.walkUp, self.walkLeft, self.walkRight, self.walkDown = {}, {}, {}, {}
        self.state = 'walk'
        for i in range(0, 7):
            self.walkUp[i] = load_image('resource/enemy/stone/enemies_golem butler_ floating_ up_0%d.png' % i)
            self.walkDown[i] = load_image('resource/enemy/stone/enemies_golem butler _floating_ down_0%d.png' % i)
            self.walkRight[i] = load_image('resource/enemy/stone/enemies_golem butler_floating_ right_0%d.png' % i)
            self.walkLeft[i] = load_image('resource/enemy/stone/enemies_golem butler_floating_ left_0%d.png' % i)

        for i in range(0, 8):
            self.attackUp[i] = load_image('resource/enemy/stone/enemies_golem butler_attack_up_%d.png' % (i + 1))
            self.attackDown[i] = load_image('resource/enemy/stone/enemies_golem butler_attack_down_%d.png' % (i + 1))
            self.attackRight[i] = load_image('resource/enemy/stone/enemies_golem butler_attack_right_%d.png' % (i + 1))
            self.attackLeft[i] = load_image('resource/enemy/stone/enemies_golem butler_attack_left_%d.png' % (i + 1))

    def update(self,mx,my):
        # global now_max_frame
        self.frame = (self.frame + 1) % self.now_max_frame
        self.x,self.y,self.state = check_attack(mx, my, self.x, self.y, 70, 8)

    def draw(self):
        if self. state == True:
            self.walkLeft[self.frame].clip_draw(0, 0, 55, 55, self.x, self.y)
        else:
            self.attackUp[self.frame].clip_draw(0, 0, 55, 55, self.x, self.y)
        # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)


def check_attack(Nx, Ny, x, y, want, speed):
    # 주인공 캐릭터와 거리가 want될떄까지 x,y축으로 랜덤으로 speed 씩 다가간다
    # x, y는 몬스터로부터 받고, 주인공 캐릭터 x,y를 Nx, Ny로 잡는다
    dx = Nx - x
    dy = Ny - y
    check = (dx) * (dx) + (dy) * (dy)
    if dx >= 0:
        dx = 1
    else:
        dx = -1
    if dy >= 0:
        dy = 1
    else:
        dy = -1
    want = want * want
    if want <= check:  # 거리가 멀때
        state = True
        dir = random.randint(0, 3)  # 0 x 1 y 2 xy
        if dir ==0:
            x= x+(dx*speed)
        elif dir == 1:
            y= y+(dy*speed)
        elif dir ==2:
            x = x + (dx * speed)
            y = y + (dy * speed)
    else:
        state = False
    return x, y,state



'''
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
'''
