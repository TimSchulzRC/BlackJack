import pygame
import os
from random import randint
import time

pygame.init()

SIZE = WIDTH, HEIGHT = 840, 540

win = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Black Jack')
bg = pygame.image.load("images/background.jpg")
bg = pygame.transform.scale(bg, (840, 540))

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30, True)

cards = []
path = "images/cards"
imageFolder = os.listdir(path)

playerHand = []
dealerHand = []


def resize_image(image, size):
    height = image.get_height()
    width = image.get_width()
    ratio = width / height
    rezizedImage = pygame.transform.scale(image, (int(size * ratio), size))
    return rezizedImage


class Card:
    def __init__(self, path, value):
        self.path = path
        self.value = value

    def show(self, win, pos):                                          # pos with form (x, y)
        card = pygame.image.load("images/cards/" + self.path)
        card = resize_image(card, 150)
        win.blit(card, pos)


def card_value(card):
    try:
        value = int(card[0])
        if value == 1:
            value = 10
    except:
        if card[0] in ["J", "Q", "K"]:
            value = 10
        elif card[0] == "A":
            value = [1, 11]
    return value


for path in imageFolder:
    cards.append(Card(path, card_value(path)))


def give_card(hand):
    card = cards[randint(0, len(cards)-1)]
    cards.remove(card)
    hand.append(card)


def display_dealer_hand():
    x, y = 100, 40
    for card in dealerHand:
        card.show(win, (x, y))
        x += 50
    dealerText = pygame.image.load("images/text/Dealer.png")
    dealerText = pygame.transform.rotate(dealerText, 90)
    dealerText = resize_image(dealerText, 250)
    win.blit(dealerText, (0, 0))


def display_player_hand():
    x, y = 100, 300
    for card in playerHand:
        card.show(win, (x, y))
        x += 50
    playerText = pygame.image.load("images/text/Player.png")
    playerText = pygame.transform.rotate(playerText, 90)
    playerText = resize_image(playerText, 250)
    win.blit(playerText, (0, 260))


def add_values(hand):
    sum = 0
    for card in hand:
        value = card.value
        if type(value) != list:
            sum += value
        if type(value) == list:
            if sum + 11 < 21:
                sum += value[1]
 #           elif hand == dealerHand:
 #              sum += value[0]
            else:
                sum += value[0]
    return sum


give_card(dealerHand)
give_card(dealerHand)
give_card(playerHand)
give_card(playerHand)


class Button:
    def __init__(self, buttonX, buttonY, image, onPressed):
        self.buttonX = buttonX
        self.buttonY = buttonY
        self.image = image
        self.onPressed = onPressed

    def draw(self):
        hold = pygame.image.load("images/buttons/" + self.image)
        win.blit(hold, (self.buttonX, self.buttonY))

    def pressed(self):
        self.onPressed()


def new_card():
    if add_values(playerHand) < 21:
        give_card(playerHand)


def hold():
    while add_values(dealerHand) < 17:
        give_card(dealerHand)
        display_dealer_hand()
        win.blit(show_sum(dealerHand), (150, 210))
        time.sleep(1)


button1X, button1Y, button1Width, button1Height = 580, 320, 168, 70
button2X, button2Y, button2Width, button2Height = 580, 420, 168, 70

button1 = Button(button1X, button1Y, "hold.png", hold)
button2 = Button(button2X, button2Y, "new_card.png", new_card)


def show_sum(hand):
    sum = myfont.render(
        str(add_values(hand)), True, (220, 220, 220))
    return sum


run = True
while run:
    win.blit(bg, (0, 0))

    display_dealer_hand()
    display_player_hand()
    button1.draw()
    button2.draw()
    # button2.draw()

    win.blit(show_sum(dealerHand), (150, 210))
    win.blit(show_sum(playerHand), (150, 470))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if button1X < x < button1X + button1Width and button1Y < y < button1Y + button1Height:
                button1.pressed()
            if button2X < x < button2X + button1Width and button2Y < y < button2Y + button2Height:
                button2.pressed()
                sumPlayer = myfont.render(
                    str(add_values(playerHand)), True, (220, 220, 220))
