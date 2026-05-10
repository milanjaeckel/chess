import pygame as pg

#start pygame
pg.init()
screen = pg.display.set_mode((800, 800)) #window (size)
clock = pg.time.Clock()
running = True

color = (255, 255, 255)    #rectangle color
positionX = 0        #recatangle position x
positionY = 0        #recatangle position y
size = 100, 100    #rectangle size


while running:      #open window

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    #render frame
    screen.fill("black")

    #chess game
    pg.draw.rect(screen, color, pg.Rect(0, 0, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(200, 0, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(400, 0, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(600, 0, 100, 100))

    pg.draw.rect(screen, color, pg.Rect(100, 100, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(300, 100, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(500, 100, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(700, 100, 100, 100))

    pg.draw.rect(screen, color, pg.Rect(0, 200, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(200, 200, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(400, 200, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(600, 200, 100, 100))

    pg.draw.rect(screen, color, pg.Rect(100, 300, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(300, 300, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(500, 300, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(700, 300, 100, 100))

    pg.draw.rect(screen, color, pg.Rect(0, 400, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(200, 400, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(400, 400, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(600, 400, 100, 100))

    pg.draw.rect(screen, color, pg.Rect(100, 500, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(300, 500, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(500, 500, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(700, 500, 100, 100))

    pg.draw.rect(screen, color, pg.Rect(0, 600, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(200, 600, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(400, 600, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(600, 600, 100, 100))

    pg.draw.rect(screen, color, pg.Rect(100, 700, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(300, 700, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(500, 700, 100, 100))
    pg.draw.rect(screen, color, pg.Rect(700, 700, 100, 100))
    


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