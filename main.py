import pygame as pg

#chess pieces
p1 = "pawn"
p2 = "bishop"
p3 = "knight"
p4 = "rook"
p5 = "queen"
p6 = "king"

line1 = [p4, p3, p2, p5, p6, p2, p3, p4]
line2 = [p1, p1, p1, p1, p1, p1, p1, p1]


#start pygame
pg.init()
screen = pg.display.set_mode((800, 800)) #window (size)
clock = pg.time.Clock()
running = True

color = (0, 0, 0)    #rectangle color
posX, posY = 0, 0        #recatangle position x, recatangle position y
sizeW = 100    #rectangle size
sizeH = 100    #rectangle size


while running:      #open window

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    #render frame
    screen.fill("black")

    #chess game
    while posX < 700:
        pg.draw.rect(screen, color, (posX, posY, sizeH, sizeW))
        print(posX)
        posX = posX + 200
        print(posX)

    


    #flip display to put game on screen
    pg.display.flip()

    clock.tick(60)

pg.quit()

