import pygame
from resuable_functions import update_and_flip, dialogue
from chapter2.levels import level_four


pygame.init()

size = (800, 800)
white = (255, 255, 255)
blue = (0, 6, 40)
black = (0, 0, 0)


# Screen set up
screen = pygame.display.set_mode(size)

# Register images
brown_monkey = pygame.image.load('img/dream/brown_monkey.jpeg')
animation_object = pygame.transform.rotate(pygame.image.load('img/working_star.png').convert(), 20)
moon = pygame.image.load('img/dream/moon.jpeg')
dreamz1 = pygame.image.load('img/dream/dream13.png')
dreamz2 = pygame.image.load('img/dream/dream14.png')
dreamz3 = pygame.image.load('img/dream/dream15.png')
dreamz4 = pygame.image.load('img/dream/dream16.png')
dreamz5 = pygame.image.load('img/dream/dream17.png')
dreamz6 = pygame.image.load('img/dream/dream18.png')
dreamz7 = pygame.image.load('img/dream/dream19.png')
dreamz8 = pygame.image.load('img/dream/dream20.png')

# Flipping back and forth between windows....

def main():
    # Flashing monkey moon
    x = -200
    y = 0
    while x > -400:
        update_and_flip()
        screen.fill(black)
        screen.blit(brown_monkey, (-300, 0))
        pygame.time.delay(1500)
        update_and_flip()
        screen.fill(black)
        screen.blit(moon, (x, y))
        x -= 25
        y -= 25

    # Flashing dream backgrounds
    update_and_flip()
    screen.fill(black)
    screen.blit(dreamz1, (0, 0))
    pygame.time.delay(3000)
    update_and_flip()
    screen.fill(black)
    screen.blit(dreamz2, (0, 0))
    pygame.time.delay(3000)
    update_and_flip()
    screen.fill(black)
    screen.blit(dreamz3, (0, 0))
    pygame.time.delay(3000)
    update_and_flip()
    screen.fill(black)
    screen.blit(dreamz4, (0, 0))
    pygame.time.delay(3000)
    update_and_flip()
    screen.fill(black)
    screen.blit(dreamz5, (0, 0))
    pygame.time.delay(3000)
    update_and_flip()
    screen.fill(black)
    screen.blit(dreamz6, (0, 0))
    pygame.time.delay(3000)
    update_and_flip()
    screen.fill(black)
    screen.blit(dreamz7, (0, 0))
    pygame.time.delay(3000)
    update_and_flip()
    screen.fill(black)
    screen.blit(dreamz8, (0, 0))

    # Star animation
    x = 0
    y = 500
    while x < 700 and y < 700:
        update_and_flip()
        screen.blit(dreamz8, [0, 0])
        x += .75
        y -= .75
        screen.blit(animation_object, (x, y))
        pygame.display.flip()
        update_and_flip()

    screen.fill(black)
    update_and_flip()
    dialogue(' W h e n  a r e  y o u ?              ', 500, 200, 20)
    pygame.time.delay(3500)

    screen.fill(black)
    update_and_flip()
    dialogue(' W h e n  i s  a n y o n e ?              ', 500, 200, 20)
    pygame.time.delay(3500)
    # Run function to start next level
    level_four.game()
