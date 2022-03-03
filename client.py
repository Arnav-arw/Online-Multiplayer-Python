import pygame
from network import network

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Client")

clientNumber = 0

class player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.rect = (x, y, width, height)
        self.vel = 5

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def readPos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(win, player1, player2):
    win.fill((255, 255, 255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = network()
    startPos = readPos(n.getPos())
    p1 = player(startPos[0], startPos[1] , 100, 100, (0, 255, 0))
    p2 = player(0, 0, 100, 100, (0, 255, 0))
    while run:
        p2Pos = readPos(n.send(makePos((p1.x, p1.y)))) 
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p1.move() 
        redrawWindow(win, p1, p2)

main()
