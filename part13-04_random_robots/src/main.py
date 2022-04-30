import pygame
import random

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
window.fill((0,0,0))

coords_list = []

for i in range (0, 1001):
    x = random.randint(0, 800 - width)
    y = random.randint(0, 800 - height)
    coords_list.append((x, y))


for tuple in coords_list:
    window.blit(robot, (tuple[0], tuple[1]))
pygame.display.flip()

   
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
