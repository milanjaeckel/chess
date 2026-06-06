import pygame as pg
import numpy as np

from board import render_board
from position import pos
from renderPieces import ChessPiece

pg.init()
size = 900
screen = pg.display.set_mode((size, size))
clock = pg.time.Clock()
running = True

all_pieces = pg.sprite.Group()
bRook = ChessPiece("pieces/b-rook.png",0 ,7)
bNight = ChessPiece("pieces/b-knight.png",117 ,7)
all_pieces.add(bRook)
all_pieces.add(bNight)

while running:      #open window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    render_board(screen, size)

    all_pieces.draw(screen)

    #flip display to put game on screen
    pg.display.flip()

    clock.tick(60)

pg.quit()

