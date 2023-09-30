from pico2d import *
import random

Width, Height = 1280, 960
open_canvas(Width, Height)

handImg = load_image('hand_arrow.png')
backGroundImg = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

p1 = [Width // 2, Height //2]
p2 = [Width // 2, Height //2]
dir = True
frame = 0

def nextRandomLocation():
    global  p1, p2, dir
    p1[0], p1[1] = p2[0], p2[1]
    p2[0], p2[1] = random.randint(0, Width), random.randint(0, Height)

    if p2[0] - p1[0] >= 0:
        dir = False
    else:
        dir = True


def moveBoy():
    global frame
    for i in range(0, 100+1, 3):
        clear_canvas()
        backGroundImg.draw(Width // 2, Height // 2)
        handImg.draw(p2[0],p2[1])

        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        if dir:
            boy.clip_draw(frame * 100, 0, 100, 100, x, y)
        else:
            boy.clip_draw(frame * 100, 100, 100, 100, x, y)


        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)
    boy.clip_draw(frame * 100, 100, 100, 100, p2[0], p2[1])






while True:
    nextRandomLocation()
    moveBoy()