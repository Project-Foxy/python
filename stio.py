from math import *
import pygame

pygame.init()

width = 800
height = 500

img = pygame.image.load('coding/resurser/bilder/epple1600.png')
pygame.display.set_icon(img)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("stio_game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                img = pygame.image.load('coding/resurser/bilder/nikee.png')
                screen.blit(img, (0, 0))
            
    
    pygame.display.update()
