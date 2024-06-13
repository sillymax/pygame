import pygame
import random

#Initialize pygame
pygame.init()

#Create display surface
width = 800
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("PEW PEW PEW")

#Set FPS and clock
fps = 60
clock = pygame.time.Clock()

#Set game values
player_velocity = 5
enemy_velocity = 5
num_enemies = 3
enemies = []

buffer_distance = 100

#Set images
background_image = pygame.image.load("assets/background.png")
player_image = pygame.image.load("assets/player.png")
player_rect = player_image.get_rect()
player_rect.left = 100
player_rect.centery = height//2

enemy_image = pygame.image.load("assets/enemy.png")
for _ in range(num_enemies):
    enemy_rect = enemy_image.get_rect()
    enemy_rect.left = random.randint(width, width + buffer_distance)
    enemy_rect.centery = random.randint(0, height - 48)
    enemies.append(enemy_rect)

def draw():
    window.blit(background_image, (0,0))
    window.blit(player_image, player_rect)
    for enemy_rect in enemies:
        window.blit(enemy_image, enemy_rect)

def enemy_movement():
    for enemy_rect in enemies:
        if enemy_rect.right < 0:
            enemy_rect.left = random.randint(width, width + buffer_distance)
            enemy_rect.centery = random.randint(0, height - 48)
        else:
            enemy_rect.x -= enemy_velocity

def main():
    running = True;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw()
        enemy_movement()
        pygame.display.update()
        clock.tick(fps)


main()