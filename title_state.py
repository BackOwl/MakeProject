import game_framework
from pico2d import *
import main_state


name = "TitleState"
image = None


def enter():
    global image
    image =load_image('resource/framebackground/title.jpg') #타이틀 사진 추가 해야함


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif( event.type, event.key) == ( SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.clip_draw(0,0,600,257,600,300,1200,600)
    update_canvas()








def update():
    pass


def pause():
    pass


def resume():
    pass






