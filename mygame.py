import game_framework
import pico2d

import main_state
import start_state


pico2d.open_canvas(1200, 600)
game_framework.run(start_state)
game_framework.run(main_state)
pico2d.close_canvas()