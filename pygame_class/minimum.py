# pygame hello world game
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('python game trip')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
