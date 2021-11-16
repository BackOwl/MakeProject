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
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,UP_DOWN, DOWN_DOWN,DOWN_UP,UP_UP,SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


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
            will.now_max_frame = 10
            will.velocity_x -= RUN_SPEED_PPS
            will.direction = 3
        elif event == LEFT_UP:
            will.now_max_frame = 10
            will.velocity_x += RUN_SPEED_PPS
            will.direction = 2
        elif event == UP_UP:
            will.now_max_frame = 10
            will.velocity_y -= RUN_SPEED_PPS
            will.direction = 0
        elif event == DOWN_UP:
            will.velocity_y += RUN_SPEED_PPS
            will.now_max_frame = 10
            will.direction = 1

    def exit(will, event):
        if event == SPACE:
            will.depend()

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
            will.now_max_frame = 10
            will.velocity_x -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            will.now_max_frame = 10
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
            will.now_max_frame = 10
            will.velocity_y -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            will.velocity_y += RUN_SPEED_PPS
            will.now_max_frame = 10
        will.dir = clamp(-1, will.velocity_x, 1)
        will.dir = clamp(-1, will.velocity_y, 1)

    def exit(will, event):
        if event == SPACE:
            will.depend()

    def do(will):
        #will.frame = (will.frame + 1) % 8
        will.frame = (will.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % will.now_max_frame
        will.x = (1 - 0.5) * will.x + 0.5 * (will.x+will.velocity_x*game_framework.frame_time)
        will.y = (1 - 0.5) * will.y + 0.5 * (will.y+will.velocity_y*game_framework.frame_time)
        #will.x += will.velocity * game_framework.frame_time
        will.x = clamp(25, will.x, 1600 - 25)

    def draw(will):
        will.image0.clip_draw(int(will.frame) * 35, will.direction * 35, 35, 35, will.x, will.y)




next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,  SPACE: IdleState,
                UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState,
               UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState}
}

class Will:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # will is only once created, so instance image loading is fine
        self.image0 = load_image('resource/Will/will animation cycle35.35.png')
        self.image1 = load_image('resource/Will/Will_Idle35.35.png')
        self.image2 = load_image('resource/Will/Will_Roll35.35.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = 1
        self.frame = 0
        self.now_max_frame = 8
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.team = [Ball() for i in range(5)]

    def get_bb(self):
        # fill here

        return 0, 0, 0, 0

    def depend(self):
        pass
    #def roll(self):
        #ball = Ball(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
        #game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        for ball in self.team:
            ball.update()

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #for ball in self.team:
            #ball.draw()
        #fill here


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

