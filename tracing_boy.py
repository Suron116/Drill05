from pico2d import *
import random

open_canvas(1280, 1024)

back = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

back.draw_now(640, 512)

drawing = True

# 랜덤 위치에 손 생성
while drawing:
    points = [random.randint(0, 1280), random.randint(0, 1024)]
    delay(3)
    hand.draw_now(points[0], points[1])