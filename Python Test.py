import pygame
import random
import math
pygame.init()
scr = pygame.display.set_mode((800,600))
x_position = int(400)
y_position = int(300)
def bounce:

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scr.fill((255,255,255))
    pygame.draw.circle(scr, (0, 0, 255), (x_position, y_position), 20)
    x_position += 0.06
    y_position += 0.04
    pygame.display.flip()
pygame.quit()