import pygame as pg
from board import render_board

#chess pieces
p1 = "pawn"
p2 = "bishop"
p3 = "knight"
p4 = "rook"
p5 = "queen"
p6 = "king"

line1 = [p4, p3, p2, p5, p6, p2, p3, p4]
line2 = [p1, p1, p1, p1, p1, p1, p1, p1]

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

