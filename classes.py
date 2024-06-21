import pygame

class Player(pygame.Rect):
    def __init__(self, left, top, width=16, height=32):
        super().__init__(left, top, width, height)
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        # player_variables
        self.speed_x = 0
        self.speed_y = 0

        self.image_counter = 0

        self.walking = False

        # player_images
        self.walk_images = []
        self.walk_images.append(
            pygame.image.load('./assets/player_1_walk_01.png'))
        self.walk_images.append(
            pygame.image.load('./assets/player_1_walk_02.png'))
        self.walk_images.append(
            pygame.image.load('./assets/player_1_walk_03.png'))
        self.walk_images.append(
            pygame.image.load('./assets/player_1_walk_04.png'))

        self.image_index = 0

        self.image = self.walk_images[self.image_index]

    def update_image(self):
        if self.image_counter >= 10:
            self.image_counter = 0

        if self.walking:
            if self.image_counter == 0:
                self.image_index += 1
                if self.image_index >= len(self.walk_images):
                    self.image_index = 0

                self.image = self.walk_images[self.image_index]

        self.image_counter += 1

    def update_position(self, screen_max_x, screen_max_y):
        self.x += self.speed_x
        if self.x <= 0:
            self.x = 0
        elif self.x >= (screen_max_x - self.w):
            self.x = screen_max_x - self.w

        self.y += self.speed_y
        if self.y <= 0:
            self.y = 0
        elif self.y >= (screen_max_y - self.h):
            self.y = screen_max_y - self.h

    def update_player_movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.speed_x = -1
                self.walking = True
                self.image_counter = 0  # allows movement for every key press...
            if event.key == pygame.K_RIGHT:
                self.speed_x = 1
                self.walking = True
                self.image_counter = 0
            if event.key == pygame.K_UP:
                self.speed_y = -1
                self.walking = True
                self.image_counter = 0
            if event.key == pygame.K_DOWN:
                self.speed_y = 1
                self.walking = True
                self.image_counter = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.speed_x = 0
                self.walking = False
                # self.counter = 0
            if event.key == pygame.K_RIGHT:
                self.speed_x = 0
                self.walking = False
                # self.counter = 0

            if event.key == pygame.K_UP:
                self.speed_y = 0
                self.walking = False
                # self.counter = 0
            if event.key == pygame.K_DOWN:
                self.speed_y = 0
                self.walking = False
                # self.counter = 0
