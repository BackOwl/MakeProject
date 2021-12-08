import game_framework
from pico2d import *
import main_state
import background


name = "TitleState"
image = None
title = None
music =None


def enter():
    global image
    global title
    global music
    #image =load_image('resource/framebackground/title.jpg') #타이틀 사진 추가 해야함
    image = background.greenwater()
    title =load_image('resource/background/main/start_enter.png')
    music = load_music('resource/sound/title_song.mp3')
    music.repeat_play()


def exit():
    global image
    global title
    del(image)
    del(title)


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
                music.stop()


def draw():
    clear_canvas()
    #image.clip_draw(0,0,600,257,600,300,1200,600)
    image.draw()
    title.clip_draw(0, 0, 1230, 463, 600, 300, 400, 100)
    image.update()
    update_canvas()








def update():
    pass


def pause():
    pass


def resume():
    pass






