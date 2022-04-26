import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()-10
window.fill((0,0,0))
for i in range(0,10):
    for j in range(0,10):
        window.blit(robot, (70+((width/3)*i) + (width*j), 100 + (20*i)))
pygame.display.flip()

   
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
