import pygame
import time
from sys import exit


from Cards import Card, cards
from network import Network
from multiprocessing.connection import Client

pygame.init()

width = 1000
height = 1000
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("UNO Client")

enableChangeColor = False
ChangeColorClicked = False

class Button:
    """
    INITIALIZATION
    
    """
    def __init__(self, text, color, x, y):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.width = 150
        self.height = 80
    
    """
    DRAW
    
    Draw button on the screen
    1. Draw Rectangle with color and sixe
    2. Create pygame.font.Sysfont object
    3. Will be drawn on screen
    
    """
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Merriweather", 40)
        text = font.render(str(self.text), 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def remove(self, win):
        pygame.draw.rect(win, (255,255,255), (self.x, self.y, self.width, self.height))
    """
    CLICK
    
    Check if button was clicked. It takes a position anc
    checks if it's within button's rectangle
    """
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False
    
class OnScreenCard(Button):

    def __init__(self, card: Card, x, y):
        self.card = card
        self.color = card.color
        self.ability = card.ability
        self.wild = card.wild
        self.text = str(card.number)
        self.x = x
        self.y = y
        self.width = 60
        self.height = 110

#  list is presumably used to store all OnScreenCard objects
onScreenCards = list()
"""
The drawButton and endTurnButton are instances of the Button class. They represent buttons that the player can click to draw a card or end their turn. The text, color, and position of each button are specified when they are created. The color is specified as an RGB tuple, and the position is specified as x and y coordinates. The size of these buttons is set to the default 
size specified in the Button class, which is 150x80 pixels.
"""
ChangeRed     = Button("Red", (255, 0, 0), 200, 700)
ChangeBlue    = Button("Blue", (0, 0, 255), 400, 700)
ChangeGreen   = Button("Green", (0, 255, 0), 200, 800)
ChangeYellow  = Button("Yellow", (250, 192, 32), 400, 800)

drawButton    = Button("Draw 1", (242, 51, 150), 500, 350)
endTurnButton = Button("End Turn", (242, 51, 150), 500, 450)
unoButton     = Button("UNO!", (242, 51, 150), 500, 550)

"""
WINDOW CLEARING

Clears the window by filling it with white color
"""
def redrawWindow(win, game, player):

    global onScreenCards
    global enableChangeColor

    win.fill((255,255,255))
    """
    WAITING FOR PLAYER
    
    If game has not been connected, it displays a "Waiting For Player" Message
    
    """
    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)

        win.blit(text, (int(width/2 - text.get_width()/2), int(height/2 - text.get_height()/2)))

    else:

        topCard = OnScreenCard(game.lastMove, 300, 500)
        topCard.draw(win)

        drawButton.draw(win)

        endTurnButton.draw(win)

        if topCard.wild != None:
            if game.turn == player:
                enableChangeColor = True
                ChangeRed.draw(win)
                ChangeBlue.draw(win)
                ChangeGreen.draw(win)
                ChangeYellow.draw(win)
            else:
                enableChangeColor = False
                ChangeRed.remove(win)
                ChangeBlue.remove(win)
                ChangeGreen.remove(win)
                ChangeYellow.remove(win)
        else:
            enableChangeColor = False
            ChangeRed.remove(win)
            ChangeBlue.remove(win)
            ChangeGreen.remove(win)
            ChangeYellow.remove(win)


        if game.turn == player:
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render("Your Move", 1, (0, 255,255))
            win.blit(text, (50, 50))

        else:
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render("Opponent\'s Move", 1, (0, 255,255))
            win.blit(text, (50, 50))

        XPosition = 50
        YPosition = 200

        updatedCards = []
        
        if player == 0:
            cardsToDraw = game.p1Cards
            if len(game.p1Cards) <= 2:
                unoButton.draw(win)
        else:
            cardsToDraw = game.p2Cards
            if len(game.p2Cards) <= 2:
                unoButton.draw(win)

        for playableCard in cardsToDraw:
            nextCard = OnScreenCard(playableCard, XPosition, YPosition)
            XPosition += 100
            nextCard.draw(win)
            updatedCards.append(nextCard)

        onScreenCards = updatedCards


    pygame.display.update()
    

def displayWinner(win, winner):
    font = pygame.font.SysFont("comicsans", 80)
    text = font.render(f"Player {winner} Wins!", 1, (0, 255, 0), True)
    win.blit(text, (int(width/2 - text.get_width()/2), int(height/2 - text.get_height()/2)))
    pygame.display.update()

def checkMove(move: Card, game) -> bool:

    lastMove = game.lastMove

    if move.number == lastMove.number:
        return True

    elif move.color == lastMove.color: 
        return True

    elif move.wild: 
        return True

    return False


def main():
    run = True
    global enableChangeColor
    global ChangeColorClicked
    global onScreenCards

    clock = pygame.time.Clock()
    n = Network()
    player = n.getPlayerNumber()
    pygame.time.delay(50)
    
    while run:
        try:
            game = n.send("get", "C")
        except:
            run = False
            print("Connection lost.")
            break

        # Check for a winner 
        winner = game.check_winner()

        if winner is not None:
            displayWinner(window, winner + 1) # Add 1 to convert player number to player index
            # Reset the game (you may need to modify the reset logic based on your game structure)
            n.send("reset", "C") # Assuming you have a reset method in your Game class

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if unoButton.click(pos) and game.connected():
                    if player % 2 == 0:
                        n.send("unop1", "C")
                    else:
                        n.send("unop2", "C")
                    print("UNO PRESSED")

                if game.turn == player:
                    if drawButton.click(pos) and game.connected():
                        game = n.send("draw", "C")

                    if endTurnButton.click(pos) and game.connected():
                        game = n.send("end", "C")

                    if game.lastMove.wild is not None:
                        if game.lastMove.wild == 'CC':
                            if ChangeRed.click(pos) and game.connected():
                                ChangeColorClicked = True
                                action = n.send("crcc", "C")
                            if ChangeGreen.click(pos) and game.connected():
                                ChangeColorClicked = True
                                action = n.send("cgcc", "C")
                            if ChangeBlue.click(pos) and game.connected():
                                ChangeColorClicked = True
                                action = n.send("cbcc", "C")
                            if ChangeYellow.click(pos) and game.connected():
                                ChangeColorClicked = True
                                action = n.send("cycc", "C")
                        else:
                            if ChangeRed.click(pos) and game.connected():
                                ChangeColorClicked = True
                                action = n.send("crp4", "C")
                            if ChangeGreen.click(pos) and game.connected():
                                ChangeColorClicked = True
                                action = n.send("cgp4", "C")
                            if ChangeBlue.click(pos) and game.connected():
                                ChangeColorClicked = True
                                action = n.send("cbp4", "C")
                            if ChangeYellow.click(pos) and game.connected():
                                ChangeColorClicked = True
                                action = n.send("cyp4", "C")

                    if ChangeColorClicked and enableChangeColor:
                        ChangeColorClicked = False
                        enableChangeColor = False
                        ChangeRed.remove(window)
                        ChangeBlue.remove(window)
                        ChangeGreen.remove(window)
                        ChangeYellow.remove(window)

                    for drawnCard in onScreenCards:
                        if drawnCard.click(pos) and game.connected():
                            if checkMove(drawnCard.card, game):
                                try:
                                    n.send("move", "C")
                                    n.send(drawnCard.card, "M")

                                except EOFError as e:
                                    print("EOF recd.")
                                    pass

        clock.tick(10)
        redrawWindow(window, game, player)

    pygame.quit()
    exit()

main()