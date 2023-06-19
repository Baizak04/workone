import pygame


class Gun():
    
    def __init__(self, screen):
        """Инициализация пушки"""
        
        self.screen = screen
        self.image = pygame.image.load('image/cannon2.png')
        self.rect = self.image.get_rect()
        self.screen_rest = screen.get_rect()
        self.rect.centerx = self.screen_rest.centerx
        self.rect.bottom = self.screen_rest.bottom
        
        
    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)