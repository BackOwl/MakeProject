from pico2d import *
import random
import game_framework
import main_state
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
        self.x, self.y = random.randint(300, 1000), random.randint(100, 500)
        self.frame = 0
        self.now_max_frame = 5
        self.walk = {}
        self.attackUp, self.attackLeft, self.attackRight, self.attackDown = {}, {}, {}, {}
        self.state = 'walk'
        self.random= random.randint(0,5)
        if BabySlime.image ==None:
            for i in range(0, 5):
                self.walk[i] = load_image('resource/enemy/orangeslime/forest_babyslime_walk_%d.png' % (i + 1))
            for i in range(0, 9):
                self.attackUp[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Up_%d.png' % (i + 1))
                self.attackDown[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Down_%d.png' % (i + 1))
                self.attackRight[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Right_%d.png' % (i + 1))
                self.attackLeft[i] = load_image('resource/enemy/orangeslime/ForestBabySlime_Attack_Left_%d.png' % (i + 1))

    def update(self, will):
        # global now_max_frame
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.now_max_frame
        self.x, self.y, self.state = check_attack(will.x, will.y, self.x, self.y, 30+self.random, 10)
        if self.state == False:
            if main_state.collide(will, self) == False:
                will.attacked()

        self.attack_state = check_state(will.x, will.y, self.x, self.y, self.state)
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


class Stone:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(300, 1000), random.randint(100, 500)
        self.frame = 0
        self.now_max_frame = 7
        self.walk = {}
        self.attackUp, self.attackLeft, self.attackRight, self.attackDown = {}, {}, {}, {}
        self.walkUp, self.walkLeft, self.walkRight, self.walkDown = {}, {}, {}, {}
        self.state = 'walk'
        self.random = random.randint(0, 10)
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

    def update(self, will):
        # global now_max_frame
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.now_max_frame
        self.x, self.y, self.state = check_attack(will.x, will.y, self.x, self.y, 50+self.random, 20)

        self.attack_state = check_state(will.x, will.y,self.x, self.y, False)
        if self.state == False:
            if main_state.collide(will, self)==False:
                will.attacked()

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw(self):
        if self.state == True:
            if self.attack_state == 'Up':
                self.walkUp[int(self.frame)].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Down':
                self.walkDown[int(self.frame)].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Right':
                self.walkRight[int(self.frame)].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Left':
                self.walkLeft[int(self.frame)].clip_draw(0, 0, 55, 60, self.x, self.y)
        else:
            if self.attack_state == 'Up':
                self.attackUp[int(self.frame)].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Down':
                self.attackDown[int(self.frame)].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Right':
                self.attackRight[int(self.frame)].clip_draw(0, 0, 55, 60, self.x, self.y)
            elif self.attack_state == 'Left':
                self.attackLeft[int(self.frame)].clip_draw(0, 0, 55, 60, self.x, self.y)
        # self.image0.clip_draw(0, 0, 35, 35, self.x, self.y)
        draw_rectangle(*self.get_bb())


def check_attack(Nx, Ny, x, y, want, speed):
    # 주인공 캐릭터와 거리가 want될떄까지 x,y축으로 랜덤으로 speed 씩 다가간다
    # x, y는 몬스터로부터 받고, 주인공 캐릭터 x,y를 Nx, Ny로 잡는다
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

    if want <= check:  # 거리가 멀때
        state = True
        A = dy/dx #y = Ax + B
        if A>=1:
            A =1
        elif A <-1:
            A = -1
        B = (y-A*x)
        x= x+ (speed* game_framework.frame_time)*lx
        y = A*x +B

    else:
        state = False
    return x, y, state


def check_state(Nx, Ny, x, y, state):
    # 계산 후 현재 서있는 방향을 기준으로 바라보는 공격 방향을 정해서 내보낸다
    # state = False일때 방향이 정해져서 멈춘다.
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
