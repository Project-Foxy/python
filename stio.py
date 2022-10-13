from math import *
import pygame

pygame.init()

width = 1200
height = 800

img = pygame.image.load('coding/resurser/bilder/epple1600.png')
pygame.display.set_icon(img)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("stio_game")

running = True

font = pygame.font.SysFont("arial", 20, bold=pygame.font.Font.bold)
black = (0, 0, 0)
white = (255, 255, 255)
whole_text = ("hi")
text = font.render(str(whole_text), True, black, white)

keys = {
    "a": 100,
}


def say(text):
    whole_text = (text)
    text = font.render(str(whole_text), True, black, white)
    screen.blit(text, (50, height - 50))

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
    

    say("text: ")
    
    pygame.display.update()
