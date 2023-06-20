from typing import Any
import pygame


class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, screen, gun):
        """Создаем пулю в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 10)
        self.color = 0, 183, 239
        self.speed = 1.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
        
        
    def update(self):
        """Перемешение пули вверх"""
        self.y = self.speed
        self.rect.y = self.y
        
        
    def draw_bullet(self):
        """Рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)