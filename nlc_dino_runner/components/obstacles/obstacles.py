from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import SCREEN_WIDTH

#Clase Padre


class Obstacles(Sprite):

    def __init__(self, image, obstacle_type):
        self.image = image
        self.type = obstacle_type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH #1100

    def update(self, game_speed, obstacles_list):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles_list.pop()
    
    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)