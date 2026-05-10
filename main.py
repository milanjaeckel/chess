import pygame as pg

#start pygame
pg.init()
screen = pg.display.set_mode((800, 800)) #window (size)
clock = pg.time.Clock()
running = True
color = (0, 0, 0) #rectangle color

while running:      #open window

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    #render frame
    screen.fill("white")

    #chess game
    pg.draw.rect(screen, color, pg.Rect(0, 0, 100, 100))


    #flip display to put game on screen
    pg.display.flip()

    clock.tick(60)

pg.quit()

p1 = "pawn"
p2 = "bishop"
p3 = "knight"
p4 = "rook"
p5 = "queen"
p6 = "king"

line1 = [p4, p3, p2, p5, p6, p2, p3, p4]
line2 = [p1, p1, p1, p1, p1, p1, p1, p1]