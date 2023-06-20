import pygame, sys

def events(gun):
    """Обработка событий"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Вправо
                if event.key == pygame.K_d:
                    gun.mright = True
                elif event.key == pygame.K_a:
                    gun.mleft = True
            elif event.type == pygame.KEYUP:
                # Вправо
                if event.key == pygame.K_d:
                    gun.mright = False
                elif event.key == pygame.K_a:
                    gun.mleft = False
                    
                    
def update(bg_color, screen, gun):
    """обновление экрана"""
    screen.fill(bg_color)
    gun.output()
    pygame.display.flip()
        