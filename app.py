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

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30, True)

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
    print("new_card")


def hold():
    print("hold")


button1X, button1Y, button1Width, button1Height = 550, 320, 168, 70
button2X, button2Y, button2Width, button2Height = 550, 420, 168, 70

button1 = Button(button1X, button1Y, "hold.png", new_card)
button2 = Button(button2X, button2Y, "new_card.png", hold)

# buttonText1 = myfont.render('Card', True, (0, 0, 0))
# button2 = Button(button2X, button2Y, button2Width, button2Height)


run = True
while run:
    display_dealer_hand()
    display_player_hand()
    button1.draw()
    button2.draw()
    # button2.draw()
    # win.blit(buttonText1, (button1X + 25, button1Y + 15))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if button1X < x < button1X + button1Width and button1Y < y < button1Y + button1Height:
                print("Button 1 pressed")
                button1.pressed()
            if button2X < x < button2X + button1Width and button2Y < y < button2Y + button2Height:
                print("Button 2 pressed")
                button2.pressed()
