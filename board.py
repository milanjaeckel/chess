import pygame as pg    

def render_board():
    posX, posY = 0, 0   #recatangle position x, recatangle position y
    s1 = True           #wether or not the first square of the row should be black or white

    #render frame
    screen.fill("black")

    #chess game
    while posY < size:
        posX = 0
        if not s1:
            posX = posX + size / 8
        while posX <= size:
            pg.draw.rect(screen, color, (posX, posY, sizeW, sizeH))
            posX = posX + size / 4
        posY = posY + size / 8
        s1 = not s1

def test_def():
    print("This is a test")