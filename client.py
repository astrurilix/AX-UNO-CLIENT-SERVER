import pygame # All the front end
import time # For delay, sleep, etc
from sys import exit # for exit()


from Cards import Card, cards
from network import Network # Custom network class
from multiprocessing.connection import Client # Multiprocessing client


pygame.init()

width = 1000
height = 1000
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("UNO Client")

class Button:
    def __init__(self, text, color, x, y):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.width = 150
        self.height = 80

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Merriweather", 40)
        text = font.render(str(self.text), 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

# Basically a button, just based on a card instead of on text and color
class OnScreenCard(Button):

    def __init__(self, card: Card, x, y):
        self.card = card
        self.color = card.color
        self.text = str(card.number)
        self.x = x
        self.y = y
        self.width = 60
        self.height = 110

onScreenCards = list()
drawButton    = Button("Draw 1", (242, 51, 150), 500, 350)
endTurnButton = Button("End Turn", (242, 51, 150), 500, 450)

def redrawWindow(win, game, player):
    """
    Redraws pygame window based on the current state of the game
    """

    global onScreenCards

    win.fill((255,255,255))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)

        win.blit(text, (int(width/2 - text.get_width()/2), int(height/2 - text.get_height()/2)))

    else:

        # Draw topmost card on screen
        topCard = OnScreenCard(game.lastMove, 300, 500)
        topCard.draw(win)

        # Draw the "Draw 1" button on screen
        drawButton.draw(win)

        # Draw the "End turn" button on screen
        endTurnButton.draw(win)

        if game.turn == player:
            # Player's turn turn
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render("Your Move", 1, (0, 255,255))
            win.blit(text, (50, 50))

        else:

            font = pygame.font.SysFont("comicsans", 60)
            text = font.render("Opponent\'s Move", 1, (0, 255,255))
            win.blit(text, (50, 50))

        # Draw all cards
        XPosition = 50
        YPosition = 200

        updatedCards = []
        
        if player == 0:
            cardsToDraw = game.p1Cards
        else:
            cardsToDraw = game.p2Cards

        for playableCard in cardsToDraw:
            nextCard = OnScreenCard(playableCard, XPosition, YPosition)
            XPosition += 100
            nextCard.draw(win)
            updatedCards.append(nextCard)

        onScreenCards = updatedCards


    pygame.display.update()


def checkMove(move: Card, game) -> bool:
    """
    Checks if the player's move was valid and returns a bool
    @Return: Bool indicating whether or not the move was valid.
    """
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Only handle this event if the player is on turn.
                if game.turn == player:
                    pos = pygame.mouse.get_pos()

                    if drawButton.click(pos) and game.connected():
                        game = n.send("draw", "C")

                    if endTurnButton.click(pos) and game.connected():
                        game = n.send("end", "C")

                    for drawnCard in onScreenCards:
                        if drawnCard.click(pos) and game.connected():
                            if checkMove(drawnCard.card, game):
                                try:
                                    # Send move
                                    n.send("move", "C")
                                    n.send(drawnCard.card, "M")

                                except EOFError as e:
                                    print("EOF recd.")
                                    pass

        clock.tick(10)
        redrawWindow(window, game, player)

main()