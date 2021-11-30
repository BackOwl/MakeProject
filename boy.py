import game_framework
from pico2d import *
from ball import Ball
import server
import main_state

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,UP_DOWN, DOWN_DOWN,DOWN_UP,UP_UP,SPACE_DOWN, JUMP_TIMER \
    ,ATTACK_DOWN,ATTACK_UP,DEAD_HP,CHANGE_SWORD,KEEPRUN,KEY_F= range(16)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYDOWN, SDLK_q):ATTACK_DOWN,
    (SDL_KEYDOWN, SDLK_r):CHANGE_SWORD,
    (SDL_KEYDOWN, SDLK_f):KEY_F,

    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,

    #(SDL_KEYUP, SDLK_SPACE): SPACE_UP
    # 공격키 q
    (SDL_KEYUP, SDLK_q):ATTACK_UP

}

# 가만히 10, 굴리기 10, 뛰기 8
# Boy States

class IdleState:

    def enter(will, event):
        if event == RIGHT_DOWN:
            will.velocity_x += RUN_SPEED_PPS
            will.now_max_frame = 8
            will.direction = 3
        elif event == LEFT_DOWN:
            will.direction = 2
            will.now_max_frame = 8
            will.velocity_x -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            will.direction = 0
            will.now_max_frame = 8
            will.velocity_y += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            will.direction = 1
            will.now_max_frame = 8
            will.velocity_y -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            will.now_max_frame = 8#
            will.velocity_x -= RUN_SPEED_PPS
            will.direction = 3
        elif event == LEFT_UP:
            will.now_max_frame = 8#
            will.velocity_x += RUN_SPEED_PPS
            will.direction = 2
        elif event == UP_UP:
            will.now_max_frame = 8#
            will.velocity_y -= RUN_SPEED_PPS
            will.direction = 0
        elif event == DOWN_UP:
            will.velocity_y += RUN_SPEED_PPS
            will.now_max_frame = 8#
            will.direction = 1


    def exit(will, event):
        # if event == SPACE_DOWN: // 방패
            #will.depend()
        pass

    def do(will):
        if will.doing_count["keeprun"]:
            will.doing_count.update(keeprun=False)
        will.frame = (will.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % will.now_max_frame


    def draw(will):
        will.image1.clip_draw(int(will.frame)* 35, will.direction * 35, 35, 35, will.x, will.y)
        if will.attack_score ==1:
            will.attack_image[will.direction].clip_draw(0, 0, 35, 35, will.x, will.y)
            will.attack_score =0


class RunState:

    def enter(will, event):
        if event == RIGHT_DOWN:
            will.velocity_x += RUN_SPEED_PPS
            will.now_max_frame = 8
            will.direction = 3
        elif event == LEFT_DOWN:
            will.direction = 2
            will.now_max_frame = 8
            will.velocity_x -= RUN_SPEED_PPS
        if event == RIGHT_UP:
            will.now_max_frame = 8#
            will.velocity_x -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            will.now_max_frame = 8#
            will.velocity_x += RUN_SPEED_PPS
        if event == UP_DOWN:
            will.direction = 0
            will.now_max_frame = 8
            will.velocity_y += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            will.direction = 1
            will.now_max_frame = 8
            will.velocity_y -= RUN_SPEED_PPS
        if event == UP_UP:
            will.now_max_frame = 8#
            will.velocity_y -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            will.velocity_y += RUN_SPEED_PPS
            will.now_max_frame = 8#

        will.dir = clamp(-1, will.velocity_x, 1)
        will.dir = clamp(-1, will.velocity_y, 1)
        will.jumptimer = 800

        int = 0
        if event == DOWN_UP or UP_UP or LEFT_UP or RIGHT_UP:
            if event == DOWN_DOWN or UP_DOWN or LEFT_DOWN or RIGHT_DOWN:
                # will.add_event(KEEPRUN)
                # RunState.exit(will, RunState)#
                will.doing_count.update(keeprun=True)
                if event == DOWN_DOWN:
                    will.direction = 1
                if event == UP_DOWN:
                    will.direction = 0
                if event == RIGHT_DOWN:
                    will.direction = 3
                if event == LEFT_DOWN:
                    will.direction = 2
            else: will.doing_count.update(keeprun=False)


        # if will.doing_count["keeprun"]:
        #     will.doing_count.update(keeprun=False)
        #     will.add_event(KEEPRUN)
        # elif not will.doing_count["keeprun"]:
        #     will.add_event(UP_UP)


    def exit(will, event):
        pass
        #if event == SPACE:
            #will.depend() // 방패

    def do(will):
        #will.frame = (will.frame + 1) % 8
        will.frame = (will.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % will.now_max_frame
        will.x = (1 - 0.5) * will.x + 0.5 * (will.x+will.velocity_x*game_framework.frame_time)
        will.y = (1 - 0.5) * will.y + 0.5 * (will.y+will.velocity_y*game_framework.frame_time)
        #will.x += will.velocity * game_framework.frame_time
        will.x = clamp(server.clampx, will.x, 1200 - server.clampx)
        will.y = clamp(server.clampy, will.y, 600 - server.clampy)

    def draw(will):
        will.image0.clip_draw(int(will.frame) * 35, will.direction * 35, 35, 35, will.x, will.y)
        if will.attack_score ==1:
            will.attack_image[will.direction].clip_draw(0, 0, 35, 35, will.x, will.y)
            will.attack_score =0


class JumpState:

    def enter(will, event):
        if event == RIGHT_DOWN:
            will.velocity_x += RUN_SPEED_PPS
            will.now_max_frame = 8
            will.direction = 3
        elif event == LEFT_DOWN:
            will.direction = 2
            will.now_max_frame = 8
            will.velocity_x -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            will.now_max_frame = 8#
            will.velocity_x -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            will.now_max_frame = 8#
            will.velocity_x += RUN_SPEED_PPS
        if event == UP_DOWN:
            will.direction = 0
            will.now_max_frame = 8
            will.velocity_y += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            will.direction = 1
            will.now_max_frame = 8
            will.velocity_y -= RUN_SPEED_PPS
        elif event == UP_UP:
            will.now_max_frame =8#
            will.velocity_y -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            will.velocity_y += RUN_SPEED_PPS
            will.now_max_frame = 10
        will.dir = clamp(-1, will.velocity_x, 1)
        will.dir = clamp(-1, will.velocity_y, 1)
        will.frame = 0
        will.jumptimer =350


    def exit(will, event):
        pass
        #if event == SPACE:
            #will.depend() // 방패

    def do(will):
        #will.frame = (will.frame + 1) % 8
        will.frame = (will.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % will.now_max_frame
        will.x = (1 - 0.5) * will.x + 0.5 * (will.x+will.velocity_x*2*game_framework.frame_time)
        will.y = (1 - 0.5) * will.y + 0.5 * (will.y+will.velocity_y*2*game_framework.frame_time)
        #will.x += will.velocity * game_framework.frame_time
        will.jumptimer -= 5
        if will.jumptimer ==0:
            will.add_event(JUMP_TIMER)

        will.x = clamp(server.clampx, will.x, 1200 - server.clampx)
        will.y = clamp(server.clampy, will.y, 600 - server.clampy)

    def draw(will):
        will.image2.clip_draw(int(will.frame) * 35, will.direction * 35, 35, 35, will.x, will.y)
        if will.attack_score ==1:
            will.attack_image[will.direction].clip_draw(0, 0, 35, 35, will.x, will.y)
            will.attack_score =0

class AttackState:
    def enter(will, event):
        will.jumptimer = 1600
        #if will.state == 'short':self.fullframe = 16
        #elif will.state == 'big':self.fullframe =40


    def exit(will, event):
        #if event == SPACE:
            #will.depend() // 방패
        # server.grasslevel += 1
        # server.grass.enter()
        # main_state.exit()
        # game_framework.run(main_state)
        will.sound_attack.play()
        pass

    def do(will):
            #will.x += will.velocity * game_framework.frame_time
        # if will.state == 'short':
        #     will.frame = (will.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        #     if will.frame > (will.attack_count + 1) * 4 % 16:
        #     else:
        # elif will.state == 'big':
        #     will.frame = (will.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 40
        #     if will.frame > (will.attack_count + 1) * 10 % 40:
        #         will.add_event(ATTACK_UP)
        #         AttackState.exit(will, ATTACK_UP)
        #     else:
        #         will.add_event(ATTACK_DOWN)
        #         AttackState.exit(will, ATTACK_DOWN)
            if will.doing_count["keeprun"]:
                will.doing_count.update(keeprun=False)
            if will.state == 'short':
                if will.attack_count == 1:
                    will.frame = (will.attack_count * 4 + FRAMES_PER_ACTION* ACTION_PER_TIME * game_framework.frame_time) % 16
                    if will.frame > 3:
                        will.doing_count.update(attack=False)
                        attack_count = 0

                elif will.attack_count == 2:
                    will.frame = (will.attack_count * 4 + FRAMES_PER_ACTION* ACTION_PER_TIME * game_framework.frame_time) % 16
                    if will.frame > 7:
                        will.doing_count.update(attack=False)
                        attack_count = 0
                elif will.attack_count == 3:
                    will.frame = (will.attack_count * 4 + FRAMES_PER_ACTION* ACTION_PER_TIME * game_framework.frame_time) % 16
                    if will.frame > 11:
                        will.doing_count.update(attack=False)
                        attack_count = 0
                elif will.attack_count == 4:
                    will.frame = (will.attack_count * 4 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
                    if will.frame > 15:
                        will.doing_count.update(attack=False)
                        attack_count = 0

            elif will.state == 'big':
                if will.attack_count == 1:
                    will.frame = ( will.attack_count * 10 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 40
                    if will.frame > 9:
                        will.doing_count.update(attack=False)
                        attack_count = 0
                elif will.attack_count == 2:
                    will.frame = ( will.attack_count * 10 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 40
                    if will.frame > 19:
                        will.doing_count.update(attack=False)
                        attack_count = 0
                elif will.attack_count == 3:
                    will.frame = (will.attack_count * 10 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 40
                    if will.frame > 29:
                        will.doing_count.update(attack=False)
                        attack_count = 0
                elif will.attack_count == 4:
                    will.frame = (will.attack_count * 10 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 40
                    if will.frame > 39:
                        will.doing_count.update(attack=False)
                        attack_count = 0
            for monster in server.monsters:
                if main_state.attack_collide(monster, will,will.direction):
                    monster.hp -= 1
                    monster.attacked()
                    pass

            will.jumptimer -=5
            if will.jumptimer ==0:
                will.attack_count =0
            will.attack_count %=4

    def draw(will):
        if will.state =='short':#4
            if will.direction ==1:
                will.short_down[int(will.frame)].clip_draw(0, 0, 35, 35, will.x, will.y)
                will.short_solder_down[int(will.frame)].clip_draw(0, 0, 60, 60, will.x, will.y)
            elif will.direction ==2:
                will.short_left[int(will.frame)].clip_draw(0, 0, 35, 35, will.x, will.y)
                will.short_solder_left[int(will.frame)].clip_draw(0, 0, 60, 60, will.x, will.y)
            elif will.direction == 3:
                will.short_right[int(will.frame)].clip_draw(0 , 0, 35, 35, will.x, will.y)
                will.short_solder_right[int(will.frame)].clip_draw(0, 0, 60, 60, will.x, will.y)
            elif will.direction == 0:
                will.short_up[int(will.frame)].clip_draw(0, 0, 35, 35, will.x, will.y)
                will.short_solder_up[int(will.frame)].clip_draw(0, 0, 60, 60, will.x, will.y)

        elif will.state == 'big':#10
            if will.direction == 1:
                will.long_down[int(will.frame)].clip_draw(0, 0, 35, 35, will.x, will.y)
                will.long_toxin_down[int(will.frame)].clip_draw(0, 0, 60, 60, will.x, will.y)
            elif will.direction == 2:
                will.long_left[int(will.frame)].clip_draw(0, 0, 35, 35, will.x, will.y)
                will.long_toxin_left[int(will.frame)].clip_draw(0, 0, 60, 60, will.x, will.y)
            elif will.direction == 3:
                will.long_right[int(will.frame)].clip_draw(0, 0, 35, 35, will.x, will.y)
                will.long_toxin_right[int(will.frame)].clip_draw(0, 0, 60, 60, will.x, will.y)
            elif will.direction == 0:
                will.long_up[int(will.frame)].clip_draw(0, 0, 35, 35, will.x, will.y)
                will.long_toxin_up[int(will.frame)].clip_draw(0, 0, 60, 60, will.x, will.y)
        if will.attack_score ==1:
            will.attack_image[will.direction].clip_draw(0, 0, 35, 35, will.x, will.y)
            will.attack_score =0
        delay(0.1)

class DeadState:
    def enter(will, event):

        pass

    def exit(will, event):
        pass

    def do(will):
        will.frame = (will.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if will.frame >=10:
            will.frame =10


    def draw(will):
        will.die[int(will.frame)].clip_draw(0,0, 35, 35, will.x, will.y)
        delay(0.1)

class ChangeSword:
    def enter(will, event):
        pass

    def exit(will, event):
        pass
    def do(will):
        if will.state == 'big':
            will.state = 'short'
            print(will.state)
        elif will.state == 'short':
            will.state = 'big'
            print(will.state)
    def draw(will):
        pass


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,  SPACE_DOWN: IdleState,
                UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,ATTACK_DOWN: AttackState, ATTACK_UP: RunState,
                DEAD_HP: DeadState,CHANGE_SWORD:ChangeSword,KEEPRUN:RunState,KEY_F:RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE_DOWN: JumpState,
               UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: RunState, DOWN_DOWN: RunState,ATTACK_DOWN: AttackState, ATTACK_UP: RunState,
               DEAD_HP: DeadState,CHANGE_SWORD:ChangeSword,KEEPRUN:RunState,KEY_F:IdleState},
    JumpState: {RIGHT_UP: RunState,LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
                UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,SPACE_DOWN: JumpState,JUMP_TIMER: RunState,
                ATTACK_DOWN: AttackState, ATTACK_UP: RunState,DEAD_HP: DeadState,CHANGE_SWORD:ChangeSword,KEEPRUN:JumpState,KEY_F:RunState},
    AttackState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE_DOWN: JumpState,
                UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: RunState, DOWN_DOWN: RunState,ATTACK_DOWN: AttackState, ATTACK_UP: RunState,
                  DEAD_HP: DeadState,CHANGE_SWORD:ChangeSword,KEEPRUN:AttackState,KEY_F:RunState},
    DeadState:{RIGHT_UP: DeadState, LEFT_UP: DeadState, RIGHT_DOWN: DeadState, LEFT_DOWN: DeadState, SPACE_DOWN: DeadState,
                UP_UP: DeadState, DOWN_UP: DeadState, UP_DOWN: DeadState, DOWN_DOWN: DeadState,ATTACK_DOWN: DeadState, ATTACK_UP: DeadState,
                  DEAD_HP: DeadState,CHANGE_SWORD:DeadState,KEEPRUN:DeadState,KEY_F:DeadState},
    ChangeSword:{RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE_DOWN: RunState,
                UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: RunState, DOWN_DOWN: RunState,ATTACK_DOWN: RunState, ATTACK_UP: IdleState,
                  DEAD_HP: DeadState,CHANGE_SWORD:IdleState,KEEPRUN:RunState,KEY_F:IdleState}

}

class Will:

    def __init__(self):
        self.x, self.y = 200, 300
        # will is only once created, so instance image loading is fine
        self.image0 = load_image('resource/Will/will animation cycle35.35.png')
        self.image1 = load_image('resource/Will/Will_Idle35.35.png')
        self.image2 = load_image('resource/Will/Will_Roll35.35.png')
        self.short_up ={};self.short_down ={};self.short_right ={};self.short_left ={};
        self.short_solder_up = {};self.short_solder_down = {};self.short_solder_right = {};self.short_solder_left = {};
        self.long_up ={};self.long_down ={};self.long_right ={};self.long_left ={};
        self.long_toxin_up = {};self.long_toxin_down = {};self.long_toxin_right = {};self.long_toxin_left = {};
        self.die= {}
        self.doing_count={"attack":False,"Roll" :False,"Die" : False,"item":False,"keeprun":False
                          ,"idle":True,"key_f":False}
        self.state = 'big'
        self.attack_count =0
        self.HP = 100
        for i in range(0, 40):
            self.long_up[i] = load_image('resource/Will/bigsword/Will_BigSwordCombo_Animation_up_%d.png' % (i+1))
            self.long_down[i] = load_image('resource/Will/bigsword/Will_BigSwordCombo_Animation_Down_%d.png' % (i + 1))
            self.long_right[i] = load_image('resource/Will/bigsword/Will_BigSwordCombo_Animation_Right_%d.png' % (i + 1))
            self.long_left[i] = load_image('resource/Will/bigsword/Will_BigSwordCombo_Animation_Left_%d.png' % (i + 1))
            self.long_toxin_up[i] = load_image('resource/Will/bigsword/toxi/ToxicBigSwordCombo_Main_Up_%d.png' % (i+1))
            self.long_toxin_down[i] = load_image('resource/Will/bigsword/toxi/ToxicBigSwordCombo_Main_Down_%d.png' % (i+1))
            self.long_toxin_right[i] = load_image('resource/Will/bigsword/toxi/ToxicBigSwordCombo_Main_Right_%d.png' % (i+1))
            self.long_toxin_left[i] = load_image('resource/Will/bigsword/toxi/ToxicBigSwordCombo_Main_Left_%d.png' % (i+1))
        for i in range(0, 18):
            self.short_up[i] = load_image('resource/Will/shortsword/Will_ShortSwordCombo_Animation_Up_%d.png' % (i+1))
            self.short_down[i] = load_image('resource/Will/shortsword/Will_ShortSwordCombo_Animation_Down_%d.png' % (i+1))
            self.short_right[i] = load_image('resource/Will/shortsword/Will_ShortSwordCombo_Animation_Right_%d.png' % (i+1))
            self.short_left[i] = load_image('resource/Will/shortsword/Will_ShortSwordCombo_Animation_Left_%d.png' % (i+1))
            self.short_solder_up[i] = load_image('resource/Will/shortsword/solder/SoldierShortSwordCombo_Main_Up_%d.png' % (i+1))
            self.short_solder_down[i] = load_image('resource/Will/shortsword/solder/SoldierShortSwordCombo_Main_Down_%d.png' % (i+1))
            self.short_solder_right[i] = load_image('resource/Will/shortsword/solder/SoldierShortSwordCombo_Main_Right_%d.png' % (i+1))
            self.short_solder_left[i] = load_image('resource/Will/shortsword/solder/SoldierShortSwordCombo_Main_Left_%d.png' % (i+1))

        self.attack_image ={}
        for i in range(0, 4):
            self.attack_image[i] = load_image('resource/Will/Will_Idle_attacked_%d.png' % (i))
        for i in range(11):
            self.die[i] = load_image('resource/Will/Die/Death of Will_Export_%d.png' % (i+1))
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = 1
        self.frame = 0
        self.jumptimer= 0
        self.now_max_frame = 8
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.attack_score = 0

        self.sound_walk = load_wav('resource/sound/Will_Walk.wav')
        self.sound_attack = load_wav('resource/sound/Will_Sword.wav')
        self.sound_roll = load_wav('resource/sound/Will_Roll.wav')

    def get_bb(self):
        if self.direction ==0:
            return self.x - 20, self.y - 20, self.x + 20, self.y + 30
        elif self.direction ==1:
            return self.x - 20, self.y - 30, self.x + 20, self.y + 20
        elif self.direction == 2:
            return self.x - 30, self.y - 20, self.x + 20, self.y + 20
        elif self.direction == 3:
            return self.x - 20, self.y - 20, self.x + 30, self.y + 20

    def depend(self):
        pass
    #def roll(self):
        #ball = Ball(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
        #game_world.add_object(ball, 1)
    def attacked(self):
        self.attack_image[self.direction].clip_draw(0, 0, 35, 35, self.x, self.y)
        self.attack_score =1
        self.HP -=0.1
        if self.HP <= 0:
            self.add_event(DEAD_HP)
            self.HP =0
        print("attacked")


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self, will):
        self.cur_state.do(self)
        if len(self.event_que) > 0 and self.cur_state != DeadState:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.change_do(event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        #for ball in self.team:
            #ball.update()
    def change_do(self,event):
        if event == ATTACK_DOWN:
            self.doing_count.update(attack = True)
            self.attack_count += 1
        elif event == ATTACK_UP:
            self.doing_count.update(attack = False)
        if event == KEY_F:
            self.doing_count.update(key_f=True)
            server.grass.update
        else:self.doing_count.update(key_f=False)

        if self.doing_count['attack']:
            self.cur_state = AttackState
        if self.doing_count['keeprun']:
            if not self.doing_count['attack']:
                self.cur_state = RunState
                self.add_event(KEEPRUN)
                self.doing_count.update(keeprun=False)
            else:self.cur_state = AttackState

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 70, '(HP: %3.2f)' % self.HP, (255, 0, 0))
        debug_print('velocity_x :' + str(self.velocity_x) + '  Dir:' + str(self.dir) + 'State: ' + self.cur_state.__name__+' frame :'+
                    str(self.now_max_frame) + 'combo: ' + str(self.attack_count)+':'+str(self.frame))
        #for ball in self.team:
            #ball.draw()
        #fill here
        draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

