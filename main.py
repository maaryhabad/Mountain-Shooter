import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode((800, 600))
print('Setup End')

print('Loop Start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pass