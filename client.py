from http import client
import pygame

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
        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(win, clientNumber):
    win.fill((255, 255, 255))
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render("Client " + str(clientNumber), 1, (0, 0, 0))
    win.blit(text, (250 - (text.get_width() / 2), 250 - (text.get_height() / 2)))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawWindow(win, clientNumber)
