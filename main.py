import pygame, sys
import math
pygame.init()

display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        display.blit(pygame.transform.scale(player_walk_images, (45,45)), (self.x-display_scroll[0], self.y-display_scroll[1]))

player_walk_images = pygame.image.load('sidescrollproject/assets/taxip.png')


player = Player(400, 300, 32, 32)

display_scroll = [0,0]

while True:
    display.fill((24,164,86))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        display_scroll[0] +=5
    if keys[pygame.K_d]:
        display_scroll[0] -=5
    if keys[pygame.K_w]:
        display_scroll[1] +=5
    if keys[pygame.K_s]:
        display_scroll[1] -=5

    player.main(display)


    clock.tick(60)
    pygame.display.update()
