import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Baizak Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 170))
square.fill('red')

myfont = pygame.font.Font()
running = True
while running:
    
    pygame.draw.circle(square, 'Red', (10, 10), 10)
    screen.blit(square, (10, 0))
        
    
    pygame.display.update
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
      
    
    