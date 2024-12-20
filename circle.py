import pygame
pygame.init()


window = pygame.display.set_mode((750,1000))
window.fill((255,255,255))


pygame.draw.circle(window,(225,225,0),(200,200),50)
pygame.draw.circle(window,(225,225,0),(100,200),50,5)

pygame.display.update()

running = True 

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()