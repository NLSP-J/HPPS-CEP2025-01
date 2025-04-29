import pygame as pg
import random, time
import asyncio

pg.init()
clock = pg.time.Clock()

score = 0
white = (255, 255, 255)
black = (0,0,0)

win_width = 500
win_height = 500
screen = pg.display.set_mode([win_width, win_height])
pg.display.set_caption('Click to win!')

font = pg.font.Font(None, 30)

x = 0
y = 0
player_x = 0
player_y = 0
clicked = False
got_time = False
time_interval = 1500
start_time = 0

obj_size = 80
obj_data = []
obj_image = pg.image.load('./assets/images/button.png')
obj_image = pg.transform.scale(obj_image,(obj_size, obj_size))



def createbutton(obj_data):
    global x, y, clicked
    if len(obj_data) < 1:
        x = random.randint(0, win_width - obj_size)
        y = random.randint(0, win_height - obj_size)
        obj_data.append([x, y, obj_image])
        clicked = False

def updatebutton(obj_data):
    global got_time, start_time
    
    if not got_time:
        start_time = pg.time.get_ticks()
        got_time = True
    x, y, obj_image = obj_data[0]
    screen.blit(obj_image, (x, y))
    if pg.time.get_ticks() - start_time > time_interval or clicked:
        obj_data.pop(0)
        got_time = False

def checkclick():
    global score, clicked
    
    player_x, player_y = pg.mouse.get_pos()

    for obj in obj_data:
        x, y, obj_image = obj
        if player_x > x and player_x < x + obj_size and player_y > y and player_y < y + obj_size:
            clicked = True
            obj_data.remove(obj)
            score += 1

async def main():

    running = True

    while running == True:
        screen.fill(white)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                checkclick()

        text = f'Current Score : {score}'
        text = font.render(text, 10, black)
        screen.blit(text, (win_width - 375, win_height - 40))
        
        createbutton(obj_data)
        updatebutton(obj_data)
        
        clock.tick(30)
        pg.display.update()
        await asyncio.sleep(0)

asyncio.run(main())
