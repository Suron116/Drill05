from pico2d import *

open_canvas(1280, 1024)

back = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

back.draw_now(640, 512)