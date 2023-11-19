import pygame
import sys
import random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), (70, 70))
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("pipe.mp3")
        self.rect.scale_by_ip(0.1, 0.1)
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y, scale=(70, 70)):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), scale)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)




pygame.init()
pygame.mixer.set_num_channels(20)

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("blue_background_color_153514_3840x2400.jpg")
pygame.mouse.set_visible(False)


clock = pygame.time.Clock()
crosshair = Crosshair("CROSSHAIR.png")
crosshair_image = pygame.transform.scale(pygame.image.load("CROSSHAIR.png"), (70, 70))

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for target in range(5000):
    new_target = Target("mark.jpg", random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    target_group.draw(screen)
    screen.blit(crosshair_image, (pygame.mouse.get_pos()[0]-35, pygame.mouse.get_pos()[1]-35))
    crosshair_group.update()