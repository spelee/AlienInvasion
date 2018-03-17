import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Rocket")

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.ext()


        screen.fill((230, 230, 230))
        pygame.display.flip()


run_game()

