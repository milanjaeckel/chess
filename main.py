import pygame as pg
import numpy as np

from board import render_board
from position import pos

#print(pos)

pg.init()
size = 900
screen = pg.display.set_mode((size, size))
clock = pg.time.Clock()
running = True

while running:      #open window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    render_board(screen, size)

    #flip display to put game on screen
    pg.display.flip()

    clock.tick(60)

pg.quit()

