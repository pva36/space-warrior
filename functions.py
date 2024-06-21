import pygame
import sys


def process_input(player_obj):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #player movement
        player_obj.update_player_movement(event)
