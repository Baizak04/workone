import pygame, sys
from bullet import Bullet
from ino import Ino


def events(screen, gun, bullets):
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
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                # Вправо
                if event.key == pygame.K_d:
                    gun.mright = False
                elif event.key == pygame.K_a:
                    gun.mleft = False
                    
                    
def update(bg_color, screen, gun, inos, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()
        
        
def update_bullets(inoc, bullets):
    """Обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inoc, True, True)
            
def update_inoc(inos):
    """Обновляет позицию инопришельцев"""
    inos.update()
            
            
def create_army(screen, inos):
    """Создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)
    
    for row_number in range(number_ino_y - 2):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)