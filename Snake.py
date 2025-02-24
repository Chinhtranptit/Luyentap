import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
# Snake
snake = [(200, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))
# Apple
apple_pos = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
# Game variables
direction = 'UP'
