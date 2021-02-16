import pygame
import os
from random import randint

pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600

win = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Black Jack')

images = []

path = "images/cards"
imageFolder = os.listdir(path)
for i in imageFolder:
    images.append(i)


class Card:
    def __init__(self):
        pass


def rand_image():
    return images[randint(0, 51)]


def show_card():
    card = pygame.image.load("images/cards/" + rand_image())
    card_height = card.get_height()
    card_width = card.get_width()
    card_ratio = card_width / card_height
    card_size = 200
    card = pygame.transform.scale(
        card, (int(card_size * card_ratio), card_size))
    win.blit(card, (0, 0))


def redrawWindow():
    show_card()
    pygame.display.update()


run = True

while run:
    redrawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
