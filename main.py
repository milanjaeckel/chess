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

color = (255, 255, 255)    #rectangle color
sizeW = 100    #rectangle size
sizeH = 100    #rectangle size


while running:      #open window

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    posX, posY = 0, 0   #recatangle position x, recatangle position y
    s1 = True           #wether or not the first square of the row should be black or white

    #render frame
    screen.fill("black")

    #chess game
    while posY < 800:
        posX = 0
        if s1 != True:
            posX = posX + 100
        while posX <= 800:
            pg.draw.rect(screen, color, (posX, posY, sizeH, sizeW))
            posX = posX + 200
        posY = posY + 100
        s1 = not s1

    


    #flip display to put game on screen
    pg.display.flip()

    clock.tick(60)

pg.quit()

