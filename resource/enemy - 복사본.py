from pico2d import *
import random


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

    def update(self, mx, my):
        # global now_max_frame
        self.frame = (self.frame + 1) % self.now_max_frame
        self.x, self.y, self.state = check_attack(mx, my, self.x, self.y, 30, 10)
        self.attack_state = check_state(mx, my, self.x, self.y, self.state)

    def draw(self):
        if self.state == True:
            self.walk[self.frame].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
        else:
            if self.attack_state =='Up':
                self.attackUp[self.frame].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
            elif self.attack_state == 'Down':
                self.attackDown[self.frame].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
            elif self.attack_state == 'Right':
                self.attackRight[self.frame].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
            elif self.attack_state == 'Left':
                self.attackLeft[self.frame].clip_draw(0, 0, 35, 35, self.x, self.y, 20, 20)
        # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)


class Stone:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 200), random.randint(100, 300)
        self.frame = 0
        self.now_max_frame = 7
        self.walk = {}
        self.attackUp, self.attackLeft, self.attackRight, self.attackDown = {}, {}, {}, {}
        self.walkUp, self.walkLeft, self.walkRight, self.walkDown = {}, {}, {}, {}
        self.state = 'walk'
        if Stone.image == None:
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

    def update(self, mx, my):
        # global now_max_frame
        self.frame = (self.frame + 1) % self.now_max_frame
        self.x, self.y, self.state = check_attack(mx, my, self.x, self.y, 70, 8)
        self.attack_state = check_state(mx, my, self.x, self.y, False)

    def draw(self):
        if self.state == True:
            if self.attack_state == 'Up':
                self.walkUp[self.frame].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Down':
                self.walkDown[self.frame].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Right':
                self.walkRight[self.frame].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Left':
                self.walkLeft[self.frame].clip_draw(0, 0, 55, 60, self.x, self.y)
        else:
            if self.attack_state == 'Up':
                self.attackUp[self.frame].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Down':
                self.attackDown[self.frame].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Right':
                self.attackRight[self.frame].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Left':
                self.attackLeft[self.frame].clip_draw(0, 0, 55, 60, self.x, self.y)
        # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)


def check_attack(Nx, Ny, x, y, want, speed):
    # ????????? ???????????? ????????? want???????????? x,y????????? ???????????? speed ??? ????????????
    # x, y??? ?????????????????? ??????, ????????? ????????? x,y??? Nx, Ny??? ?????????
    dx = Nx - x
    dy = Ny - y
    check = (dx) * (dx) + (dy) * (dy)
    if dx >= 0:
        lx = 1
    else:
        lx = -1
    if dy >= 0:
        ly = 1
    else:
        ly = -1
    want = want * want

    if want <= check:  # ????????? ??????
        state = True
        A = dy/dx #y = Ax + B
        if A>=1:
            A =1
        elif A <-1:
            A = -1
        B = (y-A*x)
        x= x+ (speed/5)*lx
        y = A*x +B

    else:
        state = False
    return x, y, state


def check_state(Nx, Ny, x, y, state):
    # ?????? ??? ?????? ????????? ????????? ???????????? ???????????? ?????? ????????? ????????? ????????????
    # state = False?????? ????????? ???????????? ?????????.
    attack_state = 'Up'
    if state == False:
        dx = Nx - x
        dy = Ny - y
        xx = dx * dx
        yy = dy * dy
        if xx >= yy:
            if dx >= 0:
                # ->
                attack_state = 'Right'
            else:
                attack_state = 'Left'
        elif xx < yy:
            if dy >= 0:
                attack_state = 'Up'
            else:
                attack_state = 'Down'
    return attack_state


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
