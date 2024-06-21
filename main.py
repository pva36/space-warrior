import pygame
import sys
import classes as c
import functions as f

# Screen max length constants

S_MAX_X = 256
S_MAX_Y = 240
S_SIZE = (S_MAX_X, S_MAX_Y)


# Game Palette
DARK = pygame.Color('#1b1233')
LIGHT = pygame.Color('#dcf29d')

# Player object
player = c.Player(0, 0)


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode(S_SIZE, pygame.SCALED)  # SCALED

    clock = pygame.time.Clock()
    running = True


    # Game Loop
    while running:

        # poll for events
        f.process_input(player)

        player.update_position(S_MAX_X, S_MAX_Y)

        # Game rendering
        screen.fill(DARK)

        player.update_image()

        screen.blit(player.image, player)


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()
