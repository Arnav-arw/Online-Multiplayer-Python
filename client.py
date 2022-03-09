import pygame
from network import network
from player import player

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Client")

def redrawWindow(win, player1, player2):
    win.fill((255, 255, 255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = network()
    p = n.getP()
    while run:
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move() 
        redrawWindow(win, p, p2)

main()
