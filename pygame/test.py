import pygame as pg

pg.init()
sc = pg.display.set_mode((800, 450), pg.FULLSCREEN | pg.SCALED)
clock = pg.time.Clock()

FPS = 60

while True:
    sc.fill((0, 0, 100))
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            exit()

    # pg.draw.rect(sc, (212, 51, 51), (100, 100, 70, 20))

    pg.display.update()