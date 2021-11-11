from pico2d import *
import random
import enemy


# 내가 게임을 플레이함에 필요한 객체를 꼽아서( 소년, 잔디) 추상화
class Grass:
    def __init__(self):
        self.image0 = load_image('resource/background/background_Level0.png')
        self.image1 = load_image('resource/background/backgroundWalls_Level0.png')

    def draw(self):
        self.image0.draw(300, 170)
        self.image1.draw(300, 170)


class Will:
    def __init__(self):
        self.x, self.y = random.randint(100, 400), 90
        self.frame = 0
        self.image0 = load_image('resource/Will/will animation cycle35.35.png')
        self.image1 = load_image('resource/Will/Will_Idle35.35.png')
        self.image2 = load_image('resource/Will/Will_Roll35.35.png')

    def update(self):
        global now_max_frame
        self.frame = (self.frame + 1) % now_max_frame
        #if self.x< 80 :self.x =self.x
        #elif self.x >500: self.x =self.x
        #else:
            #self.x = (1 - 0.5) * will.x + 0.5 * mx
        #if self.y < 60: self.y =self.y
        #elif self.y > 310:self.y =self.y
        #else:
            #self.y = (1 - 0.5) * will.y + 0.5 * my
        self.x = (1 - 0.5) * will.x + 0.5 * mx
        self.y = (1 - 0.5) * will.y + 0.5 * my
    def draw(self):
        global run,roll,rolldo
        global Will_direction
        if roll==False:
            if run:
                self.image0.clip_draw(self.frame * 35, Will_direction * 35, 35, 35, self.x, self.y)
            elif run == False:
                self.image1.clip_draw(self.frame * 35, Will_direction * 35, 35, 35, self.x, self.y)
        elif roll == True:
            self.image2.clip_draw(self.frame * 35, Will_direction * 35, 35, 35, self.x, self.y)
            rolldo += 1
            if rolldo == 7:
                rolldo = 0
                roll = False
                run = True


def handle_events():  # 키입력
    global running, run,roll
    global Will_direction, now_max_frame,Will_x_state,Will_y_state
    global mx, my, will
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                Will_direction = 2
                now_max_frame = 8
                run = True
                Will_x_state = 0
            if event.key == SDLK_RIGHT:
                Will_direction = 3
                now_max_frame = 8
                run = True
                Will_x_state = 1
            if event.key == SDLK_DOWN:
                Will_direction = 1
                now_max_frame = 8
                run = True
                Will_y_state = 0
            if event.key == SDLK_UP:
                Will_direction = 0
                now_max_frame = 8
                run = True
                Will_y_state = 1

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                if Will_x_state == 0:
                    run = False
                    now_max_frame = 10
                    Will_x_state = -1
            elif event.key == SDLK_RIGHT:
                if Will_x_state == 1:
                    run = False
                    now_max_frame = 10
                    Will_x_state = -1
            if event.key == SDLK_DOWN:
                if Will_y_state == 0:
                    run = False
                    now_max_frame = 10
                    Will_y_state = -1
            elif event.key == SDLK_UP:
                if Will_y_state == 1:
                    run = False
                    now_max_frame = 10
                    Will_y_state = -1
        #if event.key == SDLK_UP and event.key == SDLK_DOWN and event.key == SDLK_LEFT and event.key == SDLK_RIGHT and event.type == SDL_KEYUP:
           #run = False
        if event.key == SDLK_SPACE and event.type == SDL_KEYDOWN:
            now_max_frame = 8
            roll = True
            will.frame = 0
        if event.key == SDLK_SPACE and event.type == SDL_KEYUP:
            now_max_frame = 8
            if Will_y_state == -1 and Will_x_state == -1 and roll == False:
                now_max_frame = 10


'''
def update_character():
    global mx, my
    global will
    will.x = (1 - 0.5) * will.x + 0.5 * mx
    will.y = (1 - 0.5) * will.y + 0.5 * my
'''

# initialization code
open_canvas(600, 340,sync =True) # 프레임 60고정 
now_max_frame = 8
grass = Grass()  # 잔디 객체 생성
will = Will()
slime = enemy.BabySlime()
stone = enemy.Stone()
mx, my = will.x, will.y
Will_direction = 1
rolldo = 0
Will_x_state = -1
Will_y_state = -1
run = False
roll= False
# team = [Boy() for i in range(1, 11+1)]
running = True

# game main loop code
while running:
    handle_events()

    # game logic 업데이트자리
    '''for boy in team:
        boy.update()'''

    # 지금 눌릴때 한번밖에 안들어감...계속 들어가게하는법?
    if Will_x_state == 0:
        mx -= 10
        if roll: will.x -= 15
    elif Will_x_state == 1:
        mx += 10
        if roll: will.x += 15
    if Will_y_state == 0:
        my -= 10
        if roll: will.y -= 15
    elif Will_y_state == 1:
        my += 10
        if roll: will.y += 15


     # 적들
    slime.update(will.x, will.y)
    stone.update(will.x, will.y)

    #주인공
    will.update()
    #update_character()  # 걷기모션

    # game drawing
    clear_canvas()
    grass.draw()
    will.draw()
    slime.draw()
    stone.draw()


    update_canvas()

    delay(0.1)
# finalization code 마무리

close_canvas()
