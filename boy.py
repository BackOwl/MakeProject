import game_framework
from pico2d import *
from ball import Ball

import game_world

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
    ,ATTACK_DOWN,ATTACK_UP= range(12)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYDOWN, SDLK_q):ATTACK_DOWN,

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
        will.frame = (will.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % will.now_max_frame


    def draw(will):
        will.image1.clip_draw(int(will.frame)* 35, will.direction * 35, 35, 35, will.x, will.y)


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
            will.now_max_frame = 8#
            will.velocity_y -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            will.velocity_y += RUN_SPEED_PPS
            will.now_max_frame = 8#
        will.dir = clamp(-1, will.velocity_x, 1)
        will.dir = clamp(-1, will.velocity_y, 1)
        will.jumptimer = 800

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
        will.x = clamp(25, will.x, 1600 - 25)

    def draw(will):
        will.image0.clip_draw(int(will.frame) * 35, will.direction * 35, 35, 35, will.x, will.y)

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
        will.jumptimer =400


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
        will.x = clamp(35, will.x, 1200-35)

    def draw(will):
        will.image2.clip_draw(int(will.frame) * 35, will.direction * 35, 35, 35, will.x, will.y)


class AttackState:

    def enter(will, event):
        if event == RIGHT_DOWN:
            will.now_max_frame = 8
            will.direction = 3
        elif event == LEFT_DOWN:
            will.direction = 2
            will.now_max_frame = 8
        elif event == RIGHT_UP:
            will.now_max_frame = 8#
        elif event == LEFT_UP:
            will.now_max_frame = 8#
        if event == UP_DOWN:
            will.direction = 0
            will.now_max_frame = 8
        elif event == DOWN_DOWN:
            will.direction = 1
            will.now_max_frame = 8
        elif event == UP_UP:
            will.now_max_frame = 8#
        elif event == DOWN_UP:
            will.now_max_frame = 8#
        will.jumptimer = 1600
        will.attack_count+=1
        if will.state == 'short':
            will.frame = (will.attack_count * 4 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        elif will.state == 'big':
            will.frame = (will.attack_count * 10 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 40

    def exit(will, event):
        if will.state == 'short':
            if will.frame > (will.attack_count+1)*4 %16:
                will.add_event(ATTACK_UP)
            else:
                will.add_event(ATTACK_DOWN)
        elif will.state == 'big':
            if will.frame > (will.attack_count + 1) * 10 %40:
                will.add_event(ATTACK_UP)
            else:
                will.add_event(ATTACK_DOWN)
        #if event == SPACE:
            #will.depend() // 방패

    def do(will):
        if will.state =='short':
            will.frame = (will.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        elif will.state == 'big':
            will.frame = (will.frame  + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %40
            #will.x += will.velocity * game_framework.frame_time

        will.x = clamp(35, will.x, 1200 - 35)
        will.jumptimer -=5
        if will.jumptimer ==0:
            will.attack_count =0

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

        delay(0.1)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,  SPACE_DOWN: IdleState,
                UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,ATTACK_DOWN: AttackState, ATTACK_UP: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE_DOWN: JumpState,
               UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: RunState, DOWN_DOWN: RunState,ATTACK_DOWN: AttackState, ATTACK_UP: RunState},
    JumpState: {RIGHT_UP: RunState,LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
                UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,SPACE_DOWN: JumpState,JUMP_TIMER: RunState,
                ATTACK_DOWN: AttackState, ATTACK_UP: RunState},
    AttackState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE_DOWN: JumpState,
                UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: RunState, DOWN_DOWN: RunState,ATTACK_DOWN: AttackState, ATTACK_UP: RunState}

}

class Will:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # will is only once created, so instance image loading is fine
        self.image0 = load_image('resource/Will/will animation cycle35.35.png')
        self.image1 = load_image('resource/Will/Will_Idle35.35.png')
        self.image2 = load_image('resource/Will/Will_Roll35.35.png')
        self.short_up ={};self.short_down ={};self.short_right ={};self.short_left ={};
        self.short_solder_up = {};self.short_solder_down = {};self.short_solder_right = {};self.short_solder_left = {};
        self.long_up ={};self.long_down ={};self.long_right ={};self.long_left ={};
        self.long_toxin_up = {};self.long_toxin_down = {};self.long_toxin_right = {};self.long_toxin_left = {};
        self.die= load_image('resource/Will/Death of Will_Export33.41.png')
        self.state = 'big'
        self.attack_count =0
        for i in range(0, 40):
            self.long_up[i] = load_image('resource/Will/bigsword/Will_BigSwordCombo_Animation_up_%d.png' % (i+1))
            self.long_down[i] = load_image('resource/Will/bigsword/Will_BigSwordCombo_Animation_Down_%d.png' % (i + 1))
            self.long_right[i] = load_image('resource/Will/bigsword/Will_BigSwordCombo_Animation_Right_%d.png' % (i + 1))
            self.long_left[i] = load_image('resource/Will/bigsword/Will_BigSwordCombo_Animation_Left_%d.png' % (i + 1))
            self.long_toxin_up[i] = ('resource/Will/bigsword/toxi/ToxicBigSwordCombo_Main_Up_%d.png' % (i+1))
            self.long_toxin_down[i] = ('resource/Will/bigsword/toxi/ToxicBigSwordCombo_Main_Down_%d.png' % (i+1))
            self.long_toxin_right[i] = ('resource/Will/bigsword/toxi/ToxicBigSwordCombo_Main_Right_%d.png' % (i+1))
            self.long_toxin_left[i] = ('resource/Will/bigsword/toxi/ToxicBigSwordCombo_Main_Left_%d.png' % (i+1))
        for i in range(0, 18):
            self.short_up[i] = load_image('resource/Will/shortsword/Will_ShortSwordCombo_Animation_Up_%d.png' % (i+1))
            self.short_down[i] = load_image('resource/Will/shortsword/Will_ShortSwordCombo_Animation_Down_%d.png' % (i+1))
            self.short_right[i] = load_image('resource/Will/shortsword/Will_ShortSwordCombo_Animation_Right_%d.png' % (i+1))
            self.short_left[i] = load_image('resource/Will/shortsword/Will_ShortSwordCombo_Animation_Left_%d.png' % (i+1))
            self.short_solder_up[i] = load_image('resource/Will/shortsword/solder/SoldierShortSwordCombo_Main_Up_%d.png' % (i+1))
            self.short_solder_down[i] = load_image('resource/Will/shortsword/solder/SoldierShortSwordCombo_Main_Down_%d.png' % (i+1))
            self.short_solder_right[i] = load_image('resource/Will/shortsword/solder/SoldierShortSwordCombo_Main_Right_%d.png' % (i+1))
            self.short_solder_left[i] = load_image('resource/Will/shortsword/solder/SoldierShortSwordCombo_Main_Left_%d.png' % (i+1))

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
        self.team = [Ball() for i in range(5)]

    def get_bb(self):
        # fill here
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def depend(self):
        pass
    #def roll(self):
        #ball = Ball(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
        #game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self, will):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        #for ball in self.team:
            #ball.update()

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        debug_print('velocity_x :' + str(self.velocity_x) + '  Dir:' + str(self.dir) + 'State: ' + self.cur_state.__name__+' frame :'+
                    str(self.now_max_frame))
        #for ball in self.team:
            #ball.draw()
        #fill here
        draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

