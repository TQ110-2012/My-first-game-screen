import pygame

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")

bg_color = (58, 58, 58)

try:
    image = pygame.image.load('your_image.png')
    image = pygame.transform.scale(image, (300, 300))
except:
    image = pygame.Surface((300, 300))
    image.fill((200, 200, 200))

image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(bg_color)
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()
