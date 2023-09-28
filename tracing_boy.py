from pico2d import *
import random

open_canvas(1280, 1024)

back = load_image('TUK_GROUND.png')
left = load_image('left.png')
right= load_image('right.png')
hand = load_image('hand_arrow.png')

x1, y1 = 640, 512


# 1. 랜덤 위치에 손 생성
while True:
    back.draw_now(640, 512)
    points = [random.randint(0, 1280), random.randint(0, 1024)]
    x2, y2 = points[0], points[1]
    hand.draw_now(x2, y2)

    # 소년 이동
    for i in range (0, 100 + 1, 5):
        t = i / 100
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        back.draw_now(640, 512)
        hand.draw_now(x2, y2)
        
        # 방향
        if x2 > x1:
            right.draw_now(x, y)
        elif x2 < x1:
            left.draw_now(x, y)

        # 한 칸 이동 시간
        delay(0.05)
        update_canvas()