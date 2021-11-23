import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server

from boy import Will
from grass import Grass
from enemy import BabySlime, Stone
from object import Hanari,Sword
from ball import Ball

name = "MainState"



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
    server.will = Will()
    game_world.add_object(server.will, 1)

    server.grass = Grass()
    game_world.add_object(server.grass, 0)

    server.monsters = [BabySlime() for i in range(5)]+[Stone() for i in range(3)]
    game_world.add_objects(server.monsters, 1)

    server.break_objects = [Hanari() for i in range(5)]+[Sword() for i in range(1)]
    game_world.add_objects(server.break_objects, 1)





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
            server.will.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update(server.will)

    for monster in server.monsters:
        if collide(server.will, monster):
            print("COLLISION")
            server.monsters.remove(monster)
            game_world.remove_object(monster)



    # fill here for collision check



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






