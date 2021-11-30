import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server

from boy import Will
from grass import Grass,Level2,Level3
from enemy import BabySlime, Stone
from object import Hanari,Sword,Door
from ball import Ball

name = "MainState"
image = None


balls = []
big_balls = []


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def attack_collide(a,b,dir):# 왼쪽을 맞는 거, 오른쪽을 때리는 거
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if dir ==0:# 위
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
    elif dir ==1:# 아래
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
    elif dir==2:# 왼
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
    elif dir ==3: # 오
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

    return True




def enter():
    server.will = Will()
    game_world.add_object(server.will, 1)
    if server.grasslevel ==0:
        server.grass = Grass()
    elif server.grasslevel == 1:
        server.grass = Level2()
    elif server.grasslevel ==2:
        server.grass = Level3()
    game_world.add_object(server.grass, 0)
    server.monsters = [BabySlime() for i in range(server.slime_count)]+[Stone() for i in range(server.golem_count)]
    game_world.add_objects(server.monsters, 1)
    server.break_objects = [Hanari() for i in range(server.Hanari_count)]+[Sword() for i in range(server.sword_count)]
    game_world.add_objects(server.break_objects, 1)

    server.door = Door('left','next')
    server.door1 = Door('right', 'back')
    game_world.add_object(server.door , 1)
    game_world.add_object(server.door1, 1)







def exit():
    game_world.clear()

def pause():
    image = load_image('resource/framebackground/pause.png')
    image.clip_draw(0, 0, 1024, 1024, 600, 300, 600, 600)
    update_canvas()
    wait_for_keydown()

def wait_for_keydown():
    loop = True
    sound = load_wav('resource/sound/pause.wav')
    sound.play()
    while loop:
        for e in get_events():
            if e.type == SDL_KEYDOWN and e.key == SDLK_TAB:
                loop = False

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            server.will.handle_event(event)
        if event.type == SDL_KEYDOWN and event.key == SDLK_TAB:
            pause()



def update():
    for game_object in game_world.all_objects():
        game_object.update(server.will)

    for monster in server.monsters:
        if collide(server.will, monster):
            print("COLLISION")




    # fill here for collision check



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






