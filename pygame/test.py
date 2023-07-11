import pygame as pg

pg.init()
sc = pg.display.set_mode((800, 500))

while True:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            exit()

    pg.draw.rect(sc, (212, 51, 51), (100, 100, 70, 20))

    pg.display.update()