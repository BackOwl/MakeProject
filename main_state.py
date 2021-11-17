import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Will
from grass import Grass
from enemy import BabySlime, Stone
from object import Hanari
from ball import Ball

name = "MainState"

will = None
grass = None
break_objects = []
monsters = []

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




def enter():
    global will
    will = Will()
    game_world.add_object(will, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global monsters
    monsters = [BabySlime() for i in range(5)]+[Stone() for i in range(3)]
    game_world.add_objects(monsters, 1)

    global break_objects
    break_objects = [Hanari() for i in range(5)]
    game_world.add_objects(break_objects, 1)





    # fill here for balls





def exit():
    game_world.clear()

def pause():
    pass


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
            will.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update(will)

    for monster in monsters:
        if collide(will, monster):
            print("COLLISION")
            monsters.remove(monster)
            game_world.remove_object(monster)



    # fill here for collision check



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






