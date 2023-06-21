import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((320, 240))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создаеть объект шрифта
font = pygame.font.Font(None, 32)

while True:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    # создать текстовую поверхность
    text = font.render("Hello World", True, BLACK)
    # переместить текстовую поверхность в центр экрана
    screen.blit(text, ((screen.get_width() -
        text.get_width())/2,
        (screen.get_height() - text.get_height()) / 2))
            
    pygame.display.flip