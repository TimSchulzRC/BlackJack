import pygame
import os
from random import randint

pygame.init()

SIZE = WIDTH, HEIGHT = 840, 540

win = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Black Jack')
bg = pygame.image.load("images/background.jpg")
bg = pygame.transform.scale(bg, (840, 540))
win.blit(bg, (0, 0))

cards = []
path = "images/cards"
imageFolder = os.listdir(path)

playerHand = []
dealerHand = []


class Card:
    def __init__(self, path, value):
        self.path = path
        self.value = value

    def show(self, win, pos):                                          # pos with form (x, y)
        card = pygame.image.load("images/cards/" + self.path)
        cardHeight = card.get_height()
        cardWidth = card.get_width()
        cardRatio = cardWidth / cardHeight
        cardSize = 200
        card = pygame.transform.scale(
            card, (int(cardSize * cardRatio), cardSize))
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

# for card in cards:
#     print([card.path, card.value])


def give_card(hand):
    card = cards[randint(0, len(cards))]
    cards.remove(card)
    hand.append(card)


def display_dealer_hand():
    x, y = 80, 40
    for card in dealerHand:
        card.show(win, (x, y))
        x += 50


def display_player_hand():
    x, y = 80, 300
    for card in playerHand:
        card.show(win, (x, y))
        x += 50


def add_values(hand):
    sum = 0
    for card in hand:
        value = card.value
        if type(value) != list:
            sum += value
        if type(value) == list:
            if sum + 11 < 21:
                sum += value[1]
            else:
                sum += value[0]
    return sum


give_card(dealerHand)
give_card(dealerHand)
give_card(playerHand)
give_card(playerHand)
print(add_values(dealerHand))


class Button:
    def __init__(self, buttonX, buttonY, buttonWidth, buttonHeight):
        self.buttonX = buttonX
        self.buttonY = buttonY
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight

    def draw(self):
        pygame.draw.rect(win, (60, 60, 60),
                         (self.buttonX, self.buttonY, self.buttonWidth, self.buttonHeight))

    def pressed():
        pass


button1X, button1Y, button1Width, button1Height = 620, 320, 120, 70
button2X, button2Y, button2Width, button2Height = 620, 420, 120, 70

button1 = Button(button1X, button1Y, button1Width, button1Height)
button2 = Button(button2X, button2Y, button2Width, button2Height)

run = True
while run:
    display_dealer_hand()
    display_player_hand()
    button1.draw()
    button2.draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if button1X < x < button1X + button1Width and button1Y < y < button1Y + button1Height:
                print("Button 1 pressed")
