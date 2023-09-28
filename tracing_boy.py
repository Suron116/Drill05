from pico2d import *
import random

open_canvas(1280, 1024)

back = load_image('TUK_GROUND.png')
character = load_image('left.png')
hand = load_image('hand_arrow.png')

x1, y1 = 640, 512


# 1. 랜덤 위치에 손 생성
while True:
    back.draw_now(640, 512)
    points = [random.randint(0, 1280), random.randint(0, 1024)]
    x2, y2 = points[0], points[1]
    hand.draw_now(x2, y2)
    # 소년 이동
    character.draw_now(x1, y1)
    for i in range (0, 100 + 1, 5):
        t = i / 100
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        back.draw_now(640, 512)
        hand.draw_now(x2, y2)
        character.draw_now(x, y)
        delay(0.1)
        update_canvas()