import pygame 

pygame.init()
screen = pygame.display.set_mode((600,850))
done = False 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen,(0,225,225),pygame.Rect(50,50,60,60))
    pygame.display.flip()